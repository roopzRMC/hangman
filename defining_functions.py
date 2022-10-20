# %% This is a void function

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
