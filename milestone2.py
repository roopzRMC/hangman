## Test for an input to be a single letter
while True:
    guess = str(input('enter a single letter'))
    if not (len(guess) == 1 and guess.isalpha()):
        print('try again please')
        continue
    else:
        print('well done')
        break