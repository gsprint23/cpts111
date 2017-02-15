
# coding: utf-8

# # [CptS 111 Introduction to Algorithmic Problem Solving](http://piazza.com/wsu/spring2017/cpts111/home)
# [Washington State University](https://wsu.edu)
# 
# [Gina Sprint](http://eecs.wsu.edu/~gsprint/)
# # L6-2 Exam #1 Review

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
# ### 1 Introduction to Computer Science, Programming, and Python
# (Chapters 1 and 2 in zyBooks; Chapter 1 in *How to Think Like a Computer Scientist*)
# 
# * Define what is an algorithm
#     * Formal definition
#     * Examples
# * What are the 6 fundamental operations a computer can perform?
# * What are high-level programming languages?
#     * The continuum of languages
#     * How the Python Interpreter works
# * Define what is a comment
#     * Single line comments
#     * Block (multi-line) comments
# * Describe and provide examples of each
#     1. Standard identifiers
#     1. User-defined identifiers
#     1. Reserved keywords
# * Describe the rules for naming an identifier
#     * Consider Python constraints and naming conventions used in the class
#     * Python is case sensitive
# * Define what is a variable
#     * Memory is allocated when a variable is declared
#     * Assigning a value to a variable
#     * How to read `y = 5`: "y gets x" or "y is assigned x"
# * Define what is a data type
# * List three Python types and examples of each
#     1. Integer (`int`)
#     1. Floating-point (`float`)
#     1. String (`str`)
# * Input/output functions
#     * Apply `print()` and `input()`
#     * Describe what is a prompt
# * Using the `help()` function
# * Define and apply escape sequences (the newline (\n)  and double quote (\") are examples of escape sequences)
# * Describe and apply elements of "good" Python style and "best" programming practices

# ### 2 Arithmetic
# (Chapter 3 in zyBooks; Chapter 2 in *How to Think Like a Computer Scientist*)
# 
# * Apply operators to Python types
#     * Arithmetic operators include: +, -, *, /, //, %, and $**$
# * Construct and evaluate valid numerical expressions, including mixed-type expressions
# * Apply operator precedence (review the precedence table!!)
#     * *, /, //, % have the same precedence
#     * +, - have the same precedence, but lower than *, /, //, %
# * Type casting (type conversion)
#     * `int()`
#     * `float()`
#     * `str()`
# * Formatting numeric output using placeholders in a string
#     * %d
#     * %f, %.2f, etc.
#     * %s
# * What is the general algorithm applied to problems in this course?
#     * Get inputs
#     * Perform computations
#     * Output results

# ### 3 Functions
# (Chapters 4 and 5 in zyBooks; Chapters 3, 5, and 6 in *How to Think Like a Computer Scientist*)
# 
# * Define what is a module
# * Apply the `import` reserved keyword
# * Apply Python `math` module variables and functions
#     * Some of these include: `pi`, `sqrt()`, `sin()`, `cos()`, etc.
# * Define what is a function in Python
#     * General rule-of-thumb is 1 function = 1 algorithm = 1 task
# * Construct functions that solve sub-problems
# * Define parameter, argument, global variable, and local variable
# * Name, order of arguments, and return value are very important
# * Cite advantages of using functions in Python
# * What is a function call? 
#     * How do arguments relate to function calls?
#     * Based on a function call, how do you know if the function returns a value?
#         * There is an assignment operator to the left of the function call
#         * There are arithmetic/logical/relational operators to the left or right of the function call
#         * The function call is included in another function call as an argument
# * Define what is scope
# * How do functions communicate with `main()` and vice versa?
# * What is a calling function?
# * What is the call stack and how does Python use it?
# * What is a docstring
# * Describe and provide examples of the three types of errors that can occur in a program
#     * Describe what is a syntax error
#         * Which software tool reports these errors?
#     * Explain what is a logic error
#     * Describe what is a runtime error
# * How to debug your program?

# ### 4 Conditionals
# (Chapter 6 in zyBooks; Chapter 7 in *How to Think Like a Computer Scientist*)
# 
# * What is a Boolean condition?
# * List and apply relational operators
#     * These include: <, >, <=, >=, ==, !=
#     * Distinguish between = and ==
# * List and apply logical operators
#     * These include: `not`, `and`, `or`
# * Apply Boolean operator precedence (review the precedence table!!)
# * Describe what is short circuit evaluation?
#     * Applies to conditional statements with compound logic
# * Define and apply Boolean expressions
#     * DeMorgan's Law
# * What are the three types of statements that algorithms are composed of?
#     * Sequential statements
#     * Conditional statements
#     * Iterative statements
# * Construct multiple alternative `if` statements in Python
# * Construct nested `if` statements
# * How is false defined in Python? How about true?
#     * `bool` type
# * Define what is a predicate function

