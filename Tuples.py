# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 21:54:07 2020

@author: USER
"""
# Create a tuple
due = ('rob', 'props', 'comeon', 'about')
print(due)

# Access Tuple items
print(due.__contains__('rob'))

# Change tuple values
lst = list(due)
lst[0] = 'sir'
due = tuple(lst)
print(due)

# Iterate through a tuple
for var in due:
    print(due.index(var), var)
    
# Check if a tuple item exists
print(due.__contains__('rob'))

# Get the length of a tuple
print(due.__len__())

# Delete a tuple
n=2
due = due[ : n] + due[n+1 :]
print(due)