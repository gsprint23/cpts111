
# coding: utf-8

# # [CptS 111 Introduction to Algorithmic Problem Solving](http://piazza.com/wsu/spring2017/cpts111/home)
# [Washington State University](https://wsu.edu)
# 
# [Gina Sprint](http://eecs.wsu.edu/~gsprint/)
# # L9-1 Advanced Loops
# 
# Learner objectives for this lesson
# * Learn about `break` statements
# * Learn about nested loops

# ## Review of Loops
# What is the output of the following loops? Remember to draw tables!
# 

# In[ ]:

# 1
x = 0
while x < 5:
    print("%d" %(x), end="")
    x += 1


# In[ ]:

# 2
x = 0
while x < 5:
    x += 1
    print(x)


# In[ ]:

# 3
x = 5
while x < 0:
    print(x)
    x += 1


# In[ ]:

# 4
x = 5
while x < 10:
    print(x)
    x -= 1


# In[ ]:

# 5
x = 0
while x < 5:
    print(x)
x += 1


# In[ ]:

# 6
x = 0
while x < 5:
    x += 1
print(x)


# In[ ]:

# 7 error
x = 0
while x < 5:
print(x)
x += 1


# In[ ]:

# 8
for x in range(0, 3, 1):
    print(x)


# In[ ]:

# 9
for i in range(1, 7, 2):
    print(i, end="")


# ## `break` Statement
# Sometimes we need to "break" out of a loop early, i.e. before the Boolean condition is `False`. We can accomplish this anywhere in the body of the loop with the `break` statement. 
# 
# As an example, suppose we want to get input from the user until they enter the string "stop". When the user enters "stop", we want to stop getting numbers from the user and take an early exit of our loop:

# In[1]:

while True:
    line = input("Please enter a string: ")
    if line == "stop":
        break


# ## Nested Loops
# Loops within loops! Just like how we can have `if` statements within `if` statements (nested `if` statements), we do the same with loops. We just need to be conscientious of:
# * Indenting the bodies of the loops correctly
# * Progress towards all of the Boolean conditions eventually being false

# In[2]:

for i in range(0, 5):
    print("%d " %(i), end="")
    for j in range(0, i):
        print("%d" %(j), end=" ")
    print("")


# It can be helpful to keep track of the loop control variables with a table:
# 
# |i|j|output|
# |-|-|-|
# |0|0|0 \n|
# |1|0,1|1 0 \n|
# |2|0,1,2|2 0 1 \n|
# |3|0,1,2,3|3 0 1 2 \n|
# |4|0,1,2,3,4|4 0 1 2 3 \n|
# |5||End loop|

# ### Example Problem #1
# Write a program to prompt the user to enter the number of lines of stars to print. On each line, there will be as many stars printed as the line number. For example, if the user enters 5, the first line will have 1 star, the second line will have 2 stars, etc., until the 5th line, which will have 5 stars:
# 
# ```
# * 
# **
# ***
# ****
# *****
# ```

# In[ ]:




# ### Example Problem #2
# Now try and print it the other way, with `num_lines` stars on the first line, `num_lines - 1` on the second, etc.

# In[ ]:




# ### Example Problem #2 Alternative Solution
# We could rewrite the above nested loop to instead use a single loop and the string repetition operator "*":

# In[ ]:




# ## Guessing Game 2.0
# Let's add functionality to the guessing game to allow a user to play the game as many times as they want. This will require an outer menu loop to keep the guessing game going until the user wants to quit, and an inner loop to guide the user to the correct answer.

# In[3]:

import random

def display_menu():
    '''
    
    '''
    print("\n**Welcome to the guess my number game!**")
    print("Please choose from the following options")
    print("1) View the game rules")
    print("2) Play the game")
    print("3) Quit")

def display_game_rules():
    '''
    
    '''
    print("The rules are fairly straightforward.")
    print("Guess a number and I will tell you if you are correct, too high, or too low")
    
def play_guessing_game():
    '''
    
    '''
    num_to_guess = random.randrange(1, 11)
    players_guess = 0
    correct = False

    while not correct:
        print("Please enter a number between 1 and 10 inclusive")
        players_guess = int(input())

        # a guess is either equal to, greater than, or less than 
        if players_guess == num_to_guess: # BC 1
            print("Congrats, you guessed the number correctly")
            correct = True # exit loop
        elif players_guess > num_to_guess: # BC 2
            print("Your guess was too high")
        else: # players_guess < num_to_guess
            print("Your guess was too low")
    
    
def take_menu_action(choice):
    '''
    
    '''
    if choice == 1:
        display_game_rules()
    elif choice == 2:
        play_guessing_game()
    elif choice == 3:
        print("Thank you for playing")
    else:
        print("Not a valid menu option")
    
def main():
    '''
    
    '''
    choice = -1
    
    while choice != 3:
        display_menu()
        choice = int(input(">>"))
        take_menu_action(choice)

main()


# ## TODO
# 1. Work on PA4.
# 
# ## Next Lesson
# 1. We start File I/O!
