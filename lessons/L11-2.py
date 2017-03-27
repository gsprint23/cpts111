
# coding: utf-8

# # [CptS 111 Introduction to Algorithmic Problem Solving](http://piazza.com/wsu/spring2017/cpts111/home)
# [Washington State University](https://wsu.edu)
# 
# [Gina Sprint](http://eecs.wsu.edu/~gsprint/)
# # L11-2 Exam #2 Review

# ## What to Bring?
# * Two sharp pencils
# * Python Programming knowledge in your head :)
# * A "cheat sheet" (see below)  
# 
# ## What NOT to Bring?
# * Electronics (including calculators) may not be used during the exam!
# * Notes may not be used during the exam!
# 
# Note: If you are caught cheating, your exam will be confiscated and you will receive a 0.
# 
# Note: Use the restroom before class. **Once testing starts, the only reason for leaving the classroom is turning in your exam as done.**
# 
# ## The "Cheat Sheet"
# The exam will be closed-book, but you will be allowed a **handwritten** "cheat sheet": one side of a page whose dimensions may not exceed 8-1/2" by 5-1/2" (i.e. **one-half of a standard sheet of notebook paper**). You must present your cheat sheet to myself or a TA so it can be verified that it meets regulations. 
# 
# If you bring/use a cheat sheet that: 
# 1. Exceeds the allowable dimensions
# 1. Has writing on both sides of the page
# 1. Contains non-handwritten text (i.e. printed)
# 
# You run the risk of its being confiscated prior to the exam. This policy will be strictly enforced.
# 
# If you choose to use a cheat sheet, you will be required to turn in your cheat sheet with your exam.
# 
# ## Exam Timeframe
# Please be aware that, because you will be taking the exam during a normal lecture period (50 minutes), time will be extremely tight for the exam so manage your time well. If you show up late to class, you will have less time to take the exam. 

# ## Exam Coverage
# The exam covers everything we have covered so far in the course. Here is an outline of the topics we have covered so far:
# 
# ### Exam #1 Topics
# [Exam #1 review topics](http://nbviewer.jupyter.org/github/gsprint23/cpts111/blob/master/lessons/L7-1.ipynb)
# 
# ### 1 Iteration
# (Chapters 7, 8, 9 in zyBooks; Chapters 4 and 8 in *How to Think Like a Computer Scientist*)
# 
# * Define what is repetition in programs
#     * Allows for a group of operations to be performed multiple times
# * Define what is one iteration
#     * Discuss how loops are defined based on iterations
# * When is a loop needed?
# * Apply and implement the 2 looping constructs supported in Python
#     * `while`
#         * Explicit progress towards the Boolean condition becoming false
#     * `for`
#         * Iterating over sequences
#         * `range()`
#     * When is one looping construct more appropriate than the other?
# * Identify, apply, and implement the major loop patterns
#     * Looping until a general Boolean condition is met
#         * i.e. `while bank_balance > 0:`
#     * Looping for a certain number of repetitions, which is known before loop execution
#         * i.e. `while count < 10:`
#     * Looping until a special value is encountered
#         * i.e. a menu
#         * i.e. `while choice != "q":`
#     * Looping until a value within valid range is entered by user
#         * i.e. `while is_valid == False:`
# * Apply and implement nested loops
# * `break` statement
# * What is an infinite loop?
#     * A loop which will execute "forever"
# * Describe and apply compound (shorthand) assignment operators
#     * These include: +=, -=, *=, /=, //=, %=
# * Provide an example of an off-by-one loop error

# ### 2 File I/O
# (Chapter 10 in zyBooks; Chapter 11 in *How to Think Like a Computer Scientist*)
# * What is a file object?
#     * A communication channel between the program and a file
# * What is the 3-step file processing template?
#     * Open a file
#     * Process the file
#     * Close the file
# * What is a file mode?
# * What is a path?
#     * Relative path vs absolute path
# * Apply `open()`, `close()`, `readline()`, `readlines()`, `print(file=<file object>)`and `write()`
#     * You should be able to open files for read and write modes
#     * Removing leading and trailing whitespace characters with `strip()`
# * Iterating through files until the end of a file is reached
#     * `for line in in_file.readlines():`
#     * `while line != "":`
# * Positioning in files (the file "cursor")
# * Calling `print()` to write to a file

# ### 3 Strings
# (Chapter 10 in zyBooks; Chapter 9 in *How to Think Like a Computer Scientist*)
# * Define what is a string in Python
#     * A sequence of alphabetic, numeric, and special characters
# * Declare and apply strings
# * String concatenation
# * String indexing
#     * 0 based
#     * Valid indices
# * Apply the built-in `len()` function
#     * Returns the length of a string
# * Iterating over characters in a string
# * String slicing
# * Strings are immutable
#     * Strings cannot be changed
# * String comparison
#     * Strings are compared by their Unicode values
# * String searching
# * Apply string methods
#     * `strip()`
#     * `upper()`
#     * `lower()`
#     * `find()`
#     * `replace()`
#     * others?

# ### Other topics
# * Random number generation
#     * Import the `random` module
#     * Apply the `random.randrange()` function
#         * Pass in a starting integer and an ending integer + 1
#     * Apply the `random.randint()` function
#         * Pass in a starting integer and an ending integer
# * `turtle` graphics and loops

