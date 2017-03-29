
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

# In[53]:

print("cpts" == "cpts")
print("cpts" == "Cpts")
print("cpts" < "Cpts")
print("cpts" > "Cpts")


# ## Searching a String
# Supposed we want to determine if a string contains a certain character, such as an "a". How could we solve this problem?

# In[58]:

def find_character(string_to_search, char_to_find):
    found = False
    for character in string_to_search:
        if character == char_to_find:
            found = True
            break
    
    return found

def find_character_alt(string_to_search, char_to_find):
    return char_to_find in string_to_search

print(find_character_alt("hello", "l"))


# Suppose we want to return the index at which the character is located, and -1 if the character is not found? How could we modify our solution to do this?

# In[61]:

def find_character_index(string_to_search, char_to_find):
    found = -1
    i = 0
    for character in string_to_search:
        if character == char_to_find:
            found = i
            break
        i += 1
    
    return found

print(find_character_index("hello", "!"))


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

# In[ ]:




# As another example, the `upper()` method converts each character in the string to the left of the `.` to upper case and returns the new upper case string:

# In[62]:

my_string = "python"
print(my_string.upper())


# Useful string method functions include (but are not limited to):
# * `upper()`: returns the string in uppercase
# * `lower()`: returns the string in lowercase
# * `find(<character to find>)`: returns the index of `<character to find>` if `<character to find>` is in the string
# * `replace(<substring to replace>, <string to replace with>)`: returns a string with all occurrences of `<substring to replace>` replaced with `<string to replace with>`
# 
# Read more about string methods in the [Python documentation](https://docs.python.org/3.1/library/stdtypes.html#string-methods)
# 
# Examples:

# In[65]:

my_string = "hello"
print(my_string.find("e"))
new_string = my_string.replace("ll", "L")
print(new_string)


# ## Practice Problems
# 
# ### Problem \#1
# Write a function called `my_str_len()` that accepts a string as an argument and returns the number of characters in the string argument. Your function may not make use of the `len()` built-in function. Think loops!
# 

# In[49]:

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

# In[11]:

def reverse_string(word):
    '''
    
    '''
    reverse = ""
    for i in range(len(word) - 1, -1, -1):
        reverse += word[i]
    return reverse

print(reverse_string("hello"))
# palindromes (strings that are the same forward as backward)
print(reverse_string("madam im adam"))
print(reverse_string("a man a plan a canal panama"))


# ### Problem \#3
# Write a predicate function called `is_reverse()` that accepts two string arguments (`word1` and `word2`) and returns whether or not `word2` is the reverse of `word1`.

# In[12]:

def is_reverse_in_place(word1, word2):
    '''
    
    '''
    i = 0
    j = len(word2) - 1
    
    if len(word1) != len(word2):
        return False
    
    while i < len(word1):
        if word1[i] != word2[j]:
            return False
        i += 1
        j -= 1
        
    return True

print(is_reverse("hello", "olleh"))
print(is_reverse("hello", "olelh"))


# ## MA16
# On a blank sheet of paper, write the following:
# 1. Your full name
# 1. Your TA name
# 1. MA #16
# 
# Write a function that accepts an integer argument. The function displays the number of even, odd, and zero digits in the integer.
# 
# Note: this time, use strings to do this!
# 
# Example: 14019
# Even: 1
# Odd: 3
# Zero: 1

# In[3]:

def even_odd_zero(num):
    '''
    
    '''
    even = 0
    odd = 0
    zero = 0
    
    num_str = str(num)
    # use num_str to update even, odd, zero counts
    # YOUR CODE HERE
    for character in num_str:
        digit = int(character)
        if digit == 0:
            zero += 1
        elif digit % 2 == 0:
            even += 1
        else:
            odd += 1
    # END YOUR CODE
    
    print("even: %d odd: %d zero: %d" %(even, odd, zero))
    
even_odd_zero(14019)


# ## TODO
# 1. Work on PA5
# 1. Study for midterm #2
# 
# ## Next Lesson
# 1. We review for the midterm
