
# coding: utf-8

# # [CptS 111 Introduction to Algorithmic Problem Solving](http://piazza.com/wsu/spring2017/cpts111/home)
# [Washington State University](https://wsu.edu)
# 
# [Gina Sprint](http://eecs.wsu.edu/~gsprint/)
# # L10-1 More File I/O and Practice
# 
# Learner objectives for this lesson
# * Understand positioning in a file
# * Apply `strip()` to strings
# * Use the `file` keyword of `print()`

# ## The File "Cursor"
# When you open a file for reading ("r" mode), the cursor marking the current position at which to read from starts at the beginning of the file (position 0). As `readlines()` is called, the cursor moves through the file. To move the cursor back to the beginning of the file, you can either close the file and re-open it for reading.

# In[1]:

in_file = open("transactions.txt", "r")

print("File cursor is at the beginning of the file.")
for line in in_file.readlines():
    print(line)

in_file.close()
in_file = open("transactions.txt", "r")

print("File cursor is at the beginning of the file.")
transaction = in_file.readline()
print(transaction)


# ## Removing Leading and Trailing Whitespace Characters
# We can remove whitespace characters (like `\n`) with a call to a string function `strip()`:

# In[9]:

in_file = open("transactions.txt", "r")

# read data from the file advances the cursor by a certain number of bytes, 
# depending on the number of characters in the line
transaction = in_file.readline()

# repr() displays all characters in a string. we use it see the newline character as \n
print("First line: ", repr(transaction))
in_file.close()
print("First line stripping leading/trailing whitespace characters: ", repr(transaction.strip()))


# ## Revisiting `print()`
# There are several ways to print strings with the `print()` function. It is helpful to be aware of other printing approaches, especially when you want to format output a particular way. Check out these different ways to print:

# In[8]:

# format string and placeholders
print("Integer: %d, Float: %f, Float with 1 decimal: %.1f, String: %s" %(7, 8.4898899, 3.14, ":)"))

# arguments displayed separated by spaces
print(4, 5.5, ":P", 8)
# specifying the delimiter between arguments (a comma and a space)
print("A comma", "separated", "list", sep=", ")

# specifying the string concatenated to the end
print("A string without the added newline character", end="")
print("This sentence runs into the previous", end="!\n")

# https://docs.python.org/3/library/string.html
print("An {} form of placholders {:.1f}. You can also use keywords {name}".format("alternative", 9.99, name="cpts111"))

# alternative way to write to a file using print() instead of write()
outfile = open("out_demo.txt", "w")
print("Writing this output via print()", file=outfile)
outfile.close()


# ## Common Errors when Working with Files
# * Using the wrong file handle to refer to a file
# * Opening a nonexistent file for reading
# * Using a file object whose cursor is at the end of the file
# * Opening a file for reading or writing without the appropriate access rights
# * Opening a file for writing when no disk space is available
# * Opening a file for writing ("w") when the users wants to preserve the previous contents of the file ("w" discards all contents of file)

# ## Practice Problem
# For the following problems, we will need to download a file: [words.txt](http://thinkpython2.com/code/words.txt). This file contains 113,809 official crossword words, one per line. Using words.txt, write a program with the following functionality:
# 1. A function called `open_input_file()` that opens words.txt for reading and returns the file object associated with words.txt
# 1. A function called `close_file()` that accepts the file object as an argument and closes the file
# 1. A function called `first_five_words()` that displays the first 5 words of the file. Display the words one on each line, without an extra newline between the words like:
# ```
# aa
# aah
# aahed
# aahing
# aahs
# ```

# In[ ]:




# ## TODO
# 1. Turn in PA4, it is due tonight
# 1. Start PA5
# 1. Read Section 9.1 and Chapter 14
# 
# ## Next Lesson
# 1. We learn more about Strings
