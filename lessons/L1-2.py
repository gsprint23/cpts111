
# coding: utf-8

# # [CptS 111 Introduction to Algorithmic Problem Solving](http://piazza.com/wsu/fall2016/cpts111/home)
# [Washington State University](https://wsu.edu)
# 
# [Gina Sprint](http://eecs.wsu.edu/~gsprint/)
# # L1-2 Getting Started with Python
# 
# Learner objectives for this lesson
# * Python basics: syntax, standard identifiers, reserved keywords, commenting, etc.
# * Data types and typecasting
# * Input from the user and output to the user
# * Writing and running code to solve a problem

# ## Example Problem: Compute the Volume of a Cone
# Say we want to write a program to compute the volume of a cone, such as the one hosted on [Google Search](https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=volume%20of%20cone):
# ![](https://raw.githubusercontent.com/gsprint23/cpts111/master/lessons/figures/cone_volume.png)
# 
# What information would we need? 
# 
# How would we relate that information to produce a result? 
# 
# How would we interact with the user? 
# 
# How would we test such a program for correctness? 
# 
# These are all questions you will start to think when solving problems *algorithmically*.
# 
# ### Data Requirements
# Problem input: radius (of the base), height (of the cone)
# 
# Problem output: volume (of the cone)
# 
# ### Relevant Formula
# $ volume = 1 / 3 * pi * radius^2 * height $
# 
# ### Program Design
# Algorithm
# 1. Get the radius and height for the cone
# 1. Compute the volume of the cone $ volume = 1 / 3 * pi * radius^2 * height $
# 1. Display the resultant volume of the cone
# 
# ![](files\figures\volume_cone.png)
# 
# ### Actual Python Implementation

# In[1]:

radius = 0.0
height = 0.0
volume = 0.0

# get radius from user
print("Please enter the radius of a cone")
radius = float(input())

# get height from user
print("Please enter the height of a cone")
height = float(input())

# use relevant formula to compute volume
volume = 1 / 3 * 3.14 * radius ** 2 * height

# display result to user
print("The volume of a cone with radius %.2f and height %.2f is %.2f" %(radius, height, volume))


# Don't worry about understanding the details of this program. You are taking this class to learn how to write Python code.
# 
# ## Python Basics
# Python was created by Guido van Rossum in the late 1980s. It is an open source, general-purpose language. It is flexible and powerful, yet still simple enough to be quickly picked up by new programmers. Python is fairly high on the high-level programming languages spectrum, meaning its syntax and grammar is fairly close to pseudo-code.
# ![](https://raw.githubusercontent.com/gsprint23/cpts111/master/lessons/figures/language_continuum.jpg)
# 
# Python can be run on any computer architecture, so long as a Python interpreter is installed on the machine. This is similar to Java in the sense that as long as Java (more specifically, a Java Virtual Machine) is installed on your computer (you've seen the pesky Java update dialogs), you can run Java code written on any other architecture. It is convenient, cross-platform approach to application development. In contrast to *interpreted languages*, *compiled languages* are translated into specific computer architecture machine code (i.e. for a specific Intel processor instead of an AMD processor). Interpreted languages, such as Python and Java, tend to run slower than compiled languages, such as C and Fortran. 
# 
# ### Python Language Elements
# Python programs contain instructions that specify what the computer is supposed to "compute".
# 
# #### Comments

# In[3]:

# get radius from user


# The above instruction is an example of a **single line comment**. *Comments are ignored by the Python interpreter*. Single line comments are denoted by a `#` symbol; any code after the `#` symbol is simply text and is not going to be run by Python.

# In[6]:

'''This is an example 
of a multi-line comment'''

"""So is this!"""


