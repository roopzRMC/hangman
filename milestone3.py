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

# %% This is a void function

from cmath import pi
from math import factorial
from re import L


def my_void_function():
    print('this is a void function')
# %%
my_void_function()
# %%
def range_checker(lower_bound, upper_bound, number):
    if number > lower_bound and number < upper_bound:
        print(f'number is between {lower_bound} and {upper_bound}')
    else:
        print(f'number is NOT between {lower_bound} and {upper_bound}')
# %%
range_checker(2, 10, 6)
# %%
## volume of a sphere
def volume_of_sphere(radius):
    volume = round((4/3)*pi*radius**3, 2)
    return volume
# %%
volume_of_sphere(12)
# %%
# Fibonacci
import numpy as np
def fib_generator(n_terms):
    list = np.zeros(n_terms)
    list[1] = 1
    for i in range(2, len(list)):
        list[i] = list[i-2] + list[i-1]
    return list


# %%
ss = fib_generator(10)
# %%
ss
# %%
## Dictionary based function

clothing_dict = {'name':'uddie', 'price':'37', 'size':'xxl'}
# %%
type(clothing_dict)
# %%
clothing_dict['price']
# %%
def dict_printer(your_dict, attributes_to_print = 'all'):
    
    if attributes_to_print == 'all':
        key_list = []
        for i in your_dict.keys():
            key_list.append(i)
        for key in key_list:
            print(f'{key}, {your_dict[key]}')
    else:
        for i in range(0, len(attributes_to_print)):
            print(f'{attributes_to_print[i]}, {your_dict[attributes_to_print[i]]}')


# %%
dict_printer(clothing_dict, attributes_to_print=['name', 'size'])


# %%
## Profile validation
def profile_validation():

    def check_name():
        
        bad_chars = str('!@£$%^&*()')
        
        while True:
            name = input('enter your name')
            if bad_chars in name:
                name = input('please try again as you entered an invalid character')
            else:
                print('cheers for the name')
                break
        print(f'your name has been stored as {name}')
        return name
    
    name = check_name()  

    def check_age():

        while True:
            age = int(input('enter your age'))
            if age < 12:
                age = input('you must be over 12 to register')
            else:
                print('your age has been recorded')
                break
    
        return age

    age = check_age()

    def check_email():
        
        while True:
            email = input('enter a valid email')
            if '@' not in email:
                email = input('please make sure your email is valid')
            else:
                print('email registered')
                break
        return email
    
    email = check_email()
    print(f'{name}, {age}, {email}')
    #print(f'your name is {name}, your age is {check_age.age}, your email is {check_email.email}')

        

# %%
profile_validation()
# %%

## Recursion and factorial

# %%

def my_factorial(x):

    if x == 0:
        return 1
    else:
        return(x * factorial(x-1))
# %%
my_factorial(5)
# %%
## Recursive fibonacci
def fib_generator(n_terms):
    list = np.zeros(n_terms)
    list[1] = 1
    for i in range(2, len(list)):
        list[i] = list[i-2] + list[i-1]
    return list



def sum_to_one(n):
  result = 1
  call_stack = []
  
  while n != 1:
    execution_context = {"n_value": n}
    call_stack.append(execution_context)
    n -= 1
    print(call_stack)
  print("BASE CASE REACHED")

  while len(call_stack)!=0:
    return_value = call_stack.pop()
    print(call_stack)
    print(f"adding {return_value['n_value']} to {result}")
    result += return_value['n_value']
  return result, call_stack



sum_to_one(4)
    
# %%
## Recrusive fibonacci
def recursive_fib(n):
    if n<=1:
        return n
    else:
        return(recursive_fib(n-1) + recursive_fib(n-2))



# %%
l = recursive_fib(9)
# %%
print(l)
# %%
## The fibonacci loop
def div_7(term):
    if term%7 == 0:
        print(f'{term} is divisible by 7')
    else:
        print(f'{term} is not divisible by 7')

def term_size(term):
    if term >= 100 or term < 50:
        print(f'the number is either equal to or larger than 100 or or less than 50')


for i in range(1, 30):
    fib_term = recursive_fib(i)
    div_7(fib_term)
    term_size(fib_term)

# %%
## inverse the string if the start and end characters appear in the middle
test_string = "kwame"

def reverse_middle_chars(string):
    if len(string) == 0:
        return string
    elif (string[0] != len(string)//2 and string[-1] != len(string)//2+1):
        return string[-1] + reverse_middle_chars(string[:-1])
    else:
        return string

# %% 
reverse_middle_chars('hihhah')
# %%
## Palindrome detector

def palindrome_detector(string):
    if reverse_middle_chars(string) == string:
        print(f'{string} is a palindrome congrats')
    else:
        print('no palindrom detected')

# %%
palindrome_detector('hjabwala')

