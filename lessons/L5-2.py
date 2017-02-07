
# coding: utf-8

# # [CptS 111 Introduction to Algorithmic Problem Solving](http://piazza.com/wsu/spring2017/cpts111/home)
# [Washington State University](https://wsu.edu)
# 
# [Gina Sprint](http://eecs.wsu.edu/~gsprint/)
# # L5-2 If Statements
# 
# Learner objectives for this lesson
# * Understand what a Boolean condition is
# * Apply relational operators (<, >, <=, >=, ==, !=)
# * Apply logical operators (and, or, not)
# * Apply Boolean types
# * Define and call predicate functions
# * Understand `if` statements

# Algorithms are composed of three different kinds of statements:
# 1. Sequence: the ability to execute a series of instructions, one after the other.
# 1. Conditional: the ability to execute an instruction contingent upon some condition.
# 1. Iteration: the ability to execute one or more instructions repeatedly.
# 
# If statements are conditionals: the ability to **execute some code IF some condition is true**. 
# 
# ## Boolean Conditions
# Conditional statements rely on a Boolean condition, which evaluates to either true or false
# In Python, the true and false values are actually represented by the reserved keywords `True` and `False`. Numerical values also have a "True" and "False" meaning:
# * False: 0
# * True: any number except 0 (usually 1)
# 
# ### Relational Operators
# Relational operators are used to build Boolean conditions:
# * < (less than)
# * \> (greater than)
# * <= (less than or equal to)
# * \>= (greater than or equal to)
# * == (equal to)
# * != (not equal to)

# In[2]:

x = 3
y = 4
max_val = 100
min_val = 0

print(x <= 0)
print(x == y)
print(max_val >= min_val)
print(max_val != False)
print(max_val) # since this is 100, which is not 0, this is essential "True"
print(min_val != 0)
print(max_val == 99 + 1)
print(min_val - 50 < 0)


# ### Logical Operators
# We can combine relational operators with logical operators to construct general Boolean expressions in Python:
# * `and`
# * `or`
# * `not`
# 
# Truth table
# 
# |P|Q|not P|P and Q|P or Q|
# |-|-|-|-|-|
# |0|0|1|0|0|
# |0|1|1|0|1|
# |1|0|0|0|1|
# |1|1|0|1|1|
# 

# In[3]:

temp = 50
max_temp = 90
precip = 2.0
num_votes = 20
votes_needed = 20
elected = 0

print((temp < max_temp) and (precip > 0))
print((num_votes >= votes_needed or (not elected)))


# ### Operator Precedence
# Just like numeric operators (+, -, /, //, %, \*), logical operators have precedence rules that determine order of evaluation
# From highest to lowest, the precedences are as follows: 
# [Most are left-to-right; but not exponentiation and assignment]
# 
# |Operator|Precedence|
# |--------------|---------|
# |() (parentheses)|(highest)|
# |function calls||
# |**||
# |+, - (unary operators)||
# |\*, /, //, %||
# |+, -||
# |**<, <=, >=, >**, **==, !=**||
# |**not**||
# |**and**||
# |**or**||
# |= (assignment)|(lowest)|
# 
# An example: 

# In[4]:

flag = 0
y = 4.0
z = 2.0
x = 3.0

print(not flag or (y + z >= x - z))


# ### Short Circuit Evaluation
# Notice that, in case of `and`, if the first part of expression is false, the entire expression must be false
# * Example: `(5 < 3) and (4 > 3)`
# 
# Likewise, in case of `or`, if the first part of expression is true, the entire expression must be true
# * Example: `(4 > 2) or (2 > 3)`
# 
# In these two cases, Python short-circuits evaluation: Evaluation stops after first part of expression is evaluated
# 
# ### Complement (`not`)
# The complement of a condition can be obtained by applying the `not` operator
# * Example: The complement of `temp > 32` is `not (temp > 32)`, which can also be written as `temp <= 32`
# * Example: The complement of `temp == 32` is `not (temp == 32)`, which can also be written as `(temp != 32)`
# 
# Apply **DeMorgan's Laws** to complement compound logical expressions:
# * Complement of `X and Y` is `not X or not Y`
# * Complement of `X or Y` is `not X and not Y`
# 
# Example: `(temp > 32) and (num_clouds == 0 or num_clouds == 1)` is true when the temperature is above freezing and the number of clouds in the sky is 0 or 1. By applying DeMorgan's Laws, the complement of this statement is:
# `(temp <= 32) or (num_clouds != 0 and num_clouds != 1)` which is true when the temperature is at or below freezing, and there are more than 1 cloud in the sky.
# 

# ## Logical Assignment
# In addition to integers, floats, and strings, there is a data type called `Boolean`. We can store `True` or `False` in a Boolean type:

# In[2]:

boolean_condition = True
print("%s %d" %(boolean_condition, boolean_condition))


# ## `if` Statements
# Algorithms are composed of three different kinds of statements:
# 1. Sequence: the ability to execute a series of instructions, one after the other.
# 1. Conditional: the ability to execute an instruction contingent upon some condition.
# 1. Iteration: the ability to execute one or more instructions repeatedly.
# 
# If statements are conditionals: the ability to **execute some code IF some condition is true**. 
#  
# The if statement supports conditional execution in Python:
# ```
# if <test>:
#     <body>
# ```
# 
# `<test>` must be an expression that can be evaluated to either `True` or `False` (non-zero or zero), i.e. `<test>` is a **Boolean condition**
# `<body>` is one or more Python statements that are **indented** 4 spaces (or one tab, depending on your text editor)

# In[1]:

x = 5

if x == 5:
    print("x is 5!!")
    
if x == 7:
    print("x is 7!!")


# Python also defines an `if`-`else` statement:
# ```
# if <test>:
#     <body-if-test-is-true>
# else:
#     <body-if-test-is-false>
# ```
# 
# **Only one of the two `<body>` blocks can be executed each time through this code**. In other words, they are "mutually exclusive".
# 
# Note: the `else` has no `<test>` condition. The `else` body executes when the complement of `<test>` is True (i.e. `<test>` is False).

# In[2]:

temperature = 10

if temperature > 32:
    print("It is warm out!")
else: # temperature <= 32
    print("Brrrrr...")


# In[3]:

x = y = z = 0
y = y + 4
z = z * x

if z > y:  
    print("Z: %d" %(z + 1))
else: # z <= y
    print("X: %d" %(x - 1))


# ## Predicate Functions
# We can also write functions that return Booleans. Such a function is called a *predicate function*. For example, consider the following function that accepts a number as an argument and returns true or false based on whether or not the value is even:

# In[14]:

def is_even(x):
    '''
    
    '''
    return x % 2 == 0

print(is_even(7))


# Let's rewrite `is_even()` to use `if-else` statements:

# In[4]:

def is_even(x):
    '''
    
    '''
    flag = False
    if x % 2 == 0:
        # only sets flag to True when x is even
        flag = True
    return flag

def is_even_revised(x):
    '''
    This function does not use a flag, instead it has multiple return statements
    '''
    if x % 2 == 0:
        return True
    else:
        return False
    
print(is_even(5))
print(is_even_revised(5))
print(is_even(8))
print(is_even_revised(8))


# ## Common Mistakes with `if` Statements
# * Using = (assignment) instead of == (logical equality) 
# * Using if-else when if-if should be used
#     * Remember else does not have an explicit condition associated with it
# * Using logical `and` instead of logical `or` and vice versa

# ## TODO
# 1. Finish PA2!
# 1. Read about conditionals in How to Think Like a Computer Scientist.
# ## Next Lesson
# 1. Multiple alternative `if` statements and nested `if` statements.
