
# coding: utf-8

# # [CptS 111 Introduction to Algorithmic Problem Solving](http://piazza.com/wsu/spring2017/cpts111/home)
# [Washington State University](https://wsu.edu)
# 
# [Gina Sprint](http://eecs.wsu.edu/~gsprint/)
# # L4-2 More Functions
# 
# Learner objectives for this lesson
# * Understand why functions are useful to use when designing programs and solving problems
# * Understand the execution flow of a program 
# * Recognize the scope of a name (identifier)

# ## Practice Problem
# 
# A commonly used method to provide a *rough* estimate of the right length of snowboard for a rider is to calculate 88 percent of their height. Write a program that will help people estimate the length of snowboard they should buy. Obtain the user's height in feet and inches (assume these values will be entered as integers) and display the length of snowboard in centimeters to the user. Note: There are 2.54 centimeters in an inch.
# 
# Define the following functions in your solution:
# 1. `get_user_height()`: Returns the user's total height in inches.
# 1. `convert_inches_to_centimeters(inches)`: Returns `inches` in centimeters.
# 1. `calculate_snowboard_length(height_inches)`: Returns the snowboard length estimate for a rider of `height_inches` height.
# 1. `display_snowboard_length(height_inches, snowboard_cm)`: Displays the snowboard length for a rider of `height_inches`.

# ## Why Use Functions?
# * Break a large, complex solution into logical units
#     * Individual members of a programming team can work on each unit independently
# * Procedural abstraction 
#     * The calling function need not be aware of the details of how a function works—just what it does
#     * Thus, during high-level problem solving activities, we won't get bogged down in detail
# * Reuse
#     * Recall our comment on the original version of the program to compute and display the gpa of classes
#         * Redundant: Much code was duplicated
#     * Why re-write sections of code that have already been written and tested?
#     * Functions allow us to package up a well-designed solution into a **bite-size chunk that can be reused over and over**
#         * Name a group of statements for easier reading and debugging
# * Testing
#     * Allows for more efficient testing and bug resolution
#     * Each function is tested as it is implemented

# ## Function Testing
# Each function is itself a small-scale "program" 
# * It has inputs
# * It has expected outputs or side-effects
# * Ideally, it is a self-contained "black box" (does not manipulate global variables)
# It makes sense to test each function independently
# * Correctness can be verified before it is used in a larger scale application
# A *test-driver* is a short program that tests a specific function

# ## How Functions are Executed
# * When a function is called, memory for local variables is allocated
# * Memory is released upon completion of function execution (local function variables do not "outlive" function)
# 
# Example: Recall the function `display_gpa()`:

# In[4]:

# function definition
def display_gpa(gpa):
    '''
    Displays the final gpa to the user.
    '''
    print("Your GPA is: %.2f" %(gpa))
    
# function call
display_gpa(3.4)


# In a function call such as `display_gpa(3.4)`, the value 3.4 is considered the argument of the function. When the function is executed, the value 3.4 is *copied* into a **new local variable**, `gpa`. We call `gpa` a local variable because the variable is only accessible within `display_gpa()` on this particular functional call (`display_gpa(3.4)`).
# 
# ## Scope
# **Scope of a name**: region of a program where a particular meaning of a name is visible or can be referenced.
# 
# ### Global Variables
# Variables declared outside of a function are considered *global*. In general, global variables are a [bad idea](http://c2.com/cgi/wiki?GlobalVariablesAreBad) and we try to avoid using them.
# 
# ### Local Variables
# Parameter variables and variables declared within a function are considered *local*. Local variables are only visible from within that function; once function is done, variables go away (space is deallocated). Consider the following example (which is an example used for scope purposes, not as an example of good program design!):

# In[3]:

max_val = 950

def one(anarg, second):
    '''
    
    '''
    one_local = 0

def fun_two(one, anarg):
    '''
    
    '''
    local_var = 0
    
def main():
    '''
    
    '''
    local_var = 0
    
one(0, 1) # function call #1
fun_two(5, 10) # function call #2
main() # function call #3
limit = 200


# When each of the above functions are executed from function calls #1-3, what is the scope of the following identifiers?
# 
# |Name|visible in `one()` when executed<br>from function call #1|visible in `fun_two()` when executed<br>from function call #2|visible in `main()` when executed<br>from function call #3|
# |----|------------------|----------------------|-------------------|
# |`max_val`|y|y|y|
# |`limit`|n|n|n|
# |`main`|y|y|y|
# |`local_var` (local variable in `main()`)|n|n|y|
# |`one` (function)|y|n|y|
# |`anarg` (parameter in `one()`)|y|n|n|
# |`second`|y|n|n|
# |`one_local`|y|n|n|
# |`fun_two`|y|y|y|
# |`one` (parameter in `fun_two()`)|n|y|n|
# |`anarg` (parameter in `fun_two()`)|n|y|n|
# |`local_var` (local variable in `fun_two()`)|n|y|n|

# ## Body-less Functions
# You can define a function without adding a body by simply placing the reserved keyword `pass` in the body. This can be useful when you want to test your program one function at a time or when you want to organize your program without actually writing the functions (or as a placeholder if someone else is writing the function). Example:

# In[3]:

def quadratic_root_finder(a, b, c):
    '''
    Applies the quadratic equation to find the roots of a quadratic function 
    specified by the formula ax^2 + bx + c = 0
    
    To efficiently be implemented by someone else!
    '''
    pass


# ## TODO
# 1. Read the functions chapters in the textbook.
# 1. Work on PA2
# 
# ## Next Lesson
# Debugging programs and function practice!
