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

    def __repr__(self):
        rep = 'You are playing a game of hangman with' + " " + str(self.lives) + " " + "lives"
        return rep

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
print(repr(mygame))
# %%
## Create a car class

class Car:
    def __init__(self, model, year=2022):
        self.model = model
        self.year = year
        self.miles_driven = 0
    
    def drive(self):
        print('VROOOM!')
        self.miles_driven +=1

    def info(self):
        return self.miles_driven, self.model, self.year



# %%
mysaab = Car(model='95')
# %%
mysaab.drive()
# %%
mysaab.info()
# %%
class Vector:
    def __init__(self, my_list = list()):
        self.my_list = my_list
        self.length = len(self.my_list)
    
    def __repr__(self):
        return "I am a vector mate"

    def __add__(self, other):
        return self.length + other.length
    
    def __getitem__(self, index):
        return self.my_list.__getitem__(self, index)


# %%
myvec1 = Vector(my_list=[7,8,9])

# %%
myvec1

# %%
myvec2 = Vector(my_list=[1,2,3,4])

# %%
myvec2.length
# %%
myvec1 + myvec2
# %%

# %%
print(bin(myvec1))
# %%

class Vector_2(list):

    def __add__(self, other):
        return self.length + other.length

    def __getitem__(self, index):
        if index == 0:
            raise ValueError
        index = index - 1
        return list.__getitem__(self, index)    
# %%
myvector = Vector_2([4,5,6,7,8])
# %%
myvector[1]
# %%
## Create a person class and compare dates of birth + add friends to both instances

from datetime import datetime
class Person:
    def __init__(self, name, date_of_birth, friend_list):
        self.name = name
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")
        self.friend_list = friend_list

    def add_friend(self):
        pass

    def __str__(self):
        return self.name + " " + str(self.date_of_birth) + " " + str(len(self.friend_list))

    def __gt__(self, other):
        return self.date_of_birth > other.date_of_birth

    def add_friend(self, friend):
        self.friend_list.append(friend.name)
        friend.friend_list.append(self.name)


# %%
frank = Person('Frank', '2019-02-10', friend_list=['gina', 'peepee', 'kwaku'])
# %%
leo = Person('Leo', '2017-01-01', friend_list = ['baba', 'shaba', 'kwaku'])
# %%
frank.add_friend(leo)
# %%
frank.friend_list
# %%
leo.friend_list
# %%
frank < leo
# %%
leo < frank
# %%
frank.date_of_birth
# %%
leo.date_of_birth

# %%
## Create a shape class - an Abstract Base Class!

class Shape:
    def __init__(self, num_sides, tesselates=None):
        if num_sides == 0:
            raise ValueError('you must enter 2 or more side')
        else:
            self.num_sides = num_sides
        self.tesselates = tesselates

    def get_info(self):
        raise NotImplementedError('this feature has not been implemented, pipe down mate')

    def __repr__(self):
        return self.get_info()

    def __add__(self, other):
        return self.num_sides + other.num_sides


# %%
## Create the child classes based on shape
class Triangle(Shape):
    def __init__(self, num_sides, tessalates=True):
        super().__init__(num_sides, tessalates)
    
    def get_info(self):
        return f'this shape has {self.num_sides} sides and tessalates is set to {self.tesselates}'


class Square(Shape):
    def __init__(self, num_sides, tessalates=True):
        super().__init__(num_sides, tessalates)

    def get_info(self):
        return 'this shape has ' + str(self.num_sides) + ' sides' + ' and tessalates is set to ' + str(self.tesselates)

class Pentagon(Shape):
    def __init__(self, num_sides, tessalates=None):
        super().__init__(num_sides, tessalates)

    def get_info(self):
        return 'this shape has ' + str(self.num_sides) + ' sides' + ' and tessalates is set to ' + str(self.tesselates)

class Hexagon(Shape):
    def __init__(self, num_sides, tessalates=True):
        super().__init__(num_sides, tessalates)
    
    def get_info(self):
        return 'this shape has ' + str(self.num_sides) + ' sides' + ' and tessalates is set to ' + str(self.tesselates)

class Circle(Shape):
    def __init__(self,num_sides = 0, tessalates=None):
        super().__init(num_sides, tessalates)
# %%
my_triangle = Triangle(3)
my_triangle.get_info()
# %%
my_square = Square(4)
# %%
my_pentagon = Pentagon(5)
my_pentagon

# %%
print(my_pentagon)
# %%
my_pentagon + my_square
# %%
