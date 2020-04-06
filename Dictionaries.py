# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 17:41:08 2020

@author: USER
"""

# Create a dictionary
lang2man = dict()
lang2man = {'pete': 'rock', 'Ini': 'Life', 'Hip' : 'Hop'}
print(lang2man)

# Access the items of a dictionary
print(lang2man['pete'])

# Change the value of a specific item in a dictionary
lang2man['Ini'] = 'Roddy'
print(lang2man)

# Print all key names in a dictionary
print(lang2man.keys())

# Print all values in a dictionary, one by one
print(lang2man.values())

# Loop through both keys and values, by using the items() function
print(lang2man.items())

# Check if a key exists
print (lang2man.get('pete'))

# Get the length of a dictionary
print(lang2man.__len__())

# Add an item to a dictionary
lang2man = {'Chainz': 'chinaza'}
print(lang2man)

print(lang2man.pop('pete'))