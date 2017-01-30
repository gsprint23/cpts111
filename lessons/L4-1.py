
# coding: utf-8

# # [CptS 111 Introduction to Algorithmic Problem Solving](http://piazza.com/wsu/spring2017/cpts111/home)
# [Washington State University](https://wsu.edu)
# 
# [Gina Sprint](http://eecs.wsu.edu/~gsprint/)
# # L4-1 Functions
# 
# Learner objectives for this lesson
# * Call and define functions

# ## Example: Average of 3 GPAs
# Problem Statement: Write a program that computes your grade point average (gpa) after completion of 3 courses.
# 
# Inputs:
# * Grade point and number of credits for course 1
# * Grade point and number of credits for course 2
# * Grade point and number of credits for course 3
# 
# Outputs
# * Grade point average (GPA)
# Relevant formula: `GPA = ((grade_point1 * num_credits1) + (grade_point2 * num_credits2) + (grade_point3 * num_credits3)) / total_num_credits`
# 
# ### Algorithm
# 1. Get the grade points earned from each class
# 1. Get the credit hours for each class
# 1. Compute the credits hours earned
#     * `weighted_credits = (grade_point1 * num_credits1) + (grade_point2 * num_credits2) + (grade_point3 * num_credits3)`
# 1. Compute the total number of credits
#     * `total_num_credits = num_credits1 + num_credits2 + num_credits3`
# 1. Compute the average of the grade points
#     * `gpa = weighted_credits / total_num_credits`
# 1. Display the results  
# 
# ### Implementation

# In[8]:

# get grade point and credit hours for each class
print("Please enter the grade point for your computer science course: ")
gp1 = float(input())
print("Please enter number of credits for your computer science course: ")
num_credits1 = int(input())

print("Please enter the grade point for your math course: ")
gp2 = float(input())
print("Please enter number of credits for your math course: ")
num_credits2 = int(input())

print("Please enter the grade point for your karate course: ")
gp3 = float(input())
print("Please enter number of credits for your karate course: ")
num_credits3 = int(input())

# compute the weighted credit hours earned
weighted_credits = (num_credits1 * gp1) + (num_credits2 * gp2) + (num_credits3 * gp3)

# compute the total number of credits earned
total_num_credits = num_credits1 + num_credits2 + num_credits3

# copute the average of the grade points
gpa = weighted_credits / total_num_credits

# display the results to the user
print("Your GPA is: %.2f" %(gpa))


# What do you think of this example? It seems redundant, right? We're using the exact same sequence of commands (`print()` and `input()`) to obtain the three grade points and credits. If we wanted to change the prompt for entering the grade point (or number of credits), we would have to change the prompt in 3 different spots...
# 
# Is there a better (less redundant, easier to read, more concise) way to approach this problem? Enter: Functions!!

# ## Functions
# A **function** is a named sequence of statements that performs a computation. You can think of a function as a self-contained "mini-program" that solves a problem.
# 
# General rule-of-thumb: **1 function = 1 task = 1 algorithm**
# 
# You already have some practical understanding of functions from your mathematical background: $f(x) = x^2 - 4x + 4$. We pass the value of $x$ into a function called "$f$" and get a result back. 
# 
# In programming, we say a function *takes an argument* and *returns a result*.
# 
# ### Calling a Function
# Python functions can accept "input arguments"
# * The inputs to the function
# 
# Python functions may return results via a reserved keyword `return` statement that specifies the "output arguments" (also called "output parameters")
# * The outputs of the function
# 
# We have already used functions and seen them in action:

# In[ ]:

# type() is a function that accepts an argument and returns the data type of the argument
# type is the function name
# 42 is the argument
# data_type stores the return value from type
data_type = type(42)


# Now, we are going to learn how to write our own functions!
# 
# ### Defining a Function
# A *function definition* specifies the name of the function and the statements to be executed when the function is "called". We call a program by its name when we want to run it. A function definition follows the general template:
# ```
# def <function_name>(input parameters)
#     '''
#     docstring
#     '''
#     executable statements
#     ...
#     return <output parameters>
# ```
# There are several aspects of a function to note:
# * `def` is a keyword that let's Python know you are about to declare a function
# * The function name should follow similar naming conventions and style guidelines as variable names. Note that function names are user-defined identifiers and should not redefine standard-identifiers (e.g. built-in functions) or previously declared user-identifiers (e.g. your own variables you've already declared).
# * The input parameters represent data coming in to your function. Don't forget the colon after the last paren.
# * Together, `def`, function name, and input parameters form the *function header*
# * The remaining portion of the function is called the *function body*. **All statements of the function body should be indented 4 spaces**. Indentation is how Python *groups* the code you've written with the function header to collectively form the *function definition*.
# * A multi-line comment, called a docstring, immediately follows the function header. This is where you explain what the function does, what inputs it expects, what outputs it produces, what assumptions the function makes, etc. When you type `help(<function_name>)`, the text in the docstring is what shows up (cool!).
# * Following the docstring are one or more executable statements.
# * `return` statements specify the output parameters (results) of your function. Although you can have multiple return statements, in this class we will typically only have one (good style usually dictates only having one return statement per function anyways).

