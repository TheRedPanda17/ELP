class Player
    attr_accessor :symbol
    attr_reader :name, :wins

    @@current_players = 0
    def initialize(name)
        @name = name
        @wins = 0
        @@current_players += 1
        @symbol = @@current_players == 1 ? 'X' : 'O'
    end

    def add_win
        @wins += 1
    end

    def switch_symbol
        @symbol = @symbol == 'X' ? 'O' : 'X'
    end
end

class Slot
    attr_accessor :symbol

    def initialize
        @symbol = ' '
    end

    def occupied?; symbol != ' ' end
end

class WinnerFinder
    def initialize(board)
        @board = board
        clear_variables()
    end

    def clear_variables
        @row_total = [0,0,0]
        @col_total = [0,0,0]
        @diag_total = 0
        @reverse_diag_total = 0
    end

    def loop_board
        clear_variables()
        3.times do |row|
            3.times do |col|
                unless @board.slots[row][col].symbol == ' '
                    @reverse_diag_total += @board.slots[row][col].symbol == 'X' ? 1 : -1 if row + col == 2
                    @diag_total += @board.slots[row][col].symbol == 'X' ? 1 : -1 if row == col
                    @row_total[row] += @board.slots[row][col].symbol == 'X' ? 1 : -1
                    @col_total[col] += @board.slots[row][col].symbol == 'X' ? 1 : -1
                end
            end
        end
    end

    def get_winner_symbol
        loop_board()
        # Check if any of the totals are +3. If so, X's won
        if @reverse_diag_total == 3 || @diag_total == 3 || @row_total.any? {|total| total == 3} || @col_total.any? {|total| total == 3}
            'X'
        # Check if any of the totals are -3. If so, O's won 
        elsif @reverse_diag_total == -3 || @diag_total == -3 || @row_total.any? {|total| total == -3} || @col_total.any? {|total| total == -3}
            'O'
        else
            nil
        end
    end
end

class Board
    attr_reader :slots

    def initialize
        reset_board()
    end

    def filled?
        @slots.all? { |row| row.all? { |slot| slot.occupied? } }
    end

    def reset_board
        @slots = (1..3).map { |row| (1..3).map { |slot| Slot.new } }
    end
    
    def mark_slot(symbol, row, col)
        @slots[row][col].symbol = symbol
    end

    def to_s
        str = "\n #{@slots[0][0].symbol} | #{@slots[0][1].symbol} | #{@slots[0][2].symbol}"
        str += "\t 1 | 2 | 3\n"
        str += "---|---|---"
        str += "\t---|---|---\n"
        str += " #{@slots[1][0].symbol} | #{@slots[1][1].symbol} | #{@slots[1][2].symbol}"
        str += "\t 4 | 5 | 6\n"
        str += "---|---|---"
        str += "\t---|---|---\n"
        str += " #{@slots[2][0].symbol} | #{@slots[2][1].symbol} | #{@slots[2][2].symbol}"
        str += "\t 7 | 8 | 9\n\n"
    end
end

class GameLoop
    def initialize(board, player1, player2)
        @board = board
        @player1 = player1
        @player2 = player2

        @whos_turn = player1
        @game_turn = GameTurn.new(@board)
        @winner_finder = WinnerFinder.new(@board)
    end

    def play_tic_tac_toe
        @board.reset_board
        until game_over? do
            print_player_turn()
            @game_turn.take_turn(@whos_turn.symbol)
            change_turn()
        end
        get_winning_player()
    end

    def game_over?
        return @board.filled? || @winner_finder.get_winner_symbol()
    end

    def get_winning_player() 
        winner_symbol = @winner_finder.get_winner_symbol()
        winner = @player1.symbol == winner_symbol ? 
            @player1 :  
            @player2.symbol == winner_symbol ?
                @player2 : 
                nil
    end

    def change_turn 
        @whos_turn = @whos_turn == @player1 ? @player2 : @player1
    end    

    def print_player_turn
        puts "#{@whos_turn.name}'s turn. Type a number between 1-9 to place your '#{@whos_turn.symbol}.'"
    end
end

class GameTurn
    def initialize(board)
        @board = board
    end

    def take_turn(symbol)
        print @board
        slot_location = nil
        until slot_location do
            slot_number = gets.chomp

            if slot_number.to_i < 10 && slot_number.to_i > 0
                slot_location = convert_turn_number_to_slot_location(slot_number.to_i)

                if @board.slots[slot_location[:row]][slot_location[:col]].occupied?
                    slot_location = nil 
                    puts 'That slot is occupied!'
                end
            else
                puts 'Please enter a number between 1-9!'
            end
        end

        @board.mark_slot(symbol, slot_location[:row], slot_location[:col])
    end

    def convert_turn_number_to_slot_location (slot_number)
        row = slot_number < 4 ? 0 : slot_number < 7 ? 1 : 2
        col = slot_number % 3 - 1
        {row: row, col: col}
    end
end

class GameRunner
    def initialize(player1, player2)
        @player1 = player1 
        @player2 = player2
        @board = Board.new
        @game_loop = GameLoop.new(@board, @player1, @player2)
    end

    def run_game
        while play_again? do
            play_again()
            reset_game()
        end

        print "\nThanks for playing, #{@player1.name} and #{@player2.name}\n"
        print_score()
    end

    def play_again
        print_score()
        winner = @game_loop.play_tic_tac_toe()
        print_game_results(winner)
    end

    def play_again?
        return true if @player1.wins + @player2.wins == 0

        continue = ''
        until continue.upcase == 'Y' || continue.upcase == 'N' do
            print "\nPlay again? (y/n): "
            continue = gets.chomp
        end

        return continue.upcase == 'Y'
    end


    def reset_game
        @player1.switch_symbol()
        @player2.switch_symbol()
        @game_loop = GameLoop.new(@board, @player2, @player1)
    end        

    # Printing functions
    def print_game_results (winner)
        if winner
            puts "#{winner.name} has won the game!" 
            winner.add_win()
        else
            puts 'Tie Game!'
        end

        print @board
    end

    def print_score
        print "\nScore: #{@player1.name}: #{@player1.wins}, #{@player2.name}: #{@player2.wins}\n\n"
    end
end

# Play the game
print "\nWelcome to tic-tac-toe!\n"
print "\nEnter Player 1 Name: "
player1 = Player.new(gets.chomp)
print "\nEnter Player 2 Name: "
player2 = Player.new(gets.chomp)

game = GameRunner.new(player1, player2)
game.run_game()