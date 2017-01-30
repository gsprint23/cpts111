
# coding: utf-8

# # [CptS 111 Introduction to Algorithmic Problem Solving](http://piazza.com/wsu/spring2017/cpts111/home)
# [Washington State University](https://wsu.edu)
# 
# 
# [Gina Sprint](http://eecs.wsu.edu/~gsprint/)
# # L3-2 Modules and Practice
# 
# Learner objectives for this lesson
# * Understand what a module is, how to import a module, and how to access identifiers contained within a module
# * Import the `math` module and utilize math-related variables and functions
# * Import and use the `turtle` module

# ## MA4 Practice Problems
# On a blank sheet of paper, write the following:
# 1. Your full name
# 1. Your TA name (or lab time if you don't know your TA name)
# 1. MA #4
# 
# In pairs, work on the following problems. Each student needs to turn in their own paper to get credit for MA4.
# 
# 1. What are the three kinds of programming errors? Can you give an example of each?
#     1. 
#     1. 
#     1. 
# 1. Rank the order of precedence for the following C operators (1 is the highest precedence, 5 is the lowest precedence):
#     1. `+ # binary addition `
#     1. `- # unary minus (e.g. negation)`
#     1. `% # modulus`
#     1. `= # assignment`
#     1. `() # parentheses `
# 1. Evaluate each of the following equations and *determine the resultant data type*:
#     1. `4 / 12 =`
#     1. `4 // 12 =`
#     1. `4 % 12 =`
#     1. `7 // 4 =`
#     1. `9.0 / 4.0 =`
#     1. `3 / 0 = `
#     1. `3.0 % 1 =`
#     1. `16 % 0 = `
#     1. `3 % 5 = `
#     1. `9 % 5 = `
#     1. `2 * 4 ** 2 =`
#     1. `2 ** 4 ** (2 / 4) = `
# 1. Given `y = m % n`, what are the possible values of `y`?
# 1. Write the following equation as a Python arithmetic statement: 
# $$q=\frac{kA(T_1-T_2)}{L}$$
# 1. Show the output displayed by the following program when the data entered are 12 for `m` and 0 for `n`:

# In[ ]:

m = int(input("Enter an integer> "))
n = int(input("Enter an integer> "))
m = m + 5
n = 3 * n
print("m = %d\nn = %d\n" %(m, n))


# ## Python Modules
# A *module* is a file that contains a collection of related variables and functions. Python provides several modules for us programmers to use in our programs. In order to use the variables and functions within a module, we have to let Python know we want to use the module with an `import <name of module>` statement. 

# In[ ]:

import math


# To access one of the variables or functions in a module, you type the module name (somewhere in the code *after* you import the module, remember Python executes code from top to bottom), followed by a dot, and then the name of the variable or function. For example, we can access an approximation of the mathematical constant `pi` ($\pi$) in the `math` module:

# In[ ]:

print(math.pi)
print("%.4f" %(math.pi))


# As another example, to access the square root function of the `math` module, use `math.sqrt()`:

# In[ ]:

print(help(math.sqrt))
print(math.sqrt(9))


# ## Math Functions
# The Python `math` module defines numerous useful mathematical functions. This library is an excellent example of the power of functions: commonly-used mathematical operations are packaged up in functions that can be re-used over and over. We don't have to define these functions or know how they work, we can simply call the functions and use the return value(s). Examples of math functions available for our use include:
# * `fabs()` for absolute values
# * `ceil()` for computing the ceiling of a number
# * `floor()` for computing the floor of a number
# * `cos()` for cosine function
# * `sin()` for sine function
# * `tan()` for tangent function
# * `pow()` for raising a number to its power
# * `log()` for logarithms (see also `log2()` and `log10()`
# * `sqrt()` for computing square roots
# 
# Note: trig functions expect arguments in radians, not degrees. To convert degrees to radians, multiply by (`math.pi` / 180) or use the `radians()` function in the `math` module.
# 
# You can find out all the functions available within a module by importing the module, typing the module name and a dot, then pressing tab. This "auto-complete" feature is super helpful when learning a new library or when you can't remember the name of a function.

# In[ ]:

