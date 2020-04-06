# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 22:35:16 2020

@author: USER
"""
# Create a set
DueSet = {'Aaron', 'May', 'Lane'}

# Loop through a set
# for val in DueSet:
#     print(val)
    
# Check if Item exisets
if "Aaron" in DueSet:
  print('Aaron is good')
        
# Add an item to a set
DueSet.add('Word')
print(DueSet)

# Add multiple items to a set
DueSet.update(['Sampha', 'Gold'])
print(DueSet)

# Get the length of a set
print(len(DueSet))

# Remove an item in a set
DueSet.pop()
print(DueSet)

# Remove the last item in a set using the discard() 
DueSet.discard('Aaron')
print(DueSet)

# Remove the last item in a set using the pop() method
print(DueSet.clear())

# Delete a set
print(DueSet.remove())