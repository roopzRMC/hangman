# %%
def sum_to_one(n):
    if n==1:
        return n
    print(n)
    return sum_to_one(n-1) + n
# %%
sum_to_one(7)
# %%

def factorial(n):
  if n<2:
    return 1
  print(n*factorial(n-1))
  return n*factorial(n-1)