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
        self.num_letters = len(list(set(self.word)))
        ## list of guesses
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            self.num_letters -= 1
            print(f'number of unique letters remaining is {self.num_letters}')
            print(f'Good guess! {guess} is in the word')
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            print(self.word_guessed)
            
        else:
            self.num_lives -= 1
            print(f'sorry {guess} is not in the word')
            print(f'you have {self.num_lives} left')
        self.list_of_guesses.append(guess)
        print(f'your list of guesses so far {self.list_of_guesses}')

    def ask_for_input(self):
        while True:
            guess = input('Please guess a letter')
            if len(guess) != 1 or not self.word.isalpha():
                print('Invalid letter. Please enter a single alphanumeric character')
            elif guess in self.list_of_guesses:
                print('You have already tried that letter')
            else:
                self.check_guess(guess)
                #self.list_of_guesses.append(guess)
                break


# %%
def play_game(word_list):
    game=Hangman(word_list, num_lives=5)
    while True:
        if getattr(game,'num_letters') > 0 and getattr(game,'num_lives') > 0:
            game.ask_for_input()
        elif getattr(game,'num_lives')  > 0 and getattr(game,'num_letters') == 0:
            print(f'Congrats, you won the game!!')
            break
        elif getattr(game,'num_lives')==0:
            print(f'You Lost!')
            break
# %%
headphones_list = ['sennheiser', 'akg', 'beyerdynamic', 'hifiman', 'audeze']
# %%
play_game(headphones_list)
# %%