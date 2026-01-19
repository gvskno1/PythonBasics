import sys
import keyword 
import operator 
from datetime import datetime 
import os 
#==================Keywords===========
# print (keyword.kwlist)

# print (len(keyword.kwlist))

"""
#================Identifiers=========================

1var =10 #Identifier can't start with a digit 
#error : 1var =10 #Identifier can't start with a digit 

val12@ = 35 # Identifier can't use special symbols 
#error: 1var =10 #Identifier can't start with a digit 
# #SyntaxError: invalid decimal literal

import = 125 #keywords cant be used as identifiers
#error: SyntaxError: invalid syntax


val2 =10 #1. Correct way of defining identifiers
val_ = 99 #2. Correct way of defining identifiers. 


#====================Comments=========================
# Comments can be used to explain the code for more readability

# Single line comment 
val1 = 10

#Multiple 
#line 
#comment 
val1 = 10

'''
Multiple 
line 
comment 
'''
val1 = 10


val1 = 10

"""
#====================Statements=================================
#Instructions that a python interpreter can execute

p = 20 #Creates an integer object with value 20 and assigns the variable p to p
q = 20 # Create new reference q which will point to value 20. p & q will be pointing to 20
r = q # variable r will also point to the same location where p & q are pointin
#p storage Address
print(p) #OP: 20
print(type(p))# <class 'int'>
print (hex(id(p)))#0x1032c2578

#q storage Address
print(q)  #OP: 20
print(type(q)) # <class 'int'>
print (hex(id(q))) #0x1032c2578


#r storage address 
print(r)  #OP: 20
print(type(r)) # <class 'int'>
print (hex(id(r))) #0x1032c2578


