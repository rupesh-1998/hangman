import random

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word = random.choice(word_list)
        self.word_guessed = ['' for i in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')
            for i in self.word:
                if i==guess:
                    ind = self.word.index(i)
                    self.word_guessed[ind] = guess
            self.num_letters += -1
        else:
            print(f'Sorry, {guess} is not in the word.')
            self.num_lives += -1
            print(f'You have {self.num_lives} lives left')
        #self.list_of_guesses.append(guess)

    def ask_for_input(self):
        while(True):
            guess = input('Enter a letter: ')
            if len(guess)!=1 or guess.isalpha()==False:
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)




word_list = ['apple', 'banana', 'watermelon', 'orange', 'grapefruit']
Hangman(word_list).ask_for_input()
