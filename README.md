# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

milestone_1:
- made a word list and picked a random one
- asked used to guess one letter and verified its just one alphabetical letter

milestone_2:
- made function check_guess() which checks if the letter that was guessed is in the random word that was picked
- made function ask_for_input() which makes user guess a letter in a while loop until the guessed letter is a singular alphabetical letter

milestone_3:
- created Hangman class
- put ask_for_input and check_guess into class
- ask_for_input: check if guess is valid and if its non repeating ->then call check_guess
- check_guess: if guess in word: fill in word_guessed list with guess. else: reduce number of lives