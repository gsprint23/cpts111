
# coding: utf-8

# # [CptS 111 Introduction to Algorithmic Problem Solving](http://piazza.com/wsu/spring2017/cpts111/home)
# [Washington State University](https://wsu.edu)
# 
# [Gina Sprint](http://eecs.wsu.edu/~gsprint/)
# # L9-2 Files
# 
# Learner objectives for this lesson
# * Understand file system paths
# * Open, read, write, and close files
# * Use `while` and `for` loops to read in and write data to files

# ## Storing Data
# Many applications require storing and retrieving data outside of a program. Think of the many different applications you regularly use, do they utilize information that has been saved in some way?
# * PC: Your operating system stores all of your settings, files, and machine state for you.
# * Banks: Every customer's transaction history is stored in massive databases in data warehouses. When you make a debit purchase, your account balance is retrieved from one of these servers to make sure you have enough money for your transaction. (`if balance >= purchase`)
# * Games: Your progress in a game is stored in a file so that when you turn off your console (or laptop), your progress isn't lost.
# <img src="https://s-media-cache-ak0.pinimg.com/564x/9d/d4/4f/9dd44f90ec89ca27594bc9036f16ab40.jpg" width=350>
# * Search history: Websites save your recent searches in order to try and learn about your preferences and better predict what you will search for in the future.
# * Authentication: When you authorize an app to "keep you logged in", a token is being persistently stored by the app as your authentication so you don't have to type your username and password in each time.
# * Obviously many more.
# 
# ## Text Files
# A simple way to store data is in a *text file*, such as this simple text file, [transactions.txt](https://raw.githubusercontent.com/gsprint23/cpts111/master/lessons/files/transactions.txt), that stores an individual's credit card transaction history. Each line in the file represents a transaction price.
# 
# To process data in a file, we typically take the following approach:
# 1. Open the file
# 1. Process the file
#     * Read data (doesn't modify the file) or
#     * Write data (overwrite existing file) or
#     * Append data (retains existing information and adds new data)
# 1. Close the file
# 
# ### Opening a File
# Before we can read from a file or write to a file, we first need to open the file and get a file object (AKA handle). We do this with the built-in function `open()`:

# In[1]:

# in_file is our variable connecting our program to transactions.txt
# transactions.txt is a file I have in the *same folder* as this running Python file
in_file = open("transactions.txt", "r")


# #### File Modes
# The first argument to `open()` is a string representing the path to the file and the second argument is the file opening *mode*: 
# 1. "r" for reading
#     1. File must exist or you will get an error
# 1. "w" for writing
#     1. If the file does not exist, it is created
#     1. If the file does exist, it is cleared!
# 1. "a" is for appending
#     1. If the file does not exist, it is created
#     1. If the file does exist, new data written to the file is added at the end of the file
# 
# You can read more about modes [here](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files). 
# 
# `open()` returns an object that represents the connection between our program and transactions.txt.
# 
# #### Paths
# The directory (or folder) where your Python script is running is called the *current directory*. When you open a file, Python looks for it in the current directory. 
# 
# If a file you want to open is in a directory other than the current directory, you will have to specify its path. The location of a file is represented by its path, the sequence of folders that the file is stored in, plus the file's name. There are two ways to specify a path:
# 1. Relative path: a path to a file or directory relative to the current directory. For example: "files\transactions.txt" refers to a file ("transactions.txt") in a directory ("files") in the current directory.
# 1. Absolute path: a path to a file or directory specified by its exact location on your file system. For example: "C:\Users\gsprint\cpts111\lessons\files\transactions.txt" refers to a file ("transactions.txt") in the folder "C:\Users\gsprint\cpts111\lessons\files" on my C:\ drive.
# 
# Note: On a windows machine, folders and file names in a path are separated by backslashes "\". We know the backslash has a special purpose in Python, to escape certain characters, such as a newline "\n"; therefore, you will have to escape a backslash: "`\\`" in your path to a file: `"files\\transactions.txt"`. Alternatively, you can specify your path as a raw string: `r"files\transactions.txt"`. On a Unix-based machine (e.g. Mac, Linux distributions), the forward slash "/" is used in paths and you don't have to worry about this issue.
# 
# ### Closing a File
# When we are done with a file, we should close it with `close()`:

# In[7]:

in_file.close()


# ### Processing a File
# Once a file is open, we want to process the data inside the file (reading) or save data to file (writing). Consider the example [transactions.txt](https://raw.githubusercontent.com/gsprint23/cpts111/master/lessons/files/transactions.txt) we opened earlier.
# 
# #### Reading from a File
# We will use the `readline()` function to read in a *single* line in the file (in transactions.txt this is the purchase price as a **string including the newline character \n**):

