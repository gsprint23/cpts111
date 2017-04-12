
# coding: utf-8

# # [CptS 111 Introduction to Algorithmic Problem Solving](http://piazza.com/wsu/spring2017/cpts111/home)
# [Washington State University](https://wsu.edu)
# 
# [Gina Sprint](http://eecs.wsu.edu/~gsprint/)
# # L13-2 Advanced Lists
# 
# Learner objectives for this lesson
# * Learn about aliasing
# * Passing lists into functions as arguments
# * Returning lists from functions

# ## Aliasing
# When we declare a list variable, as in `list1 = [0, 1, 2, 3]`, a list *object* is created. We say the variable `list1` is a *reference* to the list object `[0, 1, 2, 3]`. In memory, this looks like the following:
# ![](https://raw.githubusercontent.com/gsprint23/cpts111/master/lessons/figures/reference_example.png)
# 
# If we declare another list variable, `list2 = [0, 1, 2, 3]`, `list2` refers to a *different* list object, even though both objects that `list1` and `list2` refer to contain the same items:
# ![](https://raw.githubusercontent.com/gsprint23/cpts111/master/lessons/figures/references_multiple_example.png)
# 
# We can test if `list1` and `list2` refer to lists that contain the same elements:

# In[21]:

list1 = [0, 1, 2, 3]
list2 = [0, 1, 2, 3]
print(list1 == list2)


# To test if `list1` and `list2` *refer* to the same list object, we can use the Python reserved keyword, `is`. `is` tests whether two variables refer to the same object: 

# In[22]:

list1 = [0, 1, 2, 3]
list2 = [0, 1, 2, 3]
print(list1 is list2)


# Note: Python is intelligent! Since strings are immutable, only one object is created in the following code:

# In[23]:

string1 = "cpts111"
string2 = "cpts111"
print(string1 == string2)
print(string1 is string2)


# In the above code, both `string1` and `string2` refer to the same string object. This phenomenon is called *aliasing*. 
# ![](https://raw.githubusercontent.com/gsprint23/cpts111/master/lessons/figures/alias_string_example.png)
# 
# Let's return to our list example and see aliasing at work. 
# 
# If instead of assigning `list2` to a new list object, we assign `list2` to `list1`: `list2 = list1`, `list2` refers to the same object as `list1`.
# ![](https://raw.githubusercontent.com/gsprint23/cpts111/master/lessons/figures/alias_example.png)
# 
# We now say the object is *aliased*, because it has more than one reference, or alias.
# 
# If the aliased object is mutable, either reference can modify the object:

# In[24]:

# same object aliased by list1 and list2
list1 = [0, 1, 2, 3]
list2 = list1
print(list1)
print(list2)
list2[2] = 100
print(list1)
print(list2)
print("\n")

# compared to creating two separate objects list1 and list2
list1 = [0, 1, 2, 3]
list2 = [0, 1, 2, 3]
print(list1)
print(list2)
list2[2] = 100
print(list1)
print(list2)


# Aliasing is important to keep in mind, especially when passing lists as arguments.

# ## Lists Arguments
# We can pass lists into functions as arguments:

# In[25]:

def pretty_print_list(list_to_print):
    '''
    
    '''
    for value in list_to_print:
        print(value, end=" ")

numbers = [0.0, 0.2, 0.4]
pretty_print_list(numbers)


# When a list is passed as an argument to a function, the function parameter variable is a *reference* to the list, making the list *aliased*. This means that if we modify a list in our function, the change to the object persists and the calling code will see the change.
# 
# In the example above, `numbers` and `list_to_print` are aliases to the list object `[0.0, 0.2, 0.4]`. If `pretty_print_list()` can use `list_to_print` to modify the object. 
# 
# Let's write a new function, `add_one()`, that adds one to each value in a list:

# In[26]:

def add_one(list_arg):
    '''
    
    '''
    for i in range(len(list_arg)):
        list_arg[i] += 1

numbers = [0.0, 0.2, 0.4]
print(numbers)
add_one(numbers)
print(numbers)


# ## Returning Lists
# We can write functions that return lists. Consider a function that returns a list of numbers from arguments `start_index` to `end_index + 1`:

# In[27]:

def create_sequence(start_index, end_index):
    '''
    
    '''
    sequence = []
    
    for i in range(start_index, end_index):
        sequence.append(i)
    return sequence

first_ten_nums = create_sequence(0, 10)
print(first_ten_nums)


# ## TODO
# 1. Work on PA6.
# 1. Read zyBooks Ch. 11, 12 and How to Think Like a Computer Scientist Ch. 10, 12.
# 
# ## Next Lesson
# We are going to practice with lists, cover the binary number system and talk about dictionaries, a quite powerful data structure!
