
# coding: utf-8

# # [CptS 111 Introduction to Algorithmic Problem Solving](http://piazza.com/wsu/spring2017/cpts111/home)
# [Washington State University](https://wsu.edu)
# 
# [Gina Sprint](http://eecs.wsu.edu/~gsprint/)
# # L14-1 Binary
# 
# Learner objectives for this lesson
# * Review the decimal number system
# * Learn the binary number system
# * By hand, convert binary to/from decimal
# * Implement algorithms to convert binary to/from decimal

# ## Review of Decimal
# The decimal (base 10) number system we use is a *positional* number system using the digits 0 through 9 (another example of zero-basing!). Each digit in a decimal number, such as 346, is in a position representing a power of 10.
# 
# |...|thousands|hundreds|tens|ones|
# |-|-|-|-|
# |...|1000|100|10|1|
# |...|$10^3$|$10^2$|$10^1$|$10^0$|
# |...|0|3|4|6|
# 
# A decimal number is the sum of the digits multiplied by their positional power of 10. Continuing with the 346 example:
# 
# |$10^2$|$10^1$|$10^0$|
# |-|-|-|
# |3|4|6|
# 
# $3 * 10^2 + 4 * 10^1 + 6 * 10^0 = 3 * 100 + 4 * 10 + 6 * 1 = 300 + 40 + 6 = 346$

# ## Binary
# Binary, like decimal, is a positional number system. Binary uses only the digits 0 and 1 though! Each digit in a binary number, such as $1011_{2}$ (The $_{2}$ denotes this number is in base 2, not base 10), is in a position representing a power of 2.
# 
# |...|eights|fours|twos|ones|
# |-|-|-|-|
# |...|8|4|2|1|
# |...|$2^3$|$2^2$|$2^1$|$2^0$|
# |...|1|0|1|1|
# 
# A binary number is the sum of the digits multiplied by their positional power of 2. Continuing with the $1011_{2}$ example:
# 
# |$2^3$|$2^2$|$2^1$|$2^0$|
# |-|-|-|-|
# |1|0|1|1|
# 
# $1 * 2^3 + 0 * 2^2 + 1 * 2^1 + 1 * 2^0 = 1 * 8 + 0 * 4 + 1 * 2 + 1 * 1 = 8 + 0 + 2 + 1 = 11$
# 
# For reference, let's review the first couple powers of two:
# 1. $2^0 = 1$
# 1. $2^1 = 2$
# 1. $2^2 = 4$
# 1. $2^3 = 8$
# 1. $2^4 = 16$
# 1. $2^5 = 32$
# 1. $2^6 = 64$
# 1. $2^7 = 128$
# 1. $2^8 = 256$
# 1. $2^9 = 512$
# 1. $2^{10} = 1024$
# 1. $2^{11} = 2048$
# 1. $2^{12} = 4096$
# 
# Where have you seen these numbers before? One place you have seen them before is hard drive storage size! Hard drives usually come in sizes that are powers of two, such as 256 gigabyte (Gb), 512 gigabyte (Gb), or 1 terabyte (Tb) (1 Tb = 1024 Gb). 
# 
# Note that 1 Gb = $2^{30} = 1,073,741,824$ bytes, 1 Tb = $2^{30} + 2^{10}$ = $2^{40} = 1,099,511,627,776$ bytes, and 1 byte = $2^{3}$ = 8 bits. If this is interesting to you, consider taking CptS 260, Computer Organization and Architecture!

# ## Binary to Decimal
# To convert a binary number to decimal, perform the above summation process. An algorithm to do this:
# 1. For each bit in the binary number
# 1. If the bit is a 1
#     1. Add $2^{i}$ to the accumulated sum, where $i$ is the position of the bit
# 
# ### Example: Convert 1010101 to decimal
# $1 * 2^6 + 0 * 2^5 + 1 * 2^4 + 0 * 2^3 + 1 * 2^2 + 0 * 2^1 + 1 * 2^0 = 1 * 64 + 0 * 32 + 1 * 16 + 0 * 8 + 1 * 4 + 0 * 2 + 1 * 1 = 64 + 16 + 4 + 1 = 85$
# 
# ### General Example
# Write a function that accepts a string representing a binary number and returns an integer representing the string in decimal. 

# In[9]:

def binary_to_decimal(binary):
    '''
    
    '''
    decimal = 0
    highest_power_two = len(binary) - 1
    
    for i in range(len(binary)):
        digit = int(binary[i])
        decimal += digit * 2 ** (highest_power_two - i)
        
    return decimal

print(binary_to_decimal("1010101"))
    


# ## Decimal to Binary
# This is the more tricky conversion! To convert a decimal number to binary, we follow the algorithm:
# 1. Identify the largest power of 2 in the decimal number, $2^N$
# 1. For each power of 2 $2^N, 2^{N - 1}, ..., 2 ^{0}$
# 1. If the power of 2 goes into the number evenly
#     1. place a 1 at that power's position
#     1. subtract the power of 2 from the number 
# 1. Else
#     1. Place a 0 in that power's position
# 
# ### Example: Convert 94 to binary.
# Highest power of 2 in 94 is $2^6 = 64$
# Algorithm:
# * $2^6 = 64$ go into 94 evenly?
#     * YES: place a 1 on the $2^6$ position
#     * Binary number so far: 1??????
#     * $94 - 2^6 = 94 - 64 = 30$
# * $2^5 = 32$ go into 30 evenly?
#     * NO: place a 0 on the $2^5$ position
#     * Binary number so far: 10?????
# * $2^4 = 16$ go into 30 evenly?
#     * YES: place a 1 on the $2^4$ position
#     * Binary number so far: 101????
#     * $30 - 2^4 = 30 - 16 = 14$
# * $2^3 = 8$ go into 14 evenly?
#     * YES: place a 1 on the $2^3$ position
#     * Binary number so far: 1011???
#     * $14 - 2^3 = 14 - 8 = 6$
# * $2^2 = 4$ go into 6 evenly?
#     * YES: place a 1 on the $2^2$ position
#     * Binary number so far: 10111??
#     * $6 - 2^2 = 6 - 4 = 2$
# * $2^1 = 2$ go into 2 evenly?
#     * YES: place a 1 on the $2^1$ position
#     * Binary number so far: 101111?
#     * $2 - 2^1 = 2 - 2 = 0$
# * $2^0 = 1$ go into 0 evenly?
#     * NO: place a 0 on the $2^0$ position
#     * Binary number so far: 1011110
# 94 in binary: 1011110
# 
# ### General Example
# Write a function that accepts an integer and returns a string representing the integer in binary.

# In[10]:

import math

def decimal_to_binary(decimal):
    '''
    
    '''
    binary = ""
    highest_power_two = int(math.log(decimal, 2)) # compute highest_power_two with log base 2(decimal)
    
    for N in range(highest_power_two, -1, -1):
        power_two = 2 ** N
        if decimal // power_two > 0: # check is power_two goes into the number evenly
            binary += "1"
            decimal -= power_two
        else:
            binary += "0"
    
    return binary

print(decimal_to_binary(94))


# ## TODO
# 1. Work on PA6.
# 1. Read Chapters 10, 11, and 12.
# 
# ## Next Lesson
# We cover dictionaries, a quite powerful data structure!
