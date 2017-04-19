
# coding: utf-8

# # [CptS 111 Introduction to Algorithmic Problem Solving](http://piazza.com/wsu/spring2017/cpts111/home)
# [Washington State University](https://wsu.edu)
# 
# [Gina Sprint](http://eecs.wsu.edu/~gsprint/)
# # L14-2 Dictionaries
# 
# Learner objectives for this lesson
# * Understand key-value pairs
# * Understand dictionaries
# * Declare, access, and manipulate dictionaries

# ## Practice Problems
# ### Problem \#1
# Adapted from Downey exercise 10.1. Write a function called `nested_sum()` that takes a list of lists of numbers and adds up the elements from all of the nested lists. For example, `nested_sum([[1, 2], [3], [4, 5, 6]])` returns 21.

# In[ ]:




# ### Problem \# 2
# Write a function called `split_the_list()` that accepts a list of numbers and returns a list of two lists. The first list in the return list is the first half of the list argument. The second list is the second half of the list argument.

# In[ ]:




# Lists are a type of *data structure*, they organize primitive data (like numbers) into a linear structure. Data structures are super important in computer science. Different types of problems require different types of data structures in order to implement a solution.
# 
# Today we are going to learn about dictionaries and see examples of the types of problems/solutions that are suited for dictionaries.
# 
# ## Key-Value Pairs
# Consider the following set of items:
# * Your student ID number
# * Your checking account number
# * The VIN number on your car
# * Your social security number
# 
# What do all of the above items have in common? They are all *unique* identifiers for something. For example, there may be several students named "John Smith" at WSU. How is the university to distinguish academic records for multiple John Smiths? They assign a unique *key* to identify each individual student:
# 
# |ID Number|Last name|First name|
# |-|-|-|
# |28905|Smith|Jane|
# |19485|Smith|John|
# |28450|Smith|John|
# |25543|Smith|John|
# |17834|Smith|Justin|
# 
# For the other examples, your checking account number is a key that uniquely identifies your account, the VIN is a key that uniquely identifies your car, and your SSN is a key that uniquely identifies you for government purposes.
# 
# Keys are useful because they *map* keys to values. In the example above, a student ID number of 28905 maps to the academic records of Jane Smith at WSU. The academic record of Jane Smith is called the *value* that the *key* (ID number) maps to. Together, the ID number (28905) and the record (Jane Smith's academic record) form a *key-value pair*. 
# 
# Keys can be represented as a list of unique values (no duplicates). Values can be represented as a list as well (can have duplicates). A single data structure that combines key lists and value lists is called a *dictionary*.
# 
# ## Dictionaries
# A *dictionary is a list with keys as indices*. Keys can be integers, strings, file objects, etc. Keys cannot be lists. To declare a dictionary, we use the curly braces `{ }`:

# In[1]:

# declares an empty dictionary
my_dict = {}
print(my_dict)
# can also use dict()
my_second_dict = dict()
print(my_second_dict)


# We can initialize a dictionary with values using comma separated `key:value` pairs:

# In[2]:

state_capitals = {'washington': 'olympia', 'idaho': 'boise', 'oregon': 'portland'}
print(state_capitals)


# We can create a dictionary from a list of tuples, where each tuple in the list is a key-value pair:

# In[4]:

# roman numerals
key_values = [("I", 1), ("V", 5), ("X", 10), ("L", 50)]
roman_numerals = dict(key_values)
print(roman_numerals)


# We can also convert a dictionary back to a list of tuples with the dictionary method `items()` and the built-in function `list()`:

# In[6]:

list_of_tuples = list(roman_numerals.items())
print(list_of_tuples)


# ### Compatible Dictionary Data Types
# #### Keys
# Dictionary keys can be integers, strings, files, tuples, etc.. Lists cannot be keys.
# 
# #### Values
# Values can be any type. For example, we can have string keys and list values:

# In[8]:

fruit_colors = {'kiwi': ['brown', 'green'], 'banana': ['yellow'], 'watermelon': ['green', 'red']}
print(fruit_colors)


# ### Dictionary Indexing
# We can access an item via a key using hard brackets `[ ]` (similar to indexing into a list):

# In[4]:

