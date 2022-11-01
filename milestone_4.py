# %%
import random
## Defining the Hangman Class
class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        word = random.choice(self.word_list)
        ## initialise the word list
        word_guessed = []
        for i in range(len(word)):
            word_guessed.append('_')
        ## number of unique letters
        num_letters = len(list(set(word)))
        ## word list
        word_list = ['sennheiser', 'akg', 'beyerdynamic', 'hifiman', 'audeze']
        ## list of guesses
        list_of_guesses = []



"""
word_guessed: list - A list of the letters of the word, with _ for each letter not yet guessed. 
For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']. 
If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']

"""