# In[11]:

transaction = in_file.readline()
# note the newline printed!! repr() shows non-printable characters like \n
print(transaction, repr(transaction), type(transaction))
transaction = float(transaction)
print(transaction, type(transaction))


# #### Writing to a File
# Now, let's use use the `write()` function to write the transaction price we just read in to an output file called single_transaction.txt:

# In[12]:

# creates the file if it does not exist
# overwrites the file contents if it does exist
out_file = open("single_transaction.txt", "w")
# save the value of transaction as string
out_file.write("%.2f" %(transaction))

# close file because we are done with out_file
out_file.close()


# ### Example Problem
# On average, how much money do I spend per credit card transaction?
# 
# Algorithm:
# 1. For each transaction
#     1. Read in the purchase price from file
#     1. Accumulate the total money spent so far
# 1. Divide total money spent by total number of transactions
# 1. Write the average transaction to file

# In[27]:

def read_transaction_price(in_file):
    '''
    
    '''
    # readline() returns a string, including the newline character
    price = in_file.readline()
    # we need to convert the string returned by readline() to a numeric value
    return float(price)

def compute_total_spent():
    '''
    
    '''
    total_spent = 0.0
    
    in_file = open("transactions.txt", "r")

    # read in all 5 transactions in the file
    for i in range(5):
        total_spent += read_transaction_price(in_file)
    
    # close the file before in_file goes out of scope
    in_file.close()
    
    return total_spent

total_spent = compute_total_spent()

avg_spent_per_transaction = total_spent / 5.0

out_file = open("avg_transaction.txt", "w")
out_file.write("On average, you spend %.2f per transaction" %(avg_spent_per_transaction))
out_file.close()


# ## File Reading
# ### `for` Loops
# Let's rewrite our transaction code to read in as many transactions as there are in the file (instead of the hard-coded 5). Using a `for` loop, `<sequence>` will be all of the lines in the input file, which we can get with a call to `in_file.readlines()`. Our `for` loop will walk through each line one at time with a loop control variable called `line`.

# In[19]:

def compute_avg_spent():
    '''
    
    '''
    # accumulator variable
    total_spent = 0.0
    # count the transactions
    num_transactions = 0

    # the input file contains lines that we will iterate through as our items
    for line in in_file.readlines():
        print(line)
        total_spent += float(line)
        num_transactions += 1
    
    # close the file before in_file goes out of scope
    in_file.close()
    
    return total_spent / num_transactions

avg_spent_per_transaction = compute_avg_spent()

print("On average, you spend %.2f per transaction" %(avg_spent_per_transaction))


# ### `while` Loops 
# Let's rewrite our transaction processing code to use a `while` loop. `readline()` will return an empty string when the end of the file is reached. This can be used in our Boolean condition:

# In[1]:

def compute_avg_spent():
    '''
    
    '''
    # accumulator variable
    total_spent = 0.0
    # count the transactions
    num_transactions = 0
    
    in_file = open("transactions.txt", "r")

    # read the first line in the file
    spent = in_file.readline()
    # test if this line is the empty string, meaning the end of file has been reached
    while spent != "":
        # not end of file, process this transaction
        print(spent)
        total_spent += float(spent)
        num_transactions += 1
        # progress toward Boolean condition being False here is progress through the file
        spent = in_file.readline()
    
    # close the file before in_file goes out of scope
    in_file.close()
    
    return total_spent / num_transactions

avg_spent_per_transaction = compute_avg_spent()

print("On average, you spend %.2f per transaction" %(avg_spent_per_transaction))


# ## MA13 Practice Problem
# On a blank sheet of paper, write the following:
# 1. Your full name
# 1. Your TA name
# 1. MA #13
# 
# Individually, solve the following problems as if they were exam questions. Each student needs to turn in their own paper to get credit for MA13.
# 1. (2 pts) Evaluate to `True` or `False`:
#     1. `7 % 2 == 3 or 12 // 10 == 2.2`
#     1. `9 / 2 > 4 or -3 >= 0 and -5`
# 1. (1 pt) Besides their name, what are the differences between a `while` loop and a `for` loop?
# 1. (3 pts) Construct a `while` loop that displays numbers in the range [3, 30] inclusive that are multiples of 3. 
# 1. (4 pts) Construct a `for` loop that sums 10 randomly generated numbers in the range [4, 8] inclusive. 

# ## TODO
# 1. Read the chapters on files in the optional textbook.
# 1. Keep working on PA4.
# 1. Have a great spring break!
# 
# ## Next Lesson
# 1. More practice with File I/O.
