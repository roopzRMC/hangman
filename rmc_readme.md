# Learnings: Hangman milestone 1 - 3

> Version Control

Github:
- Staging
- Committing
    - Writing good commit messages
- Branching
- Pull Requests


> Lists
- Indexing
- Slicing


> Strings
- Splitting string into indiviudal characters
- casting strings to lower or upper case
- leveraging set theory to determine whether one string is or is not found in another
```
string.split()
string.tolower()
string.toupper()

```


> While Loops & Control Flow
- While and and While Not

Knowing when to use a for or while loops is important:
- in a for loop you know / specify how many interations there need to be
- in a while loop you DONT know how many and there for you need to specify a break to eventually exit the loop

```
while True:
    guess = str(input('guess which word im thinking of'))
    if not (guess == the_word):
        print('wrong word, please try again')
        
    else:
        print('congrats, correct guess')
        break
```

> Beginning of OOP
- Writing a class and and instantiating
```
class ss():
    def __init__(self):

```
> Scripts destined to be a module to imported in to another script
```
if__name__="__main__":
```
This is used to protect users from invoking the script when they didnt intend to. If this is not present and the module is called - the script runs. The code block above 'hosts the code'

In addition you need to add the module to the path using SYS
```
import sys
sys.path.append('/Users/rupertcoghlan/import_challenge/people')
sys.path
```
> Context Manager

Context managers allow you to allocate and release resources precisely when you want to - a typical example of this is where you are reading from a file 
```
with open('some_file', 'w') as opened_file:
    opened_file.write('Hola!')
```
> Functions

The structure of the function is as follows

```
def function_name(args):
    some code

    return something
```
A function that does not return something is called a **VOID FUNCTION**

A function call would be

```
function_x()
```

>> Scope
### Local
- Local variables are defined **inside** a function
- These variables **cannot** be referenced from outside the function

### Global
- These are variables defined outside of a function
- They **can** be referenced outside of a function

>> Multiple Arguments
- Many single arguments are provided as a tuple
```
def get_mean(*args):
    total = sum(args)
    return total/len(args)
```
- Key word arguments are specified as
```
def test_kwargs(**kwargs)
    print(kwargs)

test_kwargs(a=1, b=2 .....)
```
> Recursion

The definition means to 're-occur'
In its most basic form recursion takes a base case and the recursive step

### Iteration
- This requires a conting var and a boolean condition
- You  iterate through the list until you have reached the expected length

### Recursive
- The best case dictated whether the function recurses or calls itself

> Object Orientated Programming

Classes are blueprints for creating objects containing;
- Attributes
- Methods

Classes can also feature inheritance;
- Multiple Inheritance;
    - Class being derived from more than one base class

```
class Base1:
    pass

class Base2:
    pass

class multi(Base1, Base2):
    pass

```

- Multi-level inheritance
    - Classes that inherit from a parent but can have multiple 'generations' from one base class


```
issubclass() + isinstance()
```

Above represent methods that can be run to determine relationships

### Overriding Parent Methods
Using .mro (Method Resolution Order) provides the order in which the child will search the parents' methods
- This can be important when inspecting errors you encounter around parent classes being searched for an attribute that is NOT required for a child

- Classes should be designed so that they are in sync
    - names of methods shouldbe adjusted slightly, eg a Triangle (inheriting from a square could be named [tri_area])

### Abstract Base Classes
- Used as a template for a template
- They force the children to have certain methods

### Magic Methods
Enable use of pythons built in functions in classes including;
```
__len__ -> defining the how the len function when called on the class
__add__ -> defining addition
__gt__  -> greater than
__eq__  -> equals
__lt__  -> less than
__repr__ -> what is printed when you print(Class)
```
