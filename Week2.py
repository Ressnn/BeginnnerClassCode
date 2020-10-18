# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 10:59:41 2020

@author: Pranav Devarinti
"""


# In[] Comments
"""
This is a multiline comment
"""
# Another kind of comment
# In[] Variable
ba = 1 # Assign to number

# In[]
1 # integer
int("9") #integer call

"Alpha" # String
str(9) # Converts to String

["A","B"] #Lists
list 

True #Booleans
bool
# In[] Number operations
"""
Here are some number operations
+ - addition
- - subtraction
/ - division
* - multiplication
=* multiply left by right and assign to left
.
.
.
** - power

"""

#What would a be?
rt = 9
rt*=1/3
rt+=7
a=rt+rt
print(a)
# In[] String Operations

a = "Alpha"
b = "Bet"

c = a+b
print(c)

#You can index to get a portion of the string
print(c[0:5])
# In[] Booleans

a = True
b = not(a)
print(b)

"""
and - returns true if a and b are true
or - returns true if either a or b are true
xor (^) - returns true if a != b
"""

print(a or b)
print(a and b)
print(a ^ b)
# In[] Casting

a = True

b = int(a)
print(b)

b = str(a)
print(b)

text = "Alpha"
print(list(text)) #Casting text to list splits by letter
# In[] Comparison Operators
"""
a==b | checks if a and b are equal
a>=b | a greater than or equal to b
a<=b | a less than or equal to b
a>b | a greater than b
a<b | a less than b

turn into true boolean if statement
is true and false if statement is false
"""

a = 10
b = 10
print(a==b)
# In[] Check

# Write a multi-line comment below-

"""
This is a multiline comment
"""

# Make a new variable called a and
# Set it to 3
# Make a variable called b
# and set it to a to the power of a
a = 3
b = a**a
print(b)

#Name me 5 data types
"""
boolean
integer
string
tuple
list
float
dictionarys
sets
numpy arrays
user-defined datatypes
"""

#Convert a into a float and add it
#to b **2 

a = "9.81"
b = 10

print(float(a)+b**2)

#Check if a is greater than b-a
a = 10
b = 14
print(a>(b-a))
