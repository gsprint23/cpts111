
# coding: utf-8

# # [CptS 111 Introduction to Algorithmic Problem Solving](http://piazza.com/wsu/fall2016/cpts111/home)
# [Washington State University](https://wsu.edu)
# 
# 
# [Gina Sprint](http://eecs.wsu.edu/~gsprint/)
# # L3-2 Modules
# 
# Learner objectives for this lesson
# * Understand what a module is, how to import a module, and how to access identifiers contained within a module
# * Import the `math` module and utilize math-related variables and functions
# * Import and use the `turtle` module

# ## Python Modules
# A *module* is a file that contains a collection of related variables and functions. Python provides several modules for us programmers to use in our programs. In order to use the variables and functions within a module, we have to let Python know we want to use the module with an `import <name of module>` statement. 

# In[2]:

import math # math is a module containing... math functions!


# To access one of the variables or functions in a module, you type the module name (somewhere in the code *after* you import the module, remember Python executes code from top to bottom), followed by a dot, and then the name of the variable or function. For example, we can access an approximation of the mathematical constant `pi` ($\pi$) in the `math` module:

# In[6]:

print(math.pi)


# As another example, to access the square root function of the `math` module, use `math.sqrt()`:

# In[8]:

# don't forget the help() command to learn more about a function
print(help(math.sqrt))

print(math.sqrt(4))


# ## Math Functions
# 
# The Python math module defines numerous useful mathematical functions. This library is an excellent example of the power of functions: commonly-used mathematical operations are packaged up in functions that can be re-used over and over. We don't have to define these functions or know how they work, we can simply call the functions and use the return value(s). Examples of math functions available for our use include:
# * `fabs()` for absolute values
# * `ceil()` for computing the ceiling of a number
# * `floor()` for computing the floor of a number
# * `cos()` for cosine function
# * `sin()` for sine function
# * `tan()` for tangent function
# * `pow()` for raising a number to its power
# * `log()` for logarithms (see also `log2()` and `log10()`
# * `sqrt()` for computing square roots
# 
# Note: trig functions expect arguments in radians, not degrees. To convert degrees to radians, multiply by (`math.pi` / 180) or use the `radians()` function in the `math` module.
# 
# You can find out all the functions available within a module by importing the module, typing the module name and a dot, then pressing tab. This "auto-complete" feature is super helpful when learning a new library or when you can't remember the name of a function.

# In[3]:

x = -5
print("Absolute value of %d: %d" %(x, math.fabs(x)))

degrees = 45
rads = degrees * (math.pi / 180.0)
print("%d degrees in radians is %.2f" %(degrees, rads))
print("The sine of %d degrees is %.2f" %(degrees, math.sin(rads)))


# ## Turtle Graphics
# There are several Python modules available for doing graphical user interface (GUI) programming. For example, the `turtle` graphics library makes it really easy to draw pictures programmatically. We will return to `turtle` graphics later, but for now, check out how easy it is to draw:

# In[ ]:

import turtle

turt = turtle.Turtle()
turt.forward(100)
turtle.done()


# ![](https://raw.githubusercontent.com/gsprint23/cpts111/master/lessons/figures/turtle_simple.png)

# ## Example of Redundant Code: Average of 3 GPAs
# Problem Statement: Write a program that computes your grade point average after completion of 3 courses.
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
# Implementation:

# In[9]:

# get grade point and credit hours for each class
print("Please enter the gpa for your computer science course: ")
gpa1 = float(input())
print("Please enter number of credits for your computer science course: ")
num_credits1 = int(input())

print("Please enter the gpa for your math course: ")
gpa2 = float(input())
print("Please enter number of credits for your math course: ")
num_credits2 = int(input())

print("Please enter the gpa for your karate course: ")
gpa3 = float(input())
print("Please enter number of credits for your karate course: ")
num_credits3 = int(input())

# compute the weighted credit hours earned
weighted_credits = (num_credits1 * gpa1) + (num_credits2 * gpa2) + (num_credits3 * gpa3)

# compute the total number of credits earned
total_num_credits = num_credits1 + num_credits2 + num_credits3

# copute the average of the grade points
gpa = weighted_credits / total_num_credits

# display the results to the user
print("Your GPA is: %.2f" %(gpa))


# What do you think of this example? It seems redundant, right? We're using the exact same sequence of commands (`print()` and `input()`) to obtain the three grade points and credits. Is there a better (less redundant, easier to read, more concise) way to approach this problem? Enter: Functions!!

# ## TODO
# 1. Work on PA1, it is due Monday, September 12th at midnight.
# 1. Read Chapter 3 (Functions) in the textbook.
# 
# ## Next Lesson
# We will define our own functions!!
