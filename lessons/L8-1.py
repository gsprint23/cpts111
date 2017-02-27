
# coding: utf-8

# # [CptS 111 Introduction to Algorithmic Problem Solving](http://piazza.com/wsu/spring2017/cpts111/home)
# [Washington State University](https://wsu.edu)
# 
# [Gina Sprint](http://eecs.wsu.edu/~gsprint/)
# # L8-1 Iteration with While Loops
# 
# Learner objectives for this lesson
# * Repeat a sequence of Python statements using iterative constructs
# * Apply the `while` reserved keyword to construct loops

# ## Recall
# Recall that algorithms are composed of three different kinds of statements:
# * Sequential: the ability to execute a series of instructions, one after the other.
# * Conditional: the ability to execute an instruction contingent upon some condition.
# * Iterative: the ability to execute one or more instructions repeatedly.
# 
# Today, we'll learn about loops: the ability to repeatedly execute a sequence of statements.
# 
# We have already see examples where we have repeated functionality several times, such as:
# * Lab4: drawing arms of snowflakes with Turtle graphics
# * Lab5: prompting the user to enter 5 numbers and computing the average
# 
# As another example of repetition, consider the following problem statement:
# 
# Suppose I want to know, on average, how much money do I spend per credit card transaction?
# 
# Algorithm:
# 1. For each transaction
#     1. Read in the purchase price
#     1. Accumulate the total money spent so far
# 1. Divide total money spent by total number of transactions
# 
# If we know in advance how many transactions there are (let's say there are 5), we can write this code as follows:

# In[1]:

def get_transaction_price():
    '''
    
    '''
    print("Please enter a transaction: ", end="")
    price = float(input())
    return price

def compute_total_spent():
    '''
    
    '''
    total_spent = 0.0

    # get all 5 transactions from the user
    total_spent += get_transaction_price()
    total_spent += get_transaction_price()
    total_spent += get_transaction_price()
    total_spent += get_transaction_price()
    total_spent += get_transaction_price()
    
    return total_spent

total_spent = compute_total_spent()

avg_spent_per_transaction = total_spent / 5.0

print("On average, you spend %.2f per credit card transaction" %(avg_spent_per_transaction))


# The line `total_spent += get_transaction_price()` is repeated 5 times, one time for each transaction entered by the user. But what if there are 1000 transactions? It would be tedious to have to repeat the accumulation statement 1000 times. What if we had to change something about the statement, maybe the name of the function? Not fun! Thus, enter loops. 
# 
# **Loops let you repeat a body of Python statements as many times as you would like.**
# 
# ## When is a Loop Needed?
# Are any steps repeated?
# * No: then no loop required
# * Yes: use a loop, simple as that!
# 
# There are two kinds of loop statements in Python. The `while` loop and the `for` loop.
# 
# ## The `while` Loop
# The `while` loop is of the following general form:
# 
# ```
# while <test>:
#     <body>
# ```
# 
# Where `<test>` is a Boolean condition and **`<body>` contains indented code that progresses towards the Boolean condition testing `False`** (a way to exit the loop).
# * `<test>` is evaluated at the beginning of the loop
#     * if `<test>` is `True`, `<body>` will be executed.
#     * if `<test>` is `False`, the first line of code *after* the indented `<body>` is executed.
# * After the last statement in `<body>` is executed, control is shifted back to the beginning of the loop and `<test>` is re-evaluated.
# * Progress towards the Boolean condition becoming `False` must be made in `<body>` Otherwise, we will have an infinite loop!
# 
# ![](http://www.tutorialspoint.com/python/images/python_while_loop.jpg)
# (Image from [http://www.tutorialspoint.com/python/images/python_while_loop.jpg](http://www.tutorialspoint.com/python/images/python_while_loop.jpg))
# 
# Let's start with a simple example. Write a program to print `num_stars` number of stars:

# In[2]:

# initialize a loop control variable
num_stars = 10

while num_stars > 0: # boolean condition
    # body of while loop. These indented statements will be repeated when the boolean condition is True
    print("*", end="")
    num_stars -= 1 # progress towards boolean condition being False

# this is the first line of code to be executed once the boolean condition is False
print("\n")


# ![](https://raw.githubusercontent.com/gsprint23/cpts111/master/lessons/figures/while_loop_example.png)
# 
# Note: Often we will have a variable whose value is tested in the Boolean condition. We call this variable a *loop control* variable. In the example above, `num_stars` is our loop control variable. We test its value in the Boolean condition.
# 
# As loops can get complicated (especially when we implement nested loops), making a table to track the value of the loop control variable(s) can be helpful. For the above example, this would like like the following:
# 
# |num_stars|output|
# |-|-|
# |5|\*|
# |4|\*|
# |3|\*|
# |2|\*|
# |1|\*|
# |0|Exit loop|

# Now let's write a program to print the first 20 even numbers (2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40):

# In[ ]:




# ## Looping Transactions
# Now, let's rewrite our transaction program to read in a variable number of credit card transactions using loops:

# In[4]:

def compute_total_spent_loop(num_transactions):
    '''
    
    '''
    total_spent = 0.0

    i = 0
    while i < num_transactions:
        # read in all num_transactions transactions from the user
        total_spent += get_transaction_price()
        i += 1
    return total_spent

print("Please enter the number of transactions: ", end="")
num = int(input())
total_spent = compute_total_spent_loop(num)
avg_spent_per_transaction = total_spent / num
print("On average, you spend %.2f per credit card transaction" %(avg_spent_per_transaction))


# #### Completing the Guessing Game
# Now that we know how to use `while` loops, let's add the functionality to continue prompting the user to guess a number, *until they guess correctly* (this is our stopping condition of our loop!).

# In[ ]:




# ## TODO
# 1. Read in the textbooks.
# 1. PA3 is due on Wednesday, get 'er done!
# 
# ## Next Lesson
# 1. More on loops.
# 1. Random numbers.
