
# coding: utf-8

# # [CptS 111 Introduction to Algorithmic Problem Solving](http://piazza.com/wsu/spring2017/cpts111/home)
# [Washington State University](https://wsu.edu)
# 
# [Gina Sprint](http://eecs.wsu.edu/~gsprint/)
# # L13-1 List Methods
# 
# Learner objectives for this lesson
# * Apply list methods
# * Delete items from a list
# * Understand the relationship between strings and lists

# ## List Warm-up Problem
# Write code to do the following:
# 1. Initialize a list of a few of your favorite foods
# 1. Print out the number of items in the list
# 1. Replace the last item in the list with "candy"
# 1. Using a loop, print out each food separated by a comma and a space, all on the same line
#     * Note: do not have an extra comma after the last element!
# 
# Example output:
# `pizza, pasta, bread, salad, ice cream`
# 
# Note: your output **should not** have hard brackets or quotes like the default output from `print(fav_foods)`:
# 
# `['pizza', 'pasta', 'bread', 'salad', 'ice cream']`

# In[2]:

# 1
fav_foods = ['pizza', 'pasta', 'bread', 'salad', 'ice cream']
# 2
print("Number of items in fav_foods:", len(fav_foods))
# 3
fav_foods[-1] = "candy"
print(fav_foods)
#4
for i in range(len(fav_foods) - 1):
    print(fav_foods[i] + ", ", end="")
print(fav_foods[-1])


# ## List Methods
# Just like with strings, lists are objects that have methods we can utilize. 
# 
# ### `append()`
# For example, since lists are mutable, there is an `append(<new item>)` method to add an item to the end of a list:

# In[1]:

cities = ["Pullman", "Spokane"]
print(cities)

# adds the string as an item
cities.append("Seattle")
print(cities)

# adds the list as an item
cities.append(["Moscow"])
print(cities)


# As review, how could we achieve the same functionality as `append()` without using `append()`?

# In[2]:

cities = ["Pullman", "Spokane"]
print(cities)

# adds the strings as an item
cities += ["Seattle"]
print(cities)


# ### `extend()`
# `extend()` is similar to `append()`; however, `extend()` takes a list as an argument and adds each item to the list:

# In[3]:

cities = ["Pullman", "Spokane"]
print(cities)

# adds each string in the list as an item
cities.extend(["Seattle", "Couer d'Alene"])
print(cities)


# What would happen if we used `append()` instead of `extend()` in the above code?

# In[4]:

cities = ["Pullman", "Spokane"]
print(cities)
cities.append(["Seattle", "Couer d'Alene"])
print(cities)


# `cities` becomes a nested list!

# ### `sort()`
# Many applications require lists of items to be sorted. In CptS121, you will learn how to write your own sorting algorithms. For now, we will use the `sort()` list method:

# In[6]:

cities = ["Pullman", "Spokane", "Seattle", "Couer d'Alene"]
print(cities)

# ascending order
cities.sort()
print(cities)


# How would you sort a list in descending order? Try using `help(cities.sort)` to find out:

# In[7]:

help(cities.sort)


# In[8]:

print(cities)
cities.sort(reverse=True)
print(cities)


# ## Deleting Items in a List
# Since lists are mutable, we can delete items in a list. 
# 
# ### Single Item Deletes
# We have two list methods to delete a *single* item in a list
# 1. When you know the *index* of the item to delete
#     * `item_removed = pop(<index>)`
# 1. When you know the *value* of the item to delete
#     * `remove(<item>)`

# In[9]:

cities = ["Pullman", "Spokane", "Seattle", "Couer d'Alene"]

# pop returns the item removed
city = cities.pop(2)
print(city)
print(cities)

# remove does not return the item removed
cities.remove("Spokane")
print(cities)


# ### `del` Keyword and Multiple Item Deletes
# Alternatively, we can delete an object using the `del` reserved keyword:

# In[10]:

cities = ["Pullman", "Spokane", "Seattle", "Couer d'Alene"]
print(cities)

# del is not a function
del cities[1]
print(cities)


