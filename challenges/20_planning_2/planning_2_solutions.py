'''
Planning challenge 2!

For each piece here, write out the pseudocode as comments FIRST, then write your code!
'''


'''
1. Shipping

You are building a system to handle shipping orders. Each order should be a dictionary that has 3 pieces of information:
-destination (string) (for the purposes of this challenge this can be any place, no need to make a full address)
-date_shipped (string)
-weight (float) (how many pounds the package is)

Assign 3 separate orders to 3 separate variables
'''
print('\nPART 1')

# Make each order as a dictionary with 3 key/value pairs for each attribute
order1 = {'destination':'Philadelphia', 'date_shipped': '10/20/20', 'weight': 20.4}
order2 = {'destination':'Queens', 'date_shipped': '10/22/20', 'weight': 0.1}
order3 = {'destination':'Los Angeles', 'date_shipped': '10/28/20', 'weight': 357.8}



'''
2. Building the database

Now, let's put the orders all into a database togther (all the orders are storedin 1 variable). 

Your database can either be a dictionary or a list. 

Print out the database to make sure all the info is in there. 

'''
print('\nPART 2')


# List solution

# put each of the three orders in a list and assign to a new variable to be the databse
order_database_list = [order1, order2, order3]

# print out the database
print(order_database_list)


# Dictionary solution
# One way to do this it to give each order a random 6-digit ID
# Put each of the order variables in the dictionary as values, and give a 6-digit int as the key
order_database_dictionary = {632817:order1, 192830: order2, 920183: order3}
print(order_database_dictionary)

'''
3. Define a function called add_order() that adds one more order to your database, and make sure it works!
Any new orders should be in the same format as your existing ones. 
'''
print('\nPART 3')

# Make some new orders
order4 = {'destination':'Atlanta', 'date_shipped': '10/29/20', 'weight': 2.1}
order5 = {'destination':'Pittsburgh', 'date_shipped': '10/30/20', 'weight': 3.3}


# LIST SOLUTION
# define the function to take in 2 arguments, the database (list) and the order (dict)
def add_order_list(database, order):
	# inside the function, append the order dict to the end of the list
	database.append(order)

# test out calling the functino to add order4 and order5
add_order_list(order_database_list, order4)
add_order_list(order_database_list, order5)

# check database by printing it out
print(order_database_list)


# DICTIONARY SOLUTION
# Once nice thing with dictionaries would be to create a random ID for each order
# Not strictly necessary, but one solution for managing the keys

# import numpy 
import numpy as np

# define the function to take in 2 arguments, the database (dict) and the order (dict)
def add_order_dict(database, order):
	# generate a random 6-digit int id between 100000 and 999999 using numpy
	id = int(np.random.randint(low = 100000, high = 999999, size = 1))

	# add a new key/value pair to the database dict, where id is the key and order is the value
	database[id] = order

# test out calling the functino to add order4 and order5
add_order_dict(order_database_dictionary, order4)
add_order_dict(order_database_dictionary, order5)

# check database by printing it out
print(order_database_dictionary)


'''
4. Define a function called complete_order() to mark a specific order in your database complete

This means that it should add a new key/value pair called 'complete' to a specific order, and set the value to True

Test this out and print out your database to make sure it works!

HINT: Think about how your choice of list/dictionary in number 2 informs how someone would reference an order in the database
'''
print('\nPART 4')


# LIST SOLUTION
# Since the database is a list, referencing orders by their position in the list (index) might be best:
# define the function to take 2 arguments, the database (list) and the INDEX corresponding to the order we want to mark as complete
def complete_order_list(database, order_index):
	# go to the corresponding order in the list, then make a key called 'complete' and set it to True
	database[order_index]['complete'] = True

# test it out on indices 2/4 of the list (3rd/5th orders)
complete_order_list(order_database_list, 2)
complete_order_list(order_database_list, 4)

# print out to check it
print(order_database_list)


# DICTIONARY SOLUTION
# Since the database is a dictionary, referencing orders by the keys makes the most sense 
# Since the keys are 6-digit integers, here we'll reference the items in the dict by their 6-digit integer keys

# define the function to take 2 arguments, the database (dict) and the KEY (6-digit int) corresponding to the order we want to mark as complete
def complete_order_dict(database, order_key):
	# select the dictionary nested within the database with the corresponding order key, and make a key 'complete', and set it to True
	database[order_key]['complete'] = True


# complete orders, referencing them by their 6-digit id keys
complete_order_dict(order_database_dictionary, 192830)
complete_order_dict(order_database_dictionary, 920183)

# print out to check it
print(order_database_dictionary)
