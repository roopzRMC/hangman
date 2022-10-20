# %% This is a void function

from cmath import pi


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