# Use comments liberally in your code! They help others read your code (including yourself, months later when it isn't so fresh in your mind). In this class, you will be required to comment your code by adhering to the CptS 111 [Python Coding Standard](http://nbviewer.jupyter.org/github/gsprint23/cpts111/blob/master/lessons/PythonCodingStandardCptS111.ipynb).
# 
# #### Standard Identifiers
# Represent names of built-in variables (data) and functions (operations) in Python, such as `print` and `input`. It is not recommended to redefine these identifiers.
# * `print(<text to display>)` displays text to the screen
# * `input()` reads input from the keyboard
# 
# #### User-defined Identifiers
# Names memory cells used for computations ("variables"). We will also later be able to name our own algorithms ("functions").
# * Identifiers can only contain letters, numbers, and underscores
# * Cannot begin with digits
# * Should not redefine standard Python standard identifiers
# * Should choose meaningful variable names (i.e. `radius` to store the radius of a cone, versus `my_variable`)
# * Use underscores between words for readability (e.g. `cone_volume`)
# * Make your variable names sufficiently different so you don't get them confused
# 
# Note: Python is case sensitive.
# 
# #### Reserved Keywords
# Python has reserved several identifiers as keywords that have special meaning about the nature of your program. You cannot use reserved keywords as user-defined identifiers in your program. Examples of reserved keywords include `True`, `False`, `None`, `and`, `or`, `not`, `if`, `else`, `elif`, `in`, `is`, `pass`, `return`, `for`, `while`, etc. In the near future, you will learn about these keywords and what they do!
# 
# ### Variable Declarations
# Declaring a variable reserves memory space for a value. It also associates a name with a memory cell (user-defined identifier).

# In[8]:

radius = 0.0


# The above instruction declares a variable called `radius` and stores the value `0.0` in the memory location associated with `radius`. `radius` is an example of a user-defined identifier.
# 
# ### Data Types
# All variables have an associated data type. A **data type is a set of values and a set of operations on those values.** Examples of data types include:
# * Integer (numeric)
#     * Values: integer whole numbers e.g. 1, -10, 5000, etc.
#     * Operations: several, including + - * / // (integer division) % (mod) and comparisons > < <= >= == !=
# * Float (numeric)
#     * Values: real numbers (must include a decimal point) e.g. 3.14, -1000.0, etc.
#     * Operations: several, including + - * / and comparisons > < <= >= == !=
# * String (sequence of characters)
#     * Values: characters e.g. "cpts111", "ABCD", '123ABC', etc.
#     * Operations: several, including + (string concatenation, joins strings by linking them end-to-end), * (repetition, repeats strings), etc. We will learn more about string operations later in the course.
#     * *Note: You can use either double or single quotes to specify a string.*
#     * *Note: Even though some strings look like numbers (e.g. "2"), they are not numbers. For example: `"5" + "7"` returns the string "57" because "5" and "7" are strings, not integers.
# 
# If you want to find out what data type a variable is, Python will tell you. Use the function `type(<variable name.)` to find out.

# In[23]:

x = 77.0

print(type(5))
print(type(x))
print(type('this is a string'))


# ### Executable Statements
# Do the work of the algorithm by transforming inputs into outputs. For example, consider the volume of the cone example:

# In[9]:

volume = 1 / 3 * 3.14 * radius ** 2 * height


# When the code statement above is executed by Python (the program is running), Python *evaluates* the expression on the right hand side of the assignment operator (=), and assigns the result to the variable `volume`. 
# 
# Python evaluates arithmetic expressions according to the same order of operation precedence you are familiar with (think PEMDAS: **P**arenthesis, **E**xponents, **M**ultiplication, **D**ivision, **A**ddition, **S**ubtraction), plus a few more operators. 
# 
# Check out this [Python precedence table](http://thepythonguru.com/wp-content/uploads/2015/08/python-operator-precedence1.jpg) to learn more.
# 
# #### Assignment Statements
# Store a computational result into a variable
# * The = operator does the assignment
# * The *, -, +, /, // operators perform the computation

# The assignment operator '=' in programing is not the same as = in math
# * Math: y = x means y is equivalent to x
# * Programming: y = x means "y is assigned x"
#  * = is an operator, not a relationship
#  * Don't read it as "y equals x" 
#  * **Read it as "y gets x" or "y is assigned to x"** 
# * Example: x = x + 1
# ![](https://raw.githubusercontent.com/gsprint23/cpts111/master/lessons/figures/assignment_example.png)
# Clearly not mathematically "equal"
# 
# We can also assign the value of one variable to another:

# In[ ]:

x = 5 # declare a new variable, x, and assign it the integer 5
y = x # declare a new variable, y, and assign it the value of x (which is 5)
y = -x # compute the negation of x (-5) and assign it to y


# #### Shorthand Assignment Operators
# Code such as, `x = x + 1` is quite common, in fact, it is so common that Python has a shorthand operator (+=) to shorten this code: `x += 1`. There are other shorthand operators for other arithmetic operators too:

# In[37]:

