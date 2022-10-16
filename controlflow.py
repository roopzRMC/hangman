# %%
from enum import unique


weight = 400
height = 1.83
bmi = weight/height**2

# %%
print(bmi)
# %%
if bmi < 18.5:
    print(f'Your BMI is {bmi}. You are in the underweight range')
elif bmi > 18.5 and bmi < 24.9:
    print(f'your BMI is {bmi}. You are in the healthy weight range')
elif bmi > 24.9 and bmi < 29.9:
    print(f'Your BMI is {bmi}. You are in the overweight range')
elif bmi > 29.9 and bmi < 39.9:
    print(f'Your BMI is {bmi}. You are in the obese range')
else:
    print('your submission is out of range, please try again')
# %%
## Flight safety checker
altitude = 30000
air_speed = 22
# %%
if altitude < 100 or altitude > 50000:
    print('unsafe flying')
elif air_speed < 60 or air_speed > 500:
    print('unsafe flying')
else:
    print('all good')
# %%
## Order of conditions
x = int(input('Enter a number: '))

if x > 20: 
    print('x is greater than 20')
elif x > 15:
    print('x is greater than 15')
elif x > 0:
    print('x is greater than 0')
else:
    print('x is less than 0')
# %%
## Unique elements in a list
def unique_items_in_list(list):
    if len(list) == len(set(list)):
        print('all items in your list are unique')
    else:
        print('you have duplicate values in your list')
# %%
test_list = ['hello', 'please', 'indeed']

unique_items_in_list(test_list)
# %%
