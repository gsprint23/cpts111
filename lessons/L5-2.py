
# coding: utf-8

# # [CptS 111 Introduction to Algorithmic Problem Solving](http://piazza.com/wsu/fall2016/cpts111/home)
# [Washington State University](https://wsu.edu)
# 
# [Gina Sprint](http://eecs.wsu.edu/~gsprint/)
# # L5-2 Boolean Conditions
# 
# Learner objectives for this lesson
# * Understand what a Boolean condition is
# * Apply relational operators (<, >, <=, >=, ==, !=)
# * Apply logical operators (and, or, not)
# * Apply Boolean types
# * Define and call predicate functions

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

# ### Short Circuit Evaluation
# Notice that, in case of `and`, if the first part of expression is false, the entire expression must be false
# * Example: `(5 < 3) and (4 > 3)`
# Likewise, in case of `or`, if the first part of expression is true, the entire expression must be true
# * Example: `(4 > 2) or (2 > 3)`
# In these two cases, Python short-circuits evaluation: Evaluation stops after first part of expression is evaluated
# 
# ## Logical Assignment
# In addition to integers, floats, and strings, there is a data type called `Boolean`. We can store `True` or `False` in a Boolean type:

# In[9]:

branching_condition = True
print("%s %d" %(is_true, is_true))


# ## Predicate Functions
# We can also write functions that return Booleans. Such a function is called a *predicate function*. For example, consider the following function that accepts a number as an argument and returns true or false based on whether or not the value is even:

# In[14]:

def is_even(x):
    '''
    
    '''
    return x % 2 == 0

print(is_even(7))


# ## TODO
# 1. Finish PA2! It is due Monday at midnight.
# 1. Read chapter 5 in Downey. Ignore the sections about recursion, we are not going to cover recursion in this class.
# 
# ## Next Lesson
# 1. We learn about `if` statements, it will be fun!
