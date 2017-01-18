
# coding: utf-8

# # [CptS 111 Introduction to Algorithmic Problem Solving](http://piazza.com/wsu/spring2017/cpts111/home)
# [Washington State University](https://wsu.edu)
# 
# [Gina Sprint](http://eecs.wsu.edu/~gsprint/)
# # L2-2 Arithmetic
# 
# Learner objectives for this lesson
# * Apply arithmetic operators in multiple operator expressions
# * Understand type conversion
# * Apply the parentheses and operator precedence when evaluating multiple operator expressions
# * Understand the difference between `int()` and `round()`
# * Use `print()` to format floating point numbers

# ## Arithmetic Expressions
# Most programming problems require arithmetic expressions as part of solution; including problems related to:
# * Mechanics
# * Kinematics
# * Materials science
# * Electronics
# * Many others
# 
# Form: `operand1 operator operand2`
# * i.e. `x + y`
# 
# Note: the type of result dependent on operand types
# 
# ### Arithmetic Operators in Python
# |Operator|Representation|Example|
# |----------|-----|-----|
# |+|Addition|10 + 5 = 15|
# |||1.55 + 13.3 = 14.85|
# |||3 + 100.7 = 103.7|
# |-|Subtraction|10 - 5 = 5|
# |||5.0 - 10.0 = -5.0|
# |||10 - 5.0 = 5.0|
# |\*|Multiplication|1 * 5 = 5|
# |||1.000 * 10.0 = 10.0|
# |||5 * 5.0 = 25.0|
# |/|Floating Point Division|2 / 3 = 0.66|
# |||10.0 / 4.0 = 2.5|
# |||10 / 3.0 = 3.33|
# |//|Integer Division|2 // 3 = 0|
# |||10.0 // 4.0 = 2.0|
# |||10 // 3.0 = 3.0|
# |%|Modulus (AKA Remainder)|5 % 2 = 1|
# |||2 % 5 = 2|
# |||6 % 0 = undefined|
# |||6.0 % 3 = 0.0|
# |\*\*|Exponentiation|2 \*\* 3 = 8|
# |||2 \*\* 3 \*\* 2 = 512|
# |||4 \*\* (2 / 4) = 2.0|
# 
# Note: The result of a modulus operation is the same as the remainder from integer division. Remember long division?
# ![](https://raw.githubusercontent.com/gsprint23/cpts111/master/lessons/figures/long_division.gif)
# (Image from https://dj1hlxw0wr920.cloudfront.net/userfiles/wyzfiles/b410fcc6-7a7b-45a0-81b9-354423866db9.gif)
# 
# In the above example, 128 // 5 is 25 and 128 % 5 is 3 (the remainder).
# 
# Note: Exponentiation groups from right to left.

# In[1]:

print(2 ** 3 ** 2) # move from right to left for exponentiation
print(4 ** 2 / 4) # exponentiation has higher precedence than division
print(4 ** (2 / 4)) # square root


# ### Mixed-Type Expressions
# An expression with different *types of operands* (e.g. an integer value and a double value).
# 
# The result is always the more precise data type. For example:
# 
# 10 (an `int`) + 25.5 (a `float`) = 35.5 (a `float`)
# 
# ### Mixed-Type Assignment Statements
# * Evaluated from right-to-left
# * Expression is first evaluated (what's on the right hand side) and then assigned to variable (what's on left hand side)
# 
# Examples:

# In[2]:

result = 0
op1_int = 5
op2_int = 42
op1_float = 5.5

# integer expression, integer assignment, result = 47
result = op1_int + op2_int
print(result, type(result))

# mixed expression, float assignment result = 10.5
result = op1_int + op1_float;
print(result, type(result))

# mixed expression, integer assignment, result = 10 (truncation occurs)
result = int(op1_int + op1_float)
print(result, type(result))


# ## Changing Type
# We have already seen type conversions to change a value of certain a data type into another data type
# 
# Two kinds of type conversions (also called casts) exist:
# 1. Implicit
# 1. Explicit
# 
# Implicit type conversion example:

# In[3]:

num1 = 12 # int
num2 = 0.0 # float
num2 = num1 # num2 is now an int
print(num2, type(num2))


# Explicit type conversion example:

# In[4]:

num1 = 1.7 # float
num1 = int(num1) # 1.7 explicitly casted to type int, 1
print(num1, type(num1))


# Note: `int()` truncates the fractional part of a floating point number. If you want to round the float instead, use `round()`. `round()` allows you to round a float to as many decimal places as you like: `round(<float>, n)` where `n` = number of decimal places. If you omit `n`, then `round(<float>)` returns a rounded integer:

# In[5]:

x = 5.87
print(int(x)) # truncates
print(round(x)) # rounds to nearest integer
print(round(x, 1)) # rounds to one decimal place


# ## Multiple Operator Expressions
# Arithmetic expressions in Python can have multiple operators. We saw this in our volume of a cone example.
# * May contain unary and binary operators
# * Unary operators consists of one operand
# * Binary operators require two operands
# 
# Example:

# In[6]:

x = 5
# -x applies the unary sign operator for negation
y = -x + x * x / 10 # what is this result? run the code to check your result
print(y)


# ## Operator Precedence
# How is `x – y / z` evaluated?
# 1. `(x – y) / z` ?
# 1. `x – (y / z)` ?
# 
# It is important to understand operator precedence rules:
# * Subexpressions in parentheses are evaluated first
# * Evaluation proceeds left to right
# * In cases where no parentheses are used, \*, /, //,and % take precedence over + and –
# 
# So `x – y / z` is evaluated as `x – (y / z)`, because / takes precedence over –
# 
# Note: The unary operators + and – are used to indicate the sign of a number (e.g., +5, -3.0). They take precedence over all binary operators, and are evaluated right to left.
# 
# Example: `-3 + 5 * 4` would be evaluated as `(-3) + (5 * 4) = 17`.
# Recommendation: Liberally use parentheses to avoid confusion and unexpected results!
# 
# Here is another precedence example (from Hanly and Koffman, page 80):
# ![](https://raw.githubusercontent.com/gsprint23/cpts111/master/lessons/figures/precedence_example.png)
# 
# ## Formatting Numbers
# Python defines "default" output style for each data type
# * No leading blanks for `int` and `float`
# * `float` displayed with digits to right of decimal point
# 
# You can override these defaults by specifying custom format strings to `print()` function. For float output, format string is of form `%n.mf`, where `n` is total width (number of columns) of formatted number, and `m` is the number of digits to the right of decimal point to display. It is possible to omit `n`. In that case, no leading spaces are printed. `m` can still specify the number of decimal places (e.g., `%.2f`).
# 

# In[7]:

x = 3
y = 2.17
# outputs 2 spaces before the 3 and 2 spaces before the 2.2
print("x is%3d. y is%5.1f." %(x, y))


# You try it! Consider the following variables:
# ```
# a = 504
# b = 302.558
# c = -12.31
# ```
# Write a Python statement that will display the following line (@ is used to denote a blank):
# @@504@@@@@302.56@@@@-12.3

# In[8]:

a = 504
b = 302.558
c = -12.31
print("%5d%11.2f%9.1f" %(a, b, c))


# ## TODO
# 1. Get started on PA1.
# 1. Bring your laptop to next class, we will be working *lots* of problems.
# 
# ## Next Lesson
# Practice, practice, practice.
