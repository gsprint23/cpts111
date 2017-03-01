
# coding: utf-8

# # [CptS 111 Introduction to Algorithmic Problem Solving](http://piazza.com/wsu/spring2017/cpts111/home)
# [Washington State University](https://wsu.edu)
# 
# [Gina Sprint](http://eecs.wsu.edu/~gsprint/)
# # L8-2 Iteration with For Loops
# 
# Learner objectives for this lesson
# * Generate random numbers
# * Repeat a sequence of Python statements using iterative constructs
# * Apply the `for` reserved keyword to construct loops

# ### Random Numbers
# To generate random numbers, we need to import the `random` module. Then, we will call the function `randrange(start, stop)` to generate a random number in the range `start` to `stop - 1`.

# In[1]:

import random

# get a random number in the range [0, 9] inclusive
rand_num = random.randrange(0, 10)
print(rand_num)

# alternative function
# get a random number in the range [0, 9] inclusive
rand_num = random.randint(0, 9)
print(rand_num)


# ## Application of `while` Loops: Generating Multiple Random Numbers
# Example problem: Write a program to display 10 random numbers in the range [1, 6] inclusive.

# In[10]:

import random

i = 0
while i < 10:
    rand_num = random.randrange(1, 7)
    print(rand_num)
    i += 1


# ## Another Application of `while` Loops: Menus
# Now, let's write a program that includes a menu for a game. Let's say the menu has 4 options:
# 1. View the game rules
# 1. Play the game
# 1. View the high score
# 1. Quit
# 
# Let's define 3 functions to implement this program:
# 1. `display_menu()`
# 1. `take_menu_action(choice)`
# 1. `main()`

# In[17]:

def display_menu():
    '''
    
    '''
    print("**Welcome to my game!**")
    print("Please choose from the following options")
    print("1) View the game rules")
    print("2) Play the game")
    print("3) View the high score")
    print("4) Quit")
   
def take_menu_action(choice):
    '''
    
    '''
    if choice == 1:
        # TODO call a function to display the rules
        pass
    elif choice == 2:
        # TODO call a function to play the game
        pass
    elif choice == 3:
        # TODO call a function to display the high score
        pass
    elif choice == 4:
        # TODO call a function to save the state of the game (e.g. high score)
        print("Thank you for playing")
    else:
        print("Not a valid menu option")
    
def main():
    '''
    
    '''
    choice = -1
    
    while choice != 4:
        display_menu()
        choice = int(input(">>"))
        take_menu_action(choice)

main()


# ## The `for` Loop
# In addition to `while` loops, Python has another type of loop, the `for` loop. `for` loops have the general template
# 
# ```
# for <item> in <sequence>:
#     <body>
# ```
# 
# Where `<sequence>` contains a *finite number of items* to be iterated through. If `<sequence>` is not finite, then we have an infinite loop!
# 
# ![](http://www.tutorialspoint.com/python/images/python_for_loop.jpg)
# (image taken from [http://www.tutorialspoint.com/python/images/python_for_loop.jpg](http://www.tutorialspoint.com/python/images/python_for_loop.jpg))

# ## `range()`
# Often we want to run a loop for sequence of values starting at `start`, ending at `stop`, and incrementing by `step`. For example, consider the first 20 even numbers. We want to start generating numbers at 2, end at 40 (and include 40), and increase by 2: 2, 4, 6, 8,..., 38, 40.
# 
# We can accomplish this by generating this sequence with the [`range()`](https://docs.python.org/3/library/functions.html#func-range) built-in Python function:
# 
# `range(start, stop, step)`
# 
# Let's re-write our "first 20 even number code" using a `for` loop:

# In[29]:

for number in range(2, 42, 2):
    print(number)
    
print("\n")

for number in range(2, 42):
    print(number)
    
print("\n")

for number in range(2):
    print(number)


# Note: `stop` specifies the index at which to terminate the loop. This is the Boolean condition, `number < stop`. When `number` equals or exceeds `stop`, the Boolean condition is `False` and the loop ends.
# 
# Note: If you do not specify a `step`, it is assumed to be 1: `range(0, 10)`
# 
# Note: If you only pass in one input argument to `range`, i.e. `range(10)`, `start` is assumed to be 0 and `stop` is the input argument value.
# 
# In summary: `range(0, 10, 1):` is equivalent to `range(0, 10):` is equivalent to `range(10):`
# 
# Try writing a program to prompt the user to enter a number, then using `for` loop to print as many stars as the number the user entered.

# In[4]:

num_stars = int(input("Please enter the number of stars to print: "))

for i in range(num_stars):
    print("*", end="")


# Let's re-write our transaction loop code to use `for` loops instead of `while` loops:

# In[27]:

def read_transaction_price():
    '''
    
    '''
    print("Please enter a transaction: ", end="")
    price = float(input())
    print(price)
    return price


def compute_total_spent_loop(num_transactions):
    '''
    
    '''
    total_spent = 0.0

    for i in range(num_transactions):
        # read in all num_transactions transactions from the user
        total_spent += read_transaction_price()
    return total_spent

print("Please enter the number of transactions: ", end="")
num = int(input())
total_spent = compute_total_spent_loop(num)
avg_spent_per_transaction = total_spent / num
print("On average, you spend %.2f per transaction" %(avg_spent_per_transaction))


# ## `while` or `for` Loops?
# When to use which loop? Each loop construct lends itself more suitable for certain tasks:
# 
# `for` loops:
# * Iterating through sequences
#     * Using `range()`
#     * Files
#     * Strings
#     * To be learned soon: lists, dictionaries
# * When we know the number of times we want to run our loop
# 
# `while` loops:
# * Prompting the user for input
#     * Menus
# * When we don't know the number of times we want to run our loop
# 

# ## TODO
# 1. Read Chapter 7 on iteration.
# 1. Get started with PA4, it's fun!
# 
# ## Next Lesson
# 1. Nested loops.
# 1. Guessing Game 2.0 :)
