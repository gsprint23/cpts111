
# coding: utf-8

# # [CptS 111 Introduction to Algorithmic Problem Solving](http://piazza.com/wsu/spring2017/cpts111/home)
# [Washington State University](https://wsu.edu)
# 
# [Gina Sprint](http://eecs.wsu.edu/~gsprint/)
# # L12-2 Lists
# 
# Learner objectives for this lesson
# * Understand what a list is
# * Declare lists
# * Apply list indexing, slicing, concatenation, and repetition
# * Apply list iteration techniques

# ## Review of Strings
# Recall a string is a *sequence of characters*. In Python, we can have sequences of items other than characters. For example, we can have sequences of:
# * Numbers
#     * Integers
#     * Floats
# * Objects
#     * Strings
#     * Files
#     * Turtles
#     * Our own objects we define ourselves (to be learned later, stay tuned!)

# ## Lists
# A list is a *sequence of items*. In a string, the items are characters. In a list, they can be any type. Items in a list are also called *elements*.
# 
# We declare a sequence of items as a list with hard brackets: `[<comma separated list items>]`

# In[3]:

list_ints = [0, 1, 10, 20]
print(list_ints)

list_floats = [0.2, 0.4, 0.6, 1.0]
print(list_floats)

# types can be mixed in a list
list_numbers = [0, 0.0, 1, 1.0, -2]
print(list_numbers)

list_strings = ["cat", "dog", "bird"]
print(list_strings)


# Note: the data types in a list need not all be the same.
# 
# ### List Indexing
# Just like with strings, list indices are 0-based. We can index into a list to access a list item just like how we indexed into a string to get an individual character:

# In[4]:

print(list_ints[0])


# ### List Length
# We can also use then `len()` function to determine the number of items in a list:

# In[5]:

print(len(list_strings))
print(list_strings[len(list_strings) - 1])


# ### The Empty List
# Just like how we can have an empty string (`""`), a string with no characters, we can have an empty list (`[]`). An empty list has no items.

# In[10]:

empty_list = []
print(len(empty_list))


# ### Nested Lists
# We can have lists of lists!

# In[4]:

nested_list = [[0, 1], [2], [3], [4, 5], []]
print(nested_list)


# Note: the sub-lists can be of unequal lengths.
# 
# Now, consider the following nested list:
# 
# `matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]`
# 
# Logically, `matrix` looks like the following:
# 
# |Column Index:||||
# |-|-|-|-|
# ||**0**|**1**|**2**|
# |**Row Index**||||
# |**0:**|1|2|3|
# |**1:**|4|5|6|
# |**2:**|7|8|9|
# 
# To access an item in a 2-dimensional nested list, we index into the `<nested list variable>` twice: `<nested list variable>[row_index][column_index]` by row first then column. For example: 

# In[6]:

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)
# the first element in the first list
print(matrix[0][0])
# the last element in the last list
print(matrix[2][2])
# the middle element in the last list (8)
print(matrix[2][1])


# ### Lists are Mutable
# Unlike strings, we can change the items in a list:

# In[8]:

buildings = ["Sloan", "EME", "Dana", "ETRL"]
print(buildings)

# modify the list
buildings[2] = "Carpenter"
print(buildings)


# Note: We still cannot change a string. Strings are immutable!

# ## Looping Through List Items
# Just like with strings, we can use the `in` operator or indices to iterate through items in a list:

# In[6]:

candies = ["twix", "reeses", "oreos", "snickers"]

for candy in candies:
    print(candy)
    
i = 0
while i < len(candies):
    print(candies[i])
    i += 1
    
i = 0
for i in range(len(candies)):
    print(candies[i])


# ## List Operators
# ### List Concatenation
# Just like with strings, we can use the concatenation `+` operator to add lists together:

# In[23]:

candies = ["twix", "reeses", "oreos", "peach rings"]

print(candies)
candies += ["m&ms", "starburst"]
print(candies)


# ### List Repetition
# Just like with strings, we can repeat items in a list with the repetition `*` operator:

# In[24]:

bag_o_candies = 5 * ["twix"]
print(bag_o_candies)

bag_o_candies += 3 * ["peach rings"]
print(bag_o_candies)


# ### List Slicing
# Just like with strings, we can use the slice operator `:` with lists:

# In[8]:

print(candies[1:3])
# returns a copy
print(candies[:])


# However, since lists are mutable, we can now change multiple items in a list at a time using slices:

# In[22]:

candies = ["twix", "reeses", "oreos", "peach rings"]
print(candies)
candies[3:] = ["butterfinger", "heath", "swedish fish"]
print(candies)
candies[0:2] = ["carmello", "airheads"]
print(candies)


# ## Tuples
# Tuples are immutable lists. They are declared as a comma separated list, with or without parentheses:

# In[2]:

my_tuple = "x", "y", "z"
print(my_tuple)
print(type(my_tuple))

# need a comma after a single element initialization
my_tuple2 = (1, )
print(my_tuple2)

# need a comma after a single element initialization
not_a_tuple = ("a")
print(not_a_tuple)
print(type(not_a_tuple))

# creating an empty tuple
empty_tuple = tuple()
print(empty_tuple)
print(type(empty_tuple))


# Tuple indexing and slicing works the same as for lists:

# In[3]:

my_tuple = ("x", "y", "z")
print(my_tuple[1])
print(my_tuple[0:2])


# HOWEVER, tuples are immutable, so you cannot modify them. The follow code demonstrates the immutability of tuples:

# In[4]:

my_tuple = ("x", "y", "z")
# crashes! tuples are immutable, you cannot change them
my_tuple[2] = "a"


# ## TODO
# 1. Take a look at PA6, it is posted!
# 1. Read Chapter 11 in zyBooks and Chapter 10 in the optional textbook.
# 
# ## Next Lesson
# 1. List methods
# 1. Deleting items in a list
# 1. Other list goodies!