# We may want to delete multiple items at a time. We can do this with a slice and `del`:

# In[11]:

cities = ["Pullman", "Spokane", "Seattle", "Couer d'Alene"]
print(cities)

del cities[0:3]
print(cities)


# ### Relationship Between Strings and Lists
# A list of single character strings is not a string:

# In[12]:

my_list = ["c", "p", "t", "s", "1", "1", "1"]
print("%s" %(my_list))


# ### `join()` (string method)
# However, we can turn a list of strings into a string with the `join()` string method. We need to specify a "delimiter" string to use to concatenate the individual strings in a list into a single string:

# In[18]:

my_list = ["c", "p", "t", "s", "1", "1", "1"]
delimiter = '' # empty string
my_string = delimiter.join(my_list)
print("%s" %(my_string))

delimiter = ':)'
my_string = delimiter.join(my_list)
print("%s" %(my_string))


# ### `list()` (function)
# To convert the string back into a list, we can type cast the string into a list with `list()`:

# In[19]:

my_string = "cpts111"
my_list = list(my_string)
print(my_list)


# ### `split()` (string method)
# `split(<string delimiter>)` breaks a string into pieces at each `<string delimiter>`. The pieces are returned as a list: 

# In[20]:

sentence = "hello how are you"
pieces = sentence.split(" ")
print(pieces)


# ## MA18 Practice Problem
# On a blank sheet of paper, write the following:
# 1. Your full name
# 1. Your TA name
# 1. MA #18
# 
# In pairs (or individually), solve the following problems. Each student needs to turn in their own paper to get credit for MA18.
# 
# Write a program that generates 100 numbers between 1 and 500 inclusive and puts them in a list. The program then does the following using the list:
# * Prints the numbers
# * Sorts the numbers
# * Prints the largest and smallest number in the list
# * Determines the number of times a user-specified number is in the list
# * Removes all instances of a user-specified number in the list
# 
# ### Step 1
# Create an empty list to store the 100 numbers.

# In[3]:

nums = []


# ### Step 2
# Write code to generate 100 random numbers between 1 and 200 store them in the list.

# In[4]:

import random
for i in range(100):
    nums.append(random.randint(1, 200))


# ### Step 3
# Write code to print the list without the brackets. Create a separate function for this since you will be printing the list several times. 

# In[5]:

def print_list(nums):
    for num in nums:
        print(num, end=" ")
    print()
print_list(nums)


# ### Step 4
# Write code that sorts the numbers in ascending order. Print the list after it is sorted.

# In[6]:

nums.sort()
print_list(nums)


# ### Step 5
# Write code to print the largest and smallest number in the list.

# In[7]:

print("smallest: %d largest: %d" %(nums[0], nums[-1]))


# ### Step 6
# Write code that prompts the user for a number between 1 and 200 and prints how many times that number is in the list. If the number is not in the list print the message: "Sorry, your number is not here!"

# In[8]:

def count_num(nums):
    num_to_find = int(input("Please enter a number in [1, 200]: "))
    count = nums.count(num_to_find)
    if count == 0:
        print("Sorry, your number is not here!")
    else:
        print("%d is in the list %d time(s)." %(num_to_find, count))
    return count

count_num(nums)


# ### (Tricky) Step 7
# Write code that prompts the user for a number between 1 and 500 and removes all instances of that item from the list (if it is in the list). If the number is not in the list print the message: "Sorry, your number is not here!"

# In[9]:

def remove_num(nums):
    '''
    Precondition: nums is sorted
    '''
    num_to_remove = int(input("Please enter a number in [1, 200] to remove: "))
    if num_to_remove not in nums:
        print("Sorry, your number is not here!")
    else:
        start_index = nums.index(num_to_remove)
        count = nums.count(num_to_remove)
        del nums[start_index:start_index+count]

remove_num(nums)
print_list(nums)


# ## TODO
# 1. Work on the Bonus PA and PA6.
# 1. Read the related chapters in the books.
# 
# ## Next Lesson
# We wrap up lists!
