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
end

class Slot
    attr_accessor :symbol, :occupied

    def initialize
        @symbol = ' '
        @occupied = false
    end
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

    def get_winner
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
        @slots.all? { |row| row.all? { |slot| slot.occupied } }
    end

    def reset_board
        @slots = (1..3).map { |row| (1..3).map { |slot| Slot.new } }
    end

    def take_turn(symbol, next_slot)
        # Convert from slot to 2d array
        row = next_slot < 4 ? 0 : next_slot < 7 ? 1 : 2
        col = next_slot % 3 - 1
        slot = @slots[row][col]

        if slot.occupied
            puts 'This slot is already taken. Try somewhere else'
        else
            slot.symbol = symbol
            slot.occupied = true
        end
    end
    
    # X's are positive, O's are negative

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

class Game
    def initialize(player1, player2)
        @player1 = player1 
        @player2 = player2
        @board = Board.new
        @winner_finder = WinnerFinder.new(@board)
    end

    def start
        @whos_turn = @player1
        start_game_loop()
    end

    private
    def start_game_loop
        play_again = true
        
        # Outside loop for multiple games 
        while play_again? do
            reset_game()
            print_score()

            # Single game loop
            until game_over? do
                print_player_turn()
                try_turn()
            end

            print_game_results()
        end

        print "\nThanks for playing, #{@player1.name} and #{@player2.name}\n"
        print_score()
    end

    def reset_game
        games_played = @player1.wins + @player2.wins
        @whos_turn = games_played % 2 == 0 ? @player1 : @player2

        unless @whos_turn.symbol == 'X'
            if @whos_turn == @player1
                @player1.symbol = 'X'
                @player2.symbol = 'O'
            else
                @player1.symbol = 'O'
                @player2.symbol = 'X'
            end
        end

        @board.reset_board()
    end

    def try_turn 
        print @board
        next_slot = nil
        until next_slot do
            next_slot = gets.chomp

            if next_slot.to_i < 10 && next_slot.to_i > 0
                next_slot = next_slot.to_i
                turn_result = @board.take_turn(@whos_turn.symbol, next_slot)

                if turn_result
                    change_turn()
                else
                    next_slot = nil
                end
            else
                puts 'Please enter a number between 1-9!'
                next_slot = nil
            end
        end
    end

    def change_turn 
        if @whos_turn == @player1
            @whos_turn = @player2
        else
            @whos_turn = @player1
        end
    end            

    # Boolean functions
    def game_over?
        return @board.filled? || @winner_finder.get_winner()
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

    # Printing functions
    def print_game_results 
        winner_symbol = @winner_finder.get_winner()
        winner = @player1.symbol == winner_symbol ? 
            @player1 :  
            @player2.symbol == winner_symbol ?
                @player2 : 
                nil

        if winner
            puts "#{winner.name} has won the game!" 
            winner.add_win()
        else
            puts 'Tie Game!'
        end

        print @board
    end

    def print_player_turn
        puts "#{@whos_turn.name}'s turn. Type a number between 1-9 to place your '#{@whos_turn.symbol}.'"
    end

    def print_score
        print "\nScore: #{@player1.name}: #{@player1.wins}, #{@player2.name}: #{@player2.wins}\n\n"
    end
end

# Play the game
print "\nWelcome to tic-tac-toe!\n"
print "\nEnter Player 1 Name: "
player_name = gets.chomp
player1 = Player.new(player_name)
print "\nEnter Player 2 Name: "
player_name = gets.chomp
player2 = Player.new(player_name)

game = Game.new(player1, player2)
game.start()