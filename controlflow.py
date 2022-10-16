# %%
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
