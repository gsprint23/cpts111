
# coding: utf-8

# # [CptS 111 Introduction to Algorithmic Problem Solving](http://piazza.com/wsu/spring2017/cpts111/home)
# [Washington State University](https://wsu.edu)
# 
# [Gina Sprint](http://eecs.wsu.edu/~gsprint/)
# # L6-1 Advanced If Statements
# 
# Learner objectives for this lesson
# * Apply nested `if` statements
# * Apply multiple alternative `if` statments (`elif`)

# ## Example Problem
# Suppose we want to write a game to have a user guess a number. We want to tell the user if they guess the number, if their guess is too high, or if their guess is too low.

# In[ ]:

num_to_guess = 4
players_guess = 0

print("Please enter a number between 1 and 10 inclusive")
players_guess = int(input())

if players_guess == num_to_guess: # BC1
    print("Congrats, you guessed the number correctly")
else:
    print("Unfortunately, you guessed the number incorrectly; however, I will give you a hint")
    
if players_guess > num_to_guess: # BC2
    print("Your guess was too high")

# Note how we do NOT want an else here, that would cause == to say your guess was too low
if players_guess < num_to_guess: # BC3
    print("Your guess was too low")


# ## Nested `if` Statements
# When a player's guess is not the number to guess (BC1 is False), we could give the hint in the body of the `else`. This would make sense because we only want to give a hint with BC1 is false, that is `players_guess != num_to_guess`. To do this, we can *nest* BC2 and BC3 in the `else` *body* of BC1 by indenting:

# In[9]:

num_to_guess = 4
players_guess = 0

print("Please enter a number between 1 and 10 inclusive")
players_guess = int(input())

if players_guess == num_to_guess: # BC 1
    print("Congrats, you guessed the number correctly")
else: # players_guess != num_to_guess:
    print("Unfortunately, you guessed the number incorrectly; however, I will give you a hint")
    if players_guess > num_to_guess: # BC 2
        print("Your guess was too high")
    # this fixes the boundary case of == num_to_guess that we had previously
    else: # players_Guess <= num_to_guess
        print("Your guess was too low")


# You can nest `if` statements as many times as you like; however, try to keep your code readable! Also, try to collapse your boolean conditions when appropriate. For example:

# In[4]:

num_guesses = 3

print("Please enter a number between 1 and 10 inclusive")
players_guess = int(input())

if players_guess != num_to_guess:
    if num_guesses > 0:
        print("You are wrong but you get to try again")
        
# the above nested if can collapse into a compound condition
if players_guess != num_to_guess and num_guesses > 0:
    print("You are wrong but you get to try again")


# ## Multiple-Alternative `if` Statements
# Sometimes we want to have multiple boolean conditions in the same block of mutually exclusive `if` statements. We can do this with *multiple-alternative if statements* and the `elif` keyword. `elif` stands for `else-if`. Think of `elif` like an `else` with a Boolean condition to test.
# 
# Consider yet another rewrite of the guessing game code:

# In[5]:

num_to_guess = 4
players_guess = 0

print("Please enter a number between 1 and 10 inclusive")
players_guess = int(input())

# a guess is either equal to, greater than, or less than 
if players_guess == num_to_guess: # BC 1
    print("Congrats, you guessed the number correctly")
elif players_guess > num_to_guess: # BC 2
    print("Your guess was too high")
else: # players_guess < num_to_guess
    print("Your guess was too low")


# Items to note about multiple-alternative if statements
# * Each condition is tested in order, from top to bottom (`if` first, then the first `elif`, then the second `elif`, etc., until the `else` if there is one). 
# * When a condition is true, the corresonding test body will be executed. No further tests will be evaluated.
#     * The bodies of the `if`, `elif`, and `else` statements are mutually exclusive. Only one body will execute.
#     * Even if more than one condition is true, only the body of the first true condition will execute.
# * If there is an `else` block in a multiple-alternative statement (there doesn't have to be an `else` block), it has to be last (meaning after the `if` and `elif` tests).

# ## Practice Problem
# Write a program to prompt the user to enter the current relative humidity (an integer between 0 and 100). Display a message according to the following table:
# 
# |Humidity|Message|
# |--------|-------|
# |20% or lower|Bone dry|
# |21% to 40%|Dry|
# |41% to 60%|Moderately dry|
# |61% to 80%|Moderately humid|
# |81% or higher|Humid|
# 
# You should have at least 2 functions in your program:
# 1. Prompts the user and reads in the humidity
# 1. Displays the corresponding message

# In[1]:

def get_humidity():
    '''
    
    '''
    print("Please enter the relative humidity, an integer between 0 and 100 inclusive")
    humidity = int(input())
    return humidity

def display_humidity_message(hum):
    '''
    
    '''
    if hum <= 20:
        print("Bone dry")
    elif hum <= 40:
        print("Dry")
    elif hum <= 60:
        print("Moderately dry")
    elif hum <= 80:
        print("Moderately humid")
    else:
        print("Humid")
        
def main():
    '''
    
    '''
    rel_humidity = get_humidity()
    display_humidity_message(rel_humidity)

main()


# We can rewrite `display_humidity_message()` to return the message instead of display it (let's rename the function `compute_humidity_message()`. We could then write another function to display the message:

# In[2]:

def compute_humidity_message(hum):
    '''
    
    '''
    if hum <= 20:
        return "Bone dry"
    elif hum <= 40:
        return "Dry"
    elif hum <= 60:
        return "Moderately dry"
    elif hum <= 80:
        return "Moderately humid"
    else:
        return "Humid"
        
def display_humidity_message(msg):
    '''
    
    '''
    print("The relative humidity is \"%s\"" %(msg))
    
def main():
    '''
    
    '''
    rel_humidity = get_humidity()
    humidity_message = compute_humidity_message(rel_humidity)
    display_humidity_message(humidity_message)

main()


# ## TODO
# 1. Study for midterm #1
# 1. Work on PA3
# 
# ## Next Lesson
# We are going to learn about iterative statements! These are awesome because we can repeat code lots of times without typing it out over and over again. We will take our guessing game to the next level by letting a user repeatedly make a guess until they guess correctly. Of course, we will still give the hints!
