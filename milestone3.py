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