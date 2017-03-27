
# coding: utf-8

# # [CptS 111 Introduction to Algorithmic Problem Solving](http://piazza.com/wsu/spring2017/cpts111/home)
# [Washington State University](https://wsu.edu)
# 
# [Gina Sprint](http://eecs.wsu.edu/~gsprint/)
# # L11-1 Advanced String Processing
# 
# Learner objectives for this lesson
# * Learn about searching
# * Compare strings for equality
# * Apply string methods

# ## String Comparison
# Often we need to compare 2 strings in order to determine if the strings are equal or not (e.g. a 20 questions game or a hang man game). We can use string comparison operators to do this:
# * == (equality)
# * != (not equal)
# * < > (less than or greater than)
# 
# Note: String comparisons are performed by comparing character [Unicode values](http://dev.networkerror.org/utf8/?start=33&end=133&cols=4&search=&show_uni_int=on&show_uni_hex=on&show_html_ent=on&show_raw_hex=on&show_raw_bin=on), index by index.

# In[11]:

print("cpts" == "cpts")
print("cpts" == "CptS")
print("cpts" < "CptS")
print("cpts" > "CptS")


# ## Searching a String
# Supposed we want to determine if a string contains a certain character, such as an "a". How could we solve this problem?

# In[15]:

def find_character(string_to_search, char_to_find):
    '''
    
    '''
    found = False
    
    for character in string_to_search:
        if character == char_to_find:
            found = True
            break
    return found

def find_character_alternative(string_to_search, char_to_find):
    '''
    
    '''
    return char_to_find in string_to_search

word = "cpts111!"
print(find_character(word, "!"))
print(find_character(word, "!"))

print(find_character(word, "T"))
print(find_character_alternative(word, "T"))


# Suppose we want to return the index at which the character is located, and -1 if the character is not found? How could we modify our solution to do this?

# In[14]:

def find_index(word, letter):
    '''
    
    '''
    i = 0
    while i < len(word):
        if word[i] == letter:
            return i
        i += 1
    return -1

print(find_index(word, "!"))
print(find_index(word, "T"))


# ## String Methods
# A function that is associated with an object is called a *method*. To call a method, we use the form `<object>.<method name>()`. We have been using methods when we interact with file objects. Recall:
# 
# ```
# file_object = open("file.txt", "r")
# line = file_object.readline()
# file_object.close()
# ```
# 
# There are several string methods that provide useful string operations. To use a string object method, we use the form `<string variable>.<method name>()`. For example, we have been using the string method `strip()`:

# In[4]:

my_string = "           python           "
my_string = my_string.strip()
print(my_string)


# As another example, the `upper()` method converts each character in the string to the left of the `.` to upper case and returns the new upper case string:

# In[4]:

my_string = "python"
upper_case = my_string.upper()
print(upper_case)


# Useful string method functions include (but are not limited to):
# * `upper()`: returns the string in uppercase
# * `lower()`: returns the string in lowercase
# * `find(<character to find>)`: returns the index of `<character to find>` if `<character to find>` is in the string
# * `replace(<substring to replace>, <string to replace with>)`: returns a string with all occurrences of `<substring to replace>` replaced with `<string to replace with>`
# 
# Read more about string methods in the [Python documentation](https://docs.python.org/3.1/library/stdtypes.html#string-methods)
# 
# Examples:

# In[4]:

my_string = "hello"
print(my_string.find("l"))
new_string = my_string.replace("l", "L")
print(my_string)


# ## Practice Problems
# 
# ### Problem \#1
# Write a function called `my_str_len()` that accepts a string as an argument and returns the number of characters in the string argument. Your function may not make use of the `len()` built-in function. Think loops!
# 

# In[9]:

def my_str_len(word):
    '''
    
    '''
    count = 0
    for letter in word:
        count += 1
    return count

print(my_str_len("hello"))


# ### Problem \#2
# Write a function called `reverse_string()` that accepts a string argument (`word`) and returns the reverse of `word`.

# In[ ]:




# ### Problem \#3
# Write a predicate function called `is_reverse()` that accepts two string arguments (`word1` and `word2`) and returns whether or not `word2` is the reverse of `word1`.

# In[ ]:




# ## TODO
# 1. Work on PA5
# 1. Study for midterm #2
# 
# ## Next Lesson
# 1. We review for the midterm
