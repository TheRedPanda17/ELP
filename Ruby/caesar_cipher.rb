def caesar_cipher(str, shiftNum)
    alpha = 'abcdefghijklmnopqrstuvwxyz'.split('')                              # Define alphabet
    shiftedStr = str.split('').map do |char|                                    # Map the passed in string
        (char =~ /[[:alpha:]]/) ?                                               # Check if character
            alpha.include?(char) ?                                              # Check if lower case
                alpha[(alpha.index char) + shiftNum - 26] :                     # Return shifted lowercase
                alpha[(alpha.index char.downcase) + shiftNum - 26].upcase :     # Return downcased, shifted, upcased
        char                                                                    # Return punctuation
    end
    shiftedStr.join('')                                                         # Join and return char array
end

# Run program
print "\nType a message to be encrypted: "
str = gets.chomp
print "Type how many positions would you like to shift the message by: "
num = gets.chomp.to_i
print "\nHere is your new message: \n\n#{caesar_cipher(str, num)}\n\n"