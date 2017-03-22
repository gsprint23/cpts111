
# coding: utf-8

# # [CptS 111 Introduction to Algorithmic Problem Solving](http://piazza.com/wsu/spring2017/cpts111/home)
# [Washington State University](https://wsu.edu)
# 
# [Gina Sprint](http://eecs.wsu.edu/~gsprint/)
# # L10-2 Strings
# 
# Learner objectives for this lesson
# * Learn about string indexing
# * Iterate through characters in a string using loops
# * Learn about string slicing

# ## Review of Strings
# A long time ago, we learned a string is a *sequence of characters*. We learned how to use strings in print statements, how to assign a string to a variable, how to typecast to a string using `str()`.

# In[14]:

print("PYTHON")
my_string = "PYTHON"
print(my_string)
print("%s %s" %(my_string, str(100.0)))


# ### String Concatenation
# We also learned how to make new strings using string concatenation (the `+` operator): `new_string = old_string1 + old_string2`:

# In[7]:

new_string = "cpts" + "111" + " uses " + my_string + "!"
print(new_string)


# ### Strings and `for` Loops
# More recently, we learned about sequences in the context of `for` loops:
# 
# ```for <item> in <sequence>:
#     <body>
# ```
# 
# We can also use `for` loops to iterate through each character in a string:

# In[8]:

for character in "PYTHON":
    print(character, end=" ")


# We can do this because the string "PYTHON" is a sequence of characters, where the first character ("P") is the located at the first index, index 0. This is called 0-based indexing.

# ## String Indexing
# Logically, the string `"PYTHON"` is organized as follows:
# 
# |Index:|0|1|2|3|4|5|
# |-|-|-|-|-|-|-|
# |Character:|P|Y|T|H|O|N|
# 
# In general, a string that has `n` characters has valid indices of 0, 1, ..., `n` - 1.
# 
# We can access a single character in the string using indexing notation: `[<index>]` (hard brackets):

# In[9]:

my_string = "PYTHON"

print(my_string[0])
print(my_string[5])


# What happens if we try to index beyond `n` - 1?

# In[10]:

print(my_string[6])


# Your program will crash! Python will tell you why though: "IndexError: string index out of range".
# 
# We can also index into a string to get single characters by using a variable:

# In[6]:

i = 2
print(my_string[i])
print(my_string[i - 1])


# ## String Length
# We can find out the length of a string, meaning the number of characters in the string, by calling the built-in string `len(<string>)` function:

# In[3]:

length = len(my_string)
print("The length of %s is: %d" %(my_string, length))


# Note: `len()` can also be useful for determining the valid index range of a string (length of the string - 1):

# In[5]:

str_len = len(my_string)
print(my_string[str_len - 1])


# ### The Empty String
# We can have an empty string (`""`), a string with no characters.

# In[2]:

empty_string = ""
print(empty_string, end="")


# ## Strings and `while` Loops
# Now, we can use a `while` loop and the built-in `len()` function to display individual characters of a string, similar to how we used a `for` loop above. Our loop control variable wil be a variable (`i`) used to index into the string: 

# In[11]:

i = 0

while i < len(my_string):
    print(my_string[i], end=" ")
    i += 1


# Using the `len()` function. We do not need to know in advance how many characters are in `my_string` to walk through each character and print it. 

# ## String Slicing
# We can use the `:` operator to select a *slice* of a string: `<string variable>[start_index:end_index + 1]`
# 
# For example:

# In[6]:

# Get the YT of PYTHON
print(my_string[1:3])

course = "CptS111"

# get a slice of the 111
course_num = course[4:7]
print(course_num)


# Omitting the start index implies a 0 for a start index and omitting an end index implies a `len(<string variable>)` for an end index:

# In[8]:

# these two are the same
print(my_string[0:2])
print(my_string[:2])

# these two are the same
print(my_string[2:len(my_string)])
print(my_string[2:])


# Note: We can also use negative indices! The last index of a string is -1, the second to last index is -2, and so on, until the first index is `-len(<string variable>)`
# 
# |Index:|0|1|2|3|4|5|
# |-|-|-|-|-|-|-|
# |Character:|P|Y|T|H|O|N|
# |Index:|-6|-5|-4|-3|-2|-1|

# In[10]:

print(my_string[-1])
print(my_string[-6])


# ## Immutability of Strings
# Strings are *immutable*, meaning they can't be changed. This means we cannot re-assign a character of a string:

# In[12]:

# crashes because strings are immutable
my_string[0] = "p"


# To "change" a string (remember strings are immutable), we can make a new string that is a variant of the old string:

# In[13]:

new_string = "p" + my_string[1:]
print(new_string)


# ## Practice Problem

# In[2]:

holiday = "easter"


# Given the above string declaration, answer the following questions:
# 1. What are the valid indices of `holiday`?
# 1. Write code to print the number of characters in `holiday`
# 1. Write code to print the "a"
# 1. Write code to print "ter"
# 1. Write code to assign "easter is April 16th" to a new string using `holiday`
# 1. Write code to assign "Easter" to a new string using `holiday`

# ## TODO
# 1. Read Chapter 8 and Chapter 9
# 1. Work on PA5
# 
# ## Next Lesson
# 1. More about Strings
# 1. String methods
