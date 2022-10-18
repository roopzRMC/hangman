# %%
from curses.ascii import isalpha
import sys
## Append the path to add the folder to help find the module
sys.path.append('/Users/rupertcoghlan/import_challenge/people')
sys.path
# %%
import utils

# %%
utils.greeting()
# %%
from group import group_people
# %%
group_people
# %%
# %%
input('hello')
# %%
## Test for an input to be a single letter
guess = str(input('enter a single letter'))
while not (len(guess) == 1 and guess.isalpha()):
    print('try again')
    guess = str(input('oops, enter a letter again plz'))
else:
    print('yay')