x = -5
print("x: %d absolute value of x: %d" %(x, math.fabs(x)))

degrees = 90
radians = degrees * (math.pi / 180)
print("sin(%d): %.2f" %(degrees, math.sin(radians)))


# ## Turtle Graphics
# There are several Python modules available for doing graphical user interface (GUI) programming. For example, the `turtle` graphics library makes it really easy to draw pictures programmatically. We will return to `turtle` graphics later, but for now, check out how easy it is to draw:

# In[ ]:

import turtle
turtle.forward(100)
turtle.done()


# <img src="https://raw.githubusercontent.com/gsprint23/cpts111/master/lessons/figures/turtle_simple.png" width=450</img>

# ## Software Development Method
# Equivalent to the "Scientific Method" in the sciences and the "Systems Approach" in business.
# 
# Six basic steps:
# 1. Specify problem requirements
# 1. Analyze the problem
# 1. Design an algorithm to solve the problem
# 1. Implement the algorithm
# 1. Test and verify the completed program
# 1. Maintain and update the program
# 
# Developing software is an iterative process, your first solution is generally not your best. Your understanding of software your required to build evolves as you understand the problem more. At this point don't be afraid to make mistakes!
# 
# ## Practice Problems
# Apply the software development method to the practice problems below. Have fun!
# 
# Note: Some problem descriptions have been adapted from Chapter 2 of Hanly & Koffman's Problem Solving and Program Design in C (7th Edition)

# ### <mark>Problem #1 Tax</mark>
# Write a program to compute the total price for a purchase after sales tax. Prompt the user to enter the purchase amount and the sales tax percent. Display the total price (to the nearest 2 decimal places) after adding the sales tax to the purchase amount.
# 
# Example output:
# 
# ```
# Please enter the purchase price: 9.00
# Please enter the sales tax as a percent (%): 7.8
# Total purchase price after tax: $9.70
# ```

# In[2]:

purchase = float(input("Please enter the purchase price: "))
tax_percent = float(input("Please enter the sales tax as a percent (%): "))

tax = purchase * (tax_percent / 100.0)
purchase += tax

print("Total purchase price after tax: $%.2f" %(purchase))


# ### <mark>Problem #2 Mileage Reimbursement</mark>
# Write a program that calculates mileage reimbursement for a salesperson at the rate of \$.35 per mile. 
# 
# Example output:
# 
# ```
# MILEAGE REIMBURSEMENT CALCULATOR
# Please enter the beginning odometer reading: 13505.2
# Please enter the ending odometer reading: 13810.6
# You traveled 305.4 miles. At $0.35 per mile, your reimbursement is $106.89
# ```

# In[ ]:




# ### <mark>Problem #3 Pythagoras</mark>
# The Pythagorean theorem states that the sum of the squares of the sides of a right triangle is equal to the square of the hypotenuse.
# 
# $$side1^{2} + side2^{2} = hypotenuse^{2}$$
# 
# For example, if two sides of a right triangle have lengths 3 and 4, then the hypotenuse must have a length of 5. Together the integers 3, 4, and 5 form a Pythagorean triple. There are an infinite number of such triples. Given two positive integers `m` and `n`, **where `m`> `n`**, a Pythagorean triple can be generated by the following formulas:
# 1. side1 = $m^2 – n^2$
# 1. side2 = $2mn$
# 1. hypotenuse = $m^2 + n^2$
# 
# Write a program that takes the values for `m` and `n` as input and displays the values of the Pythagorean triple generated by the formulas above.
# 
# Example output:
# 
# ```
# Please enter a m value: 4
# Please enter a n value: 2
# Pythagorean triple: 12^2 + 16^2 = 20^2
# ```

# In[ ]:




# In[ ]:

# check result


# ## TODO
# 1. To get good at programming you have to write code. Solve all of the practice problems above. Sketch out a pseudocode solution first on paper, then code them up in Python. 
# 1. Work on PA1, it is due Wednesday, February 1 at midnight.
# 1. Functions can be difficult to comprehend at first. Please read about functions in zyBooks and How to Think Like a Computer Scientist for extra exposure to functions, it will help!
# 
# ## Next Lesson
# We will define our own functions!!
