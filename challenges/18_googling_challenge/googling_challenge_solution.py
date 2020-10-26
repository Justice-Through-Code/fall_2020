'''
GOOGLING CHALLENGE! 

Today, we'll ask you to write a bunch of small pieces of code.

Unlike previous ones, we have NOT showed you the exact code you'll need to answer the questions.

So, you'll want to search out answers on the web, make sure you understand them, then try them out until they work!

For each question, you should also COPY THE LINK TO THE RESOURCE WHERE YOU FOUND THE SOLUTION in so that you can use it in the future too
'''


# 1A. Sort the below list in alphabetical order
print('QUESTION 1\n')
my_friends = ['Yusuf', 'Aedan', 'Mia', 'Ash', 'Paul', 'Aeshna', 'Aryn', 'Rob']

# Using list sort method as in https://www.w3schools.com/python/ref_list_sort.asp
# Sorts list in place
my_friends.sort()


print(my_friends)

# 1B. Comment your code in 1A to convince yourself you understand how it works


# 2A. Get all the keys from the below dictionary, then print them out:
# Hint: there is a single command that can do this
print('QUESTION 2\n')

my_account = {'username': 'pbloom',
			  'password': 'python3.7',
			  'balance': 101.8,
			  'transaction_dates': ['9/18/2020', '9/20/2020', '10/5/2020'],
			  'verified': True}

# use the .keys() dict method to get the keys
# https://www.geeksforgeeks.org/python-dictionary-keys-method/
my_account_keys = my_account.keys()

# print them out all at once
print(my_account_keys)

# check the data type, interesting that is is <class 'dict_keys'>
print(type(my_account_keys))

# the keys can be iterated over with a loop!
for i in my_account_keys:
	print(i)

# 2B. Comment your code in 2A to convince yourself you understand how it works



# 3A Count how many times the word 'wood' appears in the following string:
# Hint: there is a single command that can do this
print('QUESTION 3\n')
my_string = 'how much wood could a woodchuck chuck if a woodchuck could chuck wood?'

# Use the .count() string method 
# Resource for this: https://www.programiz.com/python-programming/methods/string/count
print(my_string.count('wood'))


# 3B. Comment your code in 3A to convince yourself you understand how it works



# 4A Count how many times the string 'banana' appears in the following list:
# Hint: there is a way to do this with one line of code
print('QUESTION 4\n')
my_list = ['apple', 'banana', 'banana', 'cherry', 'mango', 'banana', 'banana', 'banana']

# From W3 schools https://www.w3schools.com/python/ref_list_count.asp
# List method for counting items
print(my_list.count('banana'))



# 4B. Comment your code in 4A to convince yourself you understand how it works



# 5A Print out all of the unique strings in my_list
# Hint: there is a way to do this with one line of code
print('QUESTION 5\n')


# Using set() as option 1 from here: https://www.freecodecamp.org/news/python-unique-list-how-to-get-all-the-unique-values-in-a-list-or-array/
unique_list_items = set(my_list)
print(unique_list_items)

# Notice: the type is <class 'set'> 
print(type(unique_list_items))

# But we can convert it back to a list
unique_list_items = list(unique_list_items)
print(unique_list_items)
print(type(unique_list_items))

# 5B. Comment your code in 5A to convince yourself you understand how it works


# 6A. Import numpy, then use it to generate a random number between 0-1
print('QUESTION 6\n')

# One solution
# Using https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.random.rand.html#numpy.random.rand
from numpy import random

# the random.rand() function from numpy
my_random_number = random.rand(1)
print(my_random_number)


# Another solution
# https://www.kite.com/python/examples/186/numpy-construct-an-array-of-random-values-between-0-and-1
import numpy as np
my_random_number_2 = np.random.rand(1)
print(my_random_number_2)

# 6B. Comment your code in 6A to convince yourself you understand how it works


