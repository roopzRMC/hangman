# %%
from curses.ascii import isalpha
import random
## Defining the Hangman Class
class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        ## initialise the word list
        self.word_guessed = []
        for i in range(len(self.word)):
            self.word_guessed.append('_')
        ## number of unique letters
        self.num_letters = len(set(self.word))
        ## list of guesses
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word')
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            print(self.word_guessed)
            self.num_letters -= 1
            
        else:
            self.num_lives -= 1
            print(f'sorry {guess} is not in the word')
            print(f'you have {self.num_lives} left')
        self.list_of_guesses.append(guess)
            

    def ask_for_input(self):

        while True:
            guess = input('Please guess a letter')
            if len(guess) != 1 or not self.word.isalpha():
                print('Invalid letter. Please enter a single alphanumeric character')
            elif guess in self.list_of_guesses:
                print('You have already tried that letter')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                



# %%
myGame = Hangman(word_list = ['sennheiser', 'akg', 'beyerdynamic', 'hifiman', 'audeze'])
# %%
myGame.ask_for_input()
# %%