# ### Other Topics
# (Chapter 4 in *How to Think Like a Computer Scientist*)
# 
# * Turtle graphics

# ## Recommended Strategy for Preparing for the Exam
# The exam questions will require you to solve problems in a variety of formats: defining key terms, evaluating expressions, writing code, determining the output of code, etc.
# 
# I recommend that you use the following activities and materials to prepare for the exam:
# * Review micro assignments, lab exercises, programming assignments, and problems solved in class
#     * These may well be your best resources. An excellent learning activity would be to re-solve the micro assignments, lab exercises, in class exercises, and programming assignments. 
# * Lesson notes and example code
# * Read the textbook
#     * Read or re-read zyBooks chapters 1-6 and How to Think Like a Computer Scientist chapters 1-6. 

# ## Extra Practice Problems

# ### 1
# Evaluate the expressions below. To check your work, run the program to see the output.

# In[ ]:

print(5 // 3 * 2 / (4 % 3) + 5)
print(6.0 * 7 * 2 / 4 + 5 * 11)
print(6 % 4 + 9.0 / 4 + 2 * 5)
print(22 / 44 + (3 % 31))
print(15.0 - 4 // 6 + 2.0 * 1 - (14 % 6))
print(5 % 9 == 5 or (6 * 3 // 4 > 4 and 20 / 6 != 3))
print(4 > 3 and 2 == 2 and 3 > 9 and 34532 // 324 > 293)


# ### 2
# Complement the following statements by applying DeMorgan's Law. Reduce the expressions to the simplest terms possible:
# 1. `not (x and not y) or (x and y > 0)`
# 1. `a or not (b and not (x < y) or a == 0)`
# 1. `(a and b != c and not c) or (not a and not b and c == a)`
# 1. `x < 15 and y >= 1 and (y or x)`
# 1. `(a or not b or not c) and (a > c or not c)`

# ### 3
# What is the output of the following code?

# In[ ]:

x = 0
y = 0
if x < 5:
    print("a")
    if y < x:
        print("bc")
    elif x > 5:
        print("def")
    else:
        print("ghijk")
else:
    print("lmnop")


# ### 4
# Define and call a function that accepts 3 numbers. The function computes and returns the average of the three numbers.

# ### 5
# What is the output of the following code?

# In[ ]:

y = 55.9
x = 1 // 3
print("The value %.2f is in the variable x\n" %(x))
x = 4
print("The value %.1f is in the variable x\n" %(x))
print("The value %d is in the variable y\n" %(y))


# ### 6
# What is the output of the following code?

# In[ ]:

def my_function(param1, param2):
    num1 = 5
    param2 = 2 + num1
    print("%d %d" %(num1, param2))
    param1 = num1 * param2
    return param1

def main():
    num1 = 3
    num2 = 2
    ret_val = my_function(num2, num1)
    print("%d %d %d" %(num1, num2, ret_val))

main()


# ### 7
# Write a program that prompts the user to enter a distance in kilometers. As part of your program, write and call the following functions:
# 1. A function to get a distance in kilometers from the user.
# 1. A function that converts a distance in kilometers to a distance in meters. The relationship between kilometers and meters is: 1 kilometer = 1000 meters
# 1. A function to display the resulting meters.

# ### 8
# Define and call a function called `volume_pyramid()` that accepts two floating-point input parameters, which represent the base (B) and height (h) of the square pyramid. The function returns the volume (V) of the pyramid defined by the two parameters. Recall: $V = 1/3 \times (B \times h)$

# ### 9
# Define and call a function `sum_multiples_of_3_7()` that returns the sum of the integers that are multiples of 3 AND 7. The function should accept three integer values as parameters. 
# 
# For example, your function should return 63 if 7, 21, and 42 are passed into it or 0 if 8, 3, and -7 are passed into it, etc.

# ### 10
# Write a program that determines the total discount, in dollars, for a customer based on age and student/employment status. The program prompts the user for a ticket price (a floating-point) and age (an integer) and sends these values as input parameters to a function called `compute_discount_amount()`. `compute_discount_amount()` does the following to determine the discount:
# 
# 1. Prompts the user for student status of customer. The user should enter "y" if they are currently a student; "n" otherwise.
# 1. Prompts the user for employment status of customer. The user should type "y" if they are a WSU employee; "n" otherwise. Note: a customer may be a student and an employee. 
# 1. The following discounts should be applied: 10% for employees, 12% for senior citizens, 15% for students, and 20% for students who are also employees. Note: a customer is considered a senior citizen if they are 65 years or older. 
# 1. The function returns the value of the ticket price times the discount percentage.

# ### 11
# Given the following `main()` function, write the `evenly_divisible()` function. 
# 
# The `evenly_divisible()` function returns `True` if the first parameter is evenly divisible by the second, or vice versa and `False` otherwise. (Note: What about if the user enters a 0?)

# In[ ]:

def main():
    print("Please enter the first integer: ")
    num1 = int(input())
    print("Please enter the second integer: ")
    num2 = int(input())
    if evenly_divisible(num1, num2):
        print("The two integers are evenly divisible")
    else:
        print("The two integers are not evenly divisible")


# ### 12
# Fix all syntax, logic, and runtime errors found in the following Python code. Be sure to look for omitted keywords, values, and punctuation.

# In[ ]:

Def main(value)
    character = "A",
    
    print("Enter a character: )
    character == input()
    retun character


# ### 13
# What will be printed by the code below?

# In[ ]:

x = 0.0
y = 3.0

if y < 5.0:
    if y >= 0.0:
        print("In the second if statement")
        x = 2 * y
    else:
        print("In the innermost else statement")
        x = -3 * y
        print("I love programming!")
else:
    x = 0 * y
x = x + 1
print("The value of x is %f" %(x))


# ### 14
# Convert this nested if statement to a single if statement with a compound condition:

# In[ ]:

if age >= 35:
    if born_in_us == 1:
        if us_resident >= 14:
            print("Congrats! You can run for president.")


# ### 15
# Using the code below, show the range of values for x and y (EXAMPLE: x > 0 and x < 100, y > 10) which would cause the given statements to be displayed.
# 
# 1. Strawberry pie
# 1. Burger
# 1. Burger with fries
# 1. Coffee with cream
# 1. Coffee with sugar
# 1. Strawberry
# 1. Burger
# 1. Coffee

# In[ ]:

# , end="" suppresses the newline
if x <= 0:
    if y > 0:
        print("Strawberry ", end="")
        if x < 5:
            print("pie")
        elif y < 2:
            print("Burger ", end="")
        else:
            print("with fries")
    else:
        print("Coffee ", end="")
        if x == 0:
            print("with cream")
        elif y > 0:
            print("with sugar")


# ### 16 
# Correct the syntax errors in the code below:

# In[ ]:

If x > 1.0
z = x
else
    z = y


# ### 17
# Based on the code below, specify values for `x` and `y` that will cause the strings below to print (EXAMPLE: x > 0 and x < 100, y > 10). If it is not possible to print a string, explain why.
# 1.	I am nice bye
# 1.	You are weird not funny
# 1.	I am not nice bye
# 1.	You are weird not nice
# 1.	nice bye
# 1.	You are funny not weird
# 1.	I am nice
# 1.	You are funny not funny not weird
# 1.	You are funny smart
# 1.	You are weird
# 1.	bye
# 1.	(nothing printed)

# In[ ]:

# , end="" suppresses the newline
if x < 0 and y < 0: 
    print("You are ", end="")
    if x < 10: 
        print("weird ", end="")
    else:
        print("funny ", end="")

    if y >= 0:
        print("not funny ", end="")
    else:
        if x > 0:
            print("not weird ", end="")
        else:
            print("smart ", end="")
else:
    if x == 8: 
        print("I am ", end="")
    if y < 10:
        print("nice ", end="")
    else:
        print("not nice ", end="")
    print("bye", end="")


# ## TODO
# 1. Please study for the exam! At a *minimum*:
#     * Work or re-work through:
#         * The above practice problems
#         * Problems from class
#         * Tasks from the more recent labs
#         * Re-visit the PAs
#     * Review key concepts and definitions
# 1. Work on PA3.
# 
# ## Next Lesson
# 1. We have midterm #1.
# 1. Next, we start loops!
