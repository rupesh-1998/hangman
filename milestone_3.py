import random
from hangman_visuals import lives_visual_dict, win, lose

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word = 'aapple'#random.choice(word_list)
        self.word_guessed = ['' for i in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            inds = [i for i in range(len(self.word)) if self.word[i] == guess]
            for i in inds:
                self.word_guessed[i] = guess
            self.num_letters += -1
        else:
            self.num_lives += -1
            print(f'Sorry, {guess} is not in the word. You have {self.num_lives} lives left.')
            
        self.list_of_guesses.append(guess)
        print(f'Guesses: {self.list_of_guesses}.\n')

    def ask_for_input(self):
        #while(True):
            print('\n------------------------------------------------------')
            guess = input('--Enter a letter: ')
            if len(guess)!=1 or guess.isalpha()==False:
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter')
            else:
                self.check_guess(guess)
                #self.list_of_guesses.append(guess)



def play_game():
    word_list = ['apple', 'banana', 'watermelon', 'orange', 'grapefruit']
    game = Hangman(word_list, num_lives = 7)

    while(True):
        print(lives_visual_dict[game.num_lives])
        print('Word:', game.word_guessed)
        if game.num_lives == 0:
            print('\nYou lost!')
            print(lose)
            print(f'The word was {game.word}.')
            break
        if game.num_letters > 0:
            game.ask_for_input()
        if game.num_lives != 0 and game.num_letters <= 0:
            print('\nCongratulations! You won!')
            print(win)
            print(f'The word was {game.word}.')
            break

play_game()
