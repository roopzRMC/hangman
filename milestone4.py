# %%
## Cylinder Class
import math
from site import removeduppaths
from typing import final

class Cylinder:

    def __init__(self, height, radius=1):
        self.height = height
        self.radius = radius
        self.surface_area = None
        self.volume=None


    def get_surface_area(self):
        self.surface_area =  round((2*math.pi*self.radius*self.height + 2*math.pi*self.radius**2), 2)
        return self.surface_area 
    
    def get_volume(self):
        self.volume =  round((math.pi*self.radius**2*self.height), 2)
        return self.volume
    


# %%
## Testing CYLINDER CLASS
myCyl = Cylinder(20,5)
# %%
myCyl.get_surface_area()
# %%
myCyl.get_volume()
# %%
myCyl.surface_area
# %%
myCyl.volume
# %%
## Hangman using OOP
import random

word_repo = ['sennheiser', 'hifiman', 'grado', 'final', 'akg', 'tinn']
word = random.choice(word_repo)

# %%
print(word)
# %%
## creating hangman in a procedural way

def check_guess_legacy():
    guess = input('enter a single letter to guess the word')
    remaining_lives = 3
    while remaining_lives > 0:
        if  guess in word:
            remaining_lives -=1
            print(f'congrats, your guess is in the word and you have {remaining_lives} remaining')
            guess = input('enter a single letter to guess the word')
        elif guess not in word and remaining_lives > 0:
            remaining_lives -=1
            print(f'sorry your guess is incorrect please try again and you have {remaining_lives} remaining')
            guess = input('enter a single letter to guess the word')
        else:
            print('you must now guess the word')
            break


def check_guess_new():
    remaining_lives = 3
    letters_guessed = []
    for i in range(0, remaining_lives):
        guess = input('enter a single letter to guess the word')
        remaining_lives -=1
        if guess in word and remaining_lives > 0:
            print(f'congrats, your guess is in the word and you have {remaining_lives} remaining')
            letters_guessed.append(guess)
        elif guess not in word and remaining_lives > 0:
            print(f'sorry your guess is incorrect please try again and you have {remaining_lives} remaining')
        elif remaining_lives == 0 and guess in word:
            letters_guessed.append(guess)
            print('your guess is correct but you have no remaining lives, please guess the word')
        elif remaining_lives == 0 and guess not in word:
            print('sorry your last guess was incorrect and you must guess the word')
    print(f'here are the correctly guessed letters {letters_guessed}')


        


def test_for_word():
    check_guess_new()
    while True:
        word_guess = str.lower(input('enter your word guess'))
        if word_guess == word:
            print('you have guessed the word')
            break
        elif word_guess != word and remaining_lives > 0:
            print('please try again')
        else:
            print('sorry you have lost hangman')
            break
        
        

# %%
test_for_word()# %%
word
# %%

import random

class Hangman():

    def __init__(self,lives=3):
        self.lives = lives
        self.word = None

    def choose_word(self):
        word_repo = ['sennheiser', 'hifiman', 'grado', 'final', 'akg', 'tinn']
        self.word = random.choice(word_repo)
        return self.word

    def check_guesses(self):
        remaining_lives = self.lives
        letters_guessed = []
        for i in range(0, remaining_lives):
            guess = input('enter a single letter to guess the word')
            remaining_lives -=1
            if guess in self.word and remaining_lives > 0:
                print(f'congrats, your guess is in the word and you have {remaining_lives} remaining')
                letters_guessed.append(guess)
            elif guess not in self.word and remaining_lives > 0:
                print(f'sorry your guess is incorrect please try again and you have {remaining_lives} remaining')
            elif remaining_lives == 0 and guess in self.word:
                letters_guessed.append(guess)
                print('your guess is correct but you have no remaining lives, please guess the word')
            elif remaining_lives == 0 and guess not in self.word:
                print('\n sorry your last guess was incorrect and you must guess the word')
        print(f'\n here are the correctly guessed letters {letters_guessed}')

    def play_the_game(self):
        self.check_guesses()
        while True:
            word_guess = str.lower(input('enter your word guess'))
            if word_guess == self.word:
                print('you have guessed the word')
                break
            else:
                print('sorry you have lost hangman')
                break



# %%
mygame = Hangman()
# %%
mygame.choose_word()
# %%
mygame.play_the_game()
# %%
