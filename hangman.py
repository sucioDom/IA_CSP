 # IA, hangman.py
import random

# create a list of 10 words on a seperate txt file

# create another file holds  win/losss counts

# use split(",") on the count of words txt document to create your list of words

#pull win and lose total from the other txt file and save them as 2 seperate veriables 

# build the hangman game

#save the correct word as a veriable random.choice(name of the list 

#number of wrong guesses

ssed

#What letters have been gue

 #function too diplay the hangman
"""______
   |    |
   |    O
   |   /|\\
   |   /  \\
   |__________
"""
#function to show the letters and space(The correct word, letters that have been guessed)
# loop over the correct word
    # variable for display word(start as an empty string)
    #check if letter has been guessed
        #then add the letter to the display word
    #if they haven't guessed the letter
        # add an underscore to the display word
# returns the finished display word (outside of the loop)




# Main game loop (while True)
    #call function to show hangman
    # print function call to show display word
    # create variable and ask user to guess a letter
    # add the letter to list of guessed letters
    # check if not letter in word:
        # increase incorrect guesses
    #check if display word is the same as the word
        # Tell the user they won!
        # increase win total
        #ask them if they want to play again
            #reset random word, rest wrong guess
    #check to see if they lost (if they have 6 wrong guesses)
        #tell them they lost
        #tell them what the word was
        #Increase the lost count
        #ask if they want to play again
                    #reset random word, rest wrong guess count)