# ## Recommended Strategy for Preparing for the Exam
# The exam questions will require you to solve problems in a variety of formats: defining key terms, evaluating expressions, writing code, determining the output of code, etc.
# 
# I recommend that you use the following activities and materials to prepare for the exam:
# * Review micro assignments, lab exercises, programming assignments, and problems solved in class
#     * These may well be your best resources. An excellent learning activity would be to re-solve the micro assignments, lab exercises, in class exercises, and programming assignments. 
# * Lesson notes and example code
# * Read the textbook
#     * Read or re-read zyBooks chapters 7-10 and How to Think Like a Computer Scientist chapters 4, 8, 9, and 11. 

# ## Extra Practice Problems

# ### 1
# The following questions refer to the following program segment:

# In[ ]:

g = 0
s = 0
i = 50
t = 0
while i > 0: 
    t = int(input())
    s = s + t
    if t < 0:
        g = g + 1
    i -= 1


# 1. How many times is the loop body of the while statement executed?
# 1. At the end of the execution of the loop, describe the value stored in variable `s` 
# 1. At the end of the execution of the loop, describe the value stored in variable `g`
# 1. Modify the above code in order to make the code more readable and indicative of its purpose.

# ### 2
# Write code to open a file output.txt for writing. Then write `pi` from the `math` module to 2 decimal places to the file and close the file.

# ### 3
# Write a program to copy the contents of one file to another. As part of your solution, define and call a function, `copy_file(source, destination)` that accepts two parameters:
# 1. `source`: the name of the file to copy contents FROM
# 1. `destination`: the name of the file to copy contents TO

# ### 4
# The following questions refer to the following code: `course = "CptS 111 Spring 2017"`
# 1. Write code to print the "2" in `course`
# 1. Write code to print the "111" in `course` using the slice operator
# 1. Write code to assign a new variable, `new_course`, `course`, but with "Summer" instead of "Spring"
# 1. Write code to overwrite the string stored in `course` in all lower case letters

# ### 5
# (Tricky) The output below is from code with a variable called NUM_STARS set to 5 that determines the number of stars to print on each line (how? :) ). Write code using iterative statements that produces this output for any value of NUM_STARS.
# 
# ```
# NUM_STARS 5:
# *****5
# 0
# ****4
# *1
# ***3
# **2
# **2
# ***3
# *1
# ****4
# 0
# *****5
# ```

# ### 6
# Write a `for` loop that sums the squares of the odd integers from -111 to 333 inclusive. 

# ### 7
# Write a function called `sum_multiples_of_2_5()` that returns the sum of the integers in the range [1, 100] inclusive that are multiples of 2 AND 5.

# ### 8
# Rewrite the following code segment as an equivalent segment that uses a `for` loop.

# In[ ]:

summ = 0
next_val = 1
bound = 10
while next_val < bound: 
    summ += next_val + 1
    next_val += 1
print(summ)


# ### 9
# What is printed by the following nested loop?

# In[ ]:

for x in range(1, 5):
    for y in range(x, x + 1, 1):
        print("%d %d " %(x, y), end="")
    print("")


# ### 10 
# Write a program to prompt the user to enter an integer that is even (for this problem, 0 is neither even nor odd). The code must ensure that en even number is entered. Once an even integer is entered, the program prints the integer to the screen.

# ### 11
# What is the output of the following code segment?

# In[ ]:

for k in range(4, 0, -1): 
    for i in range(1, 5 - k + 1, 1):
        print(".", end="")
    for j in range(1, 2 * k, 1):
        print("A", end="")
    print("")


# ### 12
# Given the following input file, sentence.txt:
# 
# Example sentence.txt
# ```
# Coding
# in
# Python
# is
# SUPER
# FUN
# ```
# 
# Write a program to do the following:
# 1. Open an input file sentence.txt for reading
# 1. Open an output file sentence_out.txt for writing
# 1. Read each line in from the input file and write the following to the output file:
#     1. Print the contents of the line followed by a comma
#     1. Print the length of the line followed by a newline
# 
# Example sentence_out.txt
# ```
# Coding, 6
# in, 2
# Python, 6
# is, 2
# SUPER, 5
# FUN, 3
# ```

# ### 13
# Write a program that uses a loop to print out every other letter in the upper case alphabet. 

# ### 14
# Write a function called `get_string_length(a_string)` that returns the number of characters in the parameter `a_string`. Do not use `len()` in your solution.

# ### 15
# The following problem is adapted from problem 5.9 in Hanly and Koffman.
# 
# Suppose you own a soda distribution that sells Pepsi (ID# 1), Dr. Pepper (ID# 2), Mountain Dew (ID# 3), and Crush (ID# 4) by the case. 
# 
# Write a program to:
# 1. Read the case inventory from a file inventory.txt. In this file there are 4 numbers, one on each line, representing the number of cases for each soda in order of ID#.
# 1. Display and implement the functionality for the following menu:
#     1.	Display current inventory
#     1.	Purchase cases
#     1.	Sell cases
#     1.	Exit
# 1. Validate user input (i.e. there are enough cases in the inventory to sell and the menu choice is valid)

# ## TODO
# 1. Please study for the exam! At a *minimum*:
#     * Work or re-work through:
#         * The above practice problems
#         * Problems from class
#         * Tasks from the more recent labs
#         * Re-visit the PAs
#     * Review key concepts and definitions
# 1. Work on PA5.
# 
# ## Next Lesson
# 1. We have midterm #2.
# 1. Next week, we start lists!