x = 0
print(x)
x = x + 1
print(x)
x += 3
print(x)
x -= 3
print(x)
x *= 5
print(x)


# #### Input/Output Statements
# It is extremely useful to obtain input data interactively from the user, and to display output results to the user
# 
# Python offers several *functions* that perform input and output operations.
# 
# Begin Digression: Functions
# 
# A function is a set of statements that perform a task.
# A function performs the task, hiding from you the details of how it performs the task (they're irrelevant)
# We'll study functions in depth!
# 
# End Digression
# 
# ##### Output
# The [`print()`](https://docs.python.org/3/library/functions.html#print) function is used to display text output of the program to the user, via the console. We have already seen the `print()` function in action:

# In[14]:

print("The volume of a cone with radius %.2f and height %.2f is %.2f" %(radius, height, volume))


# The text in red and surrounded by quotes is called a *string*, which is a sequence of characters. This is what will be displayed to the screen. 
# 
# The `%.2f` is called a *placeholder* for a floating point number (i.e. the f) with 2 decimal places (i.e. the .2). `%d` is used as placeholder for integers and `%s` is used as a placeholder for strings. 
# 
# The variable names at the end of the statement in parenthesis are the list of values corresponding to the placeholder (order matters!). The value of `radius` will be inserted at the first placeholder, the value of `height` for the second, and the value of `volume` for the third. Do you see that order matters?
# 
# Note: Adding `"\n"` to a string will print a newline character, a non-printable character that starts the cursor on a new line. This can be useful if you want to add extra space between text without writing extra `print()` statements.

# In[24]:

print("Standard spacing")
print("Adding extra space with the newline character\n")
print("**Next line**")


# ##### Input
# The [`input()`](https://docs.python.org/3/library/functions.html#input) function is used to collect input from the user of our programs via the keyboard. We have already seen the `input()` function in action:

# In[ ]:

radius = float(input())


# This statement forces the program to pause until the user enters a value from the keyboard and hits the return key. `input()` returns a string representation of the text entered by the user (recall a string is a sequence of characters). Since we want to assign a floating point number to the variable `radius` for use in arithmetic computation later, we *type cast* the string entered by the user into a value of type `float`.
# 
# Notes on input/output:
# * `input()` should always be used in conjunction with a `print()` statement that displays a prompt, so that the user knows that an input value is expected.
# * You can actually combine the prompt and the read input statements in one line. Simply place a string inside of the parentheses for `input()`: `radius = float(input("Please enter the radius"))`. In this case, the inner-most function (`input()`) is executed first. Once the user has pressed enter and the value is read in, the value is converted to a float by the type cast.
# 
# ### Getting `help()`
# If you want more information about how to use a function, such as `print()`, ask Python! Type `help(<identifier name>)` to get more information about a variable, data type, function, etc. 

# In[38]:

help(print)


# ## Debugging
# The process of locating and fixing errors in your programs is called *debugging*. There are 3 types of errors that can occur in a program:
# 1. Syntax: Incorrect program structure, e.g. a missing parenthesis: `print("hello"`
# 1. Runtime: Errors that crash your program, e.g. dividing by zero: `5 / 0`
# 1. Logic/semantic: Program does not do what you intend it to do, e.g. producing an incorrect cone volume result

# ## TODO
# 1. Test your installation of Anaconda3 and your Python development environment:
# Following [Lab 0](http://nbviewer.jupyter.org/github/gsprint23/cpts111/blob/master/labs/Lab0.ipynb), you should have downloaded and installed [Anaconda3](https://docs.continuum.io/anaconda/install). This is the Python distribution we are going to use for this class. Follow these steps to run the volume of a cone code from above:
#     1. Launch the Spyder IDE (integrated development environment).
#     1. Copy and paste the volume of a cone code into the left panel's text editor. 
#     1. Save the program as cone_volume.py. Press the run button (the green play button) on the toolbar or press F5 on your keyboard to run the program. 
#     1. In the right panel of Spyder, your code should be running in the console, cool!
# 1. Visit the [course schedule](http://www.eecs.wsu.edu/~gsprint/cpts111/schedule.html) and read chapters 1 and 2.
# 1. Go to the Voiland College of Engineering and Architecture Ice Cream Social tomorrow at 3pm in the ETRL courtyard. Talk to Computer Science clubs and meet cool new people.
# 
# ## Next Lesson
# Arithmetic in Python!
