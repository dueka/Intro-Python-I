# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:18:28 2020

@author: USER
"""
# Create a list
Ozark = ['Marty', 'Byrde', 'Rigged', 'Money']

#  Access list items
print(Ozark[1])

# Chnage the value of a list item
Ozark[1] = 'Nancy'

# Loop through a list
for i in Ozark:
    print(i)

# Check if a List Item Exists
for Marty in Ozark:
    print(Marty)
    
# Get the length of a list 
print(len(Ozark))

# Add an item to the end of a list
Ozark.insert(5,'Launder')
print(Ozark)

# Add an item at a specified index
Ozark.insert(3,'Email')
print(Ozark)

# Remove an item
Ozark.pop()
print(Ozark)

# Remove an item at a specified index
del Ozark[1]
print(Ozark)

# Empty a list
Ozark1 = Ozark
del Ozark[:]
print(Ozark1) 

# Use the list() construcotor to make a list
print(list())