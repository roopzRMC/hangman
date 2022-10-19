# %%
## Test whether the guess is the correct word
the_word = 'smarty'
while True:
    guess = str(input('guess which word im thinking of'))
    if not (guess == the_word):
        print('wrong word, please try again')
        continue
    else:
        print('congrats, correct guess')
        break

# %%
## Test whether the guess is in the word
the_second_word = 'surplusage'

while True:
    user_supplied_word = str(input('enter your word'))
    if not (user_supplied_word in the_second_word):
        print('sorry your word is not in the programmed word')
    else:
        print(f'well done {user_supplied_word} is in {the_second_word}')
        break
