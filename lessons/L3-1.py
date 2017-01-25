
# coding: utf-8

# # [CptS 111 Introduction to Algorithmic Problem Solving](http://piazza.com/wsu/spring2017/cpts111/home)
# [Washington State University](https://wsu.edu)
# 
# [Gina Sprint](http://eecs.wsu.edu/~gsprint/)
# # L3-1 Errors and Practice
# 
# Learner objectives for this lesson
# * Learn about programming erros
# * Practice arithmetic in Python

# ## Programming Errors
# Rarely will you write a program that is free of errors. You'll need to diagnose and correct three kinds of errors:
# 1. Syntax errors (code violates syntax rules for a proper Python program)
#     * Detected at compile time
#     * Program will not run unless they're corrected
#     * Examples
#         * Undeclared identifiers
#         * Invalid identifiers (e.g. a space in a variable name)
#         * Failure to close a comment or string properly
#         * Incorrect indenting (we will learn about indenting when we learn about functions)
# 2. Run-time errors
#     * Cause the program to "crash": an error is reported, and control is turned over to the operating system
#     * Examples
#         * Division by zero
#         * Getting into an infinite loop, which may ultimately cause a "stack overflow"
# 3. Logic Errors
#     * Cause the program to compute incorrect results
#     * Often go unnoticed, at least at first
#     * Examples
#         * Your algorithm is wrong because you misunderstand the problem
#         * You do not obtain input data properly, so your computations work on the wrong data.

# ## MA3 Practice Problems
# On a blank sheet of paper, write the following:
# 1. Your full name
# 1. Your TA name (or lab time if you don't know your TA name)
# 1. MA #3
# 
# In pairs, work on the following problems. Each student needs to turn in their own paper to get credit for MA3.
# 
# 1. Label each of the following as either "Python reserved keyword", "standard identifier", or "other valid identifier":
#     1. `int`: standard
#     1. `PI`: other
#     1. `if`: reserved keyword
#     1. `main`: other
#     1. `while`: reserved keyword
#     1. `high_score`: other
# 1. How should you read the statement: `temp_value = old_value + new_value`? "temp_value **is assigned** old_value plus new_value"
# 1. Which Python data type would be best to represent the following? For each blank, you may list `int`, `float`, or `str` only.
#     1. Gender: `str`
#     1. Average of 10 numbers: `float`
#     1. Number of students in CptS111: `int`
#     1. Price of a gallon of milk: `float`

# ## TODO
# 1. Practice floating point division, integer division, and mod!
# 2. Work on PA1.
# 
# ## Next Lesson
# We will practice more with arithmetic and learn about modules.