# ## GPA Example Revisited: Enter Functions
# Let's write a function called `get_grade_point()`:

# In[3]:

def get_grade_point(course_name):
    '''
    docstring for get_grade_point()
    
    Prompts the user for a grade point based on a course.
    '''
    print("Please enter the grade point for %s: " %(course_name))
    gp = float(input())
    return gp

print(help(get_grade_point))


# Now, everytime we want to read in information from the user about the grade point for a course, we can call `get_grade_point()` instead:

# In[5]:

# get grade point and credit hours for each class
gp1 = get_grade_point("computer science")
print("Please enter number of credits for your computer science course: ")
num_credits1 = int(input())

gp2 = get_grade_point("math")
print("Please enter number of credits for your math course: ")
num_credits2 = int(input())

gp3 = get_grade_point("karate")
print("Please enter number of credits for your karate course: ")
num_credits3 = int(input())

# compute the weighted credit hours earned
weighted_credits = (num_credits1 * gp1) + (num_credits2 * gp2) + (num_credits3 * gp3)

# compute the total number of credits earned
total_num_credits = num_credits1 + num_credits2 + num_credits3

# compute the average of the grade points
gpa = weighted_credits / total_num_credits

# display the results to the user
print("Your GPA is: %.2f" %(gpa))


# ### Let's write more functions for the other tasks in our program. Remember, 1 function = 1 task = 1 algorithm.

# In[2]:

def get_credits(course_name):
    '''
    Prompts the user for the number of credits for a course.
    '''
    print("Please enter the number of credits for %s: " %(course_name))
    num_credits = int(input())
    return num_credits

def compute_weighted_credits(gp1, gp2, gp3, num_credits1, num_credits2, num_credits3):
    '''
    Computes the weighted credits for three courses.
    '''
    weighted_credits = (num_credits1 * gp1) + (num_credits2 * gp2) + (num_credits3 * gp3)
    return weighted_credits

def sum_credits(credits1, credits2, credits3):
    '''
    
    '''
    total_credits = credits1 + credits2 + credits3
    return total_credits

def compute_gpa(weighted_credits, total_num_credits):
    '''
    Averages the weighted credits earned by the total number of credits taken.
    '''
    gpa = weighted_credits / total_num_credits
    return gpa

def display_gpa(gpa):
    '''
    Displays the final gpa to the user.
    '''
    print("Your GPA is: %.2f" %(gpa))


# And now, the new and improved program that utilizes functions:

# In[6]:

# get grade point and credit hours for each class
gp1 = get_grade_point("computer science")
num_credits1 = get_credits("computer science")

gp2 = get_grade_point("math")
num_credits2 = get_credits("math")

gp3 = get_grade_point("karate")
num_credits3 = get_credits("karate")

# compute the weighted credit hours earned
weighted_credits = compute_weighted_credits(gp1, gp2, gp3, num_credits1, num_credits2, num_credits3)

# compute the total number of credits earned
total_num_credits = sum_credits(num_credits1, num_credits2, num_credits3)

# copute the average of the grade points
gpa = compute_gpa(weighted_credits, total_num_credits)

# display the results to the user
display_gpa(gpa)


# #### Program Execution Revisited
# * Python executes code from top to bottom; however, read a program based on it's execution *flow*, not necessarily from top to bottom.
# * Function definitions do not alter the flow of program execution.
#     * When Python encounters a function definition, it notes the existence of the function, but does not execute the function
# * Statements in a function definition are not executed until the function is *called*. 
#     * Calling a function alters the top to bottom flow of program execution
# * Functions need to be defined *above* any code that calls the function.
# * When a function finishes executing, the next Python statement after the function call is executed.
# * Functions can call other functions!

# ## MA5 Practice Problem
# On a blank sheet of paper, write the following:
# 1. Your full name
# 1. Your TA name
# 1. MA #5
# 
# In pairs, work on the following problems. Each student needs to turn in their own paper to get credit for MA5.
# 1. Solve practice problems 2 and 3 from L3-2 without using functions.
# 1. Re-solve practice problems 2 and 3 from L3-2 using functions. Define functions for:
#     1. Getting user input
#     1. Computing results
#     1. Display the results

# ### TODO
# 1. PA1 is due Wednesday at midnight.
# 1. For extra practice, re-write the cone_volume.py code to be modular, meaning it uses functions. What would be a logical breakdown of the program into functions? Perhaps a `get_radius()`, `get_height()`, `compute_volume()`, and `display_volume()`.
# 
# ## Next Lesson
# More functions! Functions that return mutiple values, functions that call other functions, and more.
