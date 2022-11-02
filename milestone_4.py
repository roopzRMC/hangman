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
        word_guessed = []
        for i in range(len(word)):
            word_guessed.append('_')
        ## number of unique letters
        num_letters = len(list(set(self.word)))
        ## list of guesses
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = str.lower(guess)
        if guess in self.word:
            print(f'Good guess! {guess} is in the word')
        else:
            print('please try again')

    def ask_for_input(self):

        while True:
            guess = input('Please guess a letter')
            if len(guess) != 1 and self.word.isalpha() ==False:
                print('Invalid letter. Please enter a single alphanumeric character')
            elif guess in self.list_of_guesses:
                print('You have already tried that letter')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                



"""
word_guessed: list - A list of the letters of the word, with _ for each letter not yet guessed. 
For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']. 
If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']

"""


# %%
myGame = Hangman(word_list = ['sennheiser', 'akg', 'beyerdynamic', 'hifiman', 'audeze'])
# %%
myGame.ask_for_input()
# %%