state_capitals = {'washington': 'olympia', 'idaho': 'boise', 'oregon': 'portland'}
print("The capital of idaho is %s" %(state_capitals['idaho']))


# ### Adding Key-Value Pairs
# Since dictionaries are *mutable*, we can add key-value pairs to the dictionary using hard brackets `[ ]`:

# In[5]:

state_capitals = {'washington': 'olympia', 'idaho': 'boise', 'oregon': 'portland'}
print(state_capitals)

state_capitals['montana'] = 'helena'
print(state_capitals)


# Note: keys in a dictionary are not sorted in any particular order.
# 
# ### Dictionary Length with `len()`
# We can still determine the number of items (key-value pairs) in a dictionary with `len()`:

# In[6]:

state_capitals = {'washington': 'olympia', 'idaho': 'boise', 'oregon': 'portland'}
print(len(state_capitals))


# ### Existence of a Key
# We can also test if a key is a valid key in the dictionary with the `in` keyword:

# In[10]:

state_capitals = {'washington': 'olympia', 'idaho': 'boise', 'oregon': 'portland'}

print('california' in state_capitals)
print('idaho' in state_capitals)
print('olympia' in state_capitals)


# ## Looping through a Dictionary
# We can traverse a dictionary easily with a `for` loop that walks through each key in the dictionary:

# In[8]:

sides = {'square': 4, 'triangle': 3, 'pentagon': 5, 'rectangle': 4}

for side in sides:
    print(side, sides[side], sep= ": ")


# ## Example Problem: Letter Frequencies
# Suppose we want to keep track of the frequency of letters in a word. For example, the word "hello" has 4 letters with the following frequencies:
# * h: 1
# * e: 1
# * l: 2
# * o: 1
# 
# Let's write a program to prompt the user to enter a word. Our program will tell the user the frequency of each letter in the word. We could solve this problem with either a list or a dictionary:
# * List solution
#     1. Create a list with 26 zeros
#     1. Write a function to convert a letter into an integer in the range [0-25] to index into the list. We can do this with the `ord(<character>)` function and ASCII codes...
#     1. Walk through the word and increment the corresponding list position for each letter
#     1. Convert the index of non-zero list entries back to characters using `char(<integer>)` to print out the histogram results
# * Dictionary solution
#     1. Create an empty dictionary
#     1. Walk through the word and add the letter to the dictionary with a count of zero if the letter is not already a key, increment otherwise.
#     
# The dictionary solution lends itself more suitable to this problem because we do not have to allocate space for all letters ahead of time and we don't have to perform a character to integer conversion to index into the data structure.

# In[7]:

def compute_letter_frequencies(word):
    '''
    
    '''
    histogram = {}
    
    for letter in word:
        if letter in histogram:
            histogram[letter] += 1
        else:
            histogram[letter] = 1
    return histogram

print(compute_letter_frequencies("hello"))
print(compute_letter_frequencies("mississippi"))


# Compared to the list solution:

# In[8]:

def letter_to_index(letter):
    '''
    
    '''
    ascii_val = ord(letter)
    index = ascii_val - ord('a')
    return index

def index_to_letter(index):
    '''
    
    '''
    ascii_val = index + ord('a')
    letter = chr(ascii_val)
    return letter
    
def compute_letter_frequencies_list(word):
    '''
    
    '''
    histogram = [0] * 26
    
    word.lower()
    for letter in word:
        index = letter_to_index(letter)
        histogram[index] += 1
    return histogram

def pretty_print(histogram):
    '''
    
    '''
    for i in range(len(histogram)):
        if histogram[i] != 0:
            letter = index_to_letter(i)
            print("%s: %d" %(letter, histogram[i]), end=" ")
    print("")

histogram = compute_letter_frequencies_list("hello")
pretty_print(histogram)


# Note: We have now seen lists of tuples, lists of lists, dictionaries of lists, etc. In general, we can have sequences of sequences. The types of sequences that can be nested and the number of nesting levels is up to you, the programmer!

# ## TODO
# 1. Work on PA6.
# 1. Bonus PA is due tonight.
# 1. Start studying for the final.
# 
# ## Next Lesson
# * Practice and review for the final. 
# 
# Note: dictionaries are the last big topic of CptS 111, congrats on learning all of these cool Python concepts in CptS 111 :)
