# Bootcamp class 20 - Planning More Abstractly


![title](https://memegenerator.net/img/instances/68471051.jpg)

# Planning with nested data

Often, nested data structures make planning ahead a little tricky! Today, we'll practice planning ahead to make some nested data structures and functions to work with them

# Demo 1. Planning ahead with a 'shopping cart'

I want to make a data structure here that sets up an online shopping cart so that we can keep track of:
* the items in my cart
* the price of each item
* the quantity of each item

## Outlining 

If I were to make an online of the data structure, it might look something like this:


* item1
    * item1 name
    * item1 price
    * item1 quantity
* item2
    * item2 name
    * item2 price
    * item2 quantity    
    

## Outline -- > code

Okay so now that we have the outline we can start to see what the nested data structure would look like. Let's try filling this in with some sample code. We could imagine our cart as either being a *list with nested dictionaries inside* or a *dictionary with nested dictionaries inside*

### List version

```python
cart1 = [{'name':'banana bunch', 'price': 0.80, 'quantity':2},
        {'name':'salmon steak', 'price': 6.89, 'quantity':3}]
```

### Dictionary version

```python
cart2 = {'banana bunch':{'price': 0.80, 'quantity':2},
        'salmon steak':{'price': 6.89, 'quantity':3}}
```

So, with these we store much of the same data, but in slightly different ways. Either way, our planning of how we want the data to be organized beforehand helps us set this up!

# Demo 2. Planning ahead with a shopping cart function

## Getting the total price -- list version

Let's make a function to get the total price of our shopping cart. For the list version, we could write out pseudocode like this

```python
# function takes 1 argument -- a shopping cart
def get_total(cart):
    pass
	# initialize total price to 0

	# loop through the list of items (for each item in the cart)
		# multiply the price of the item by the quantity and add to the total price

	# return the total price
```

Then we can add in the python code to match our pseudocode:

```python
# function takes 1 argument -- a shopping cart
def get_total(cart):
	# initialize total price to 0
	total_price = 0
	# loop through the list of items (for each item in the cart)
	for item in cart:
		# multiply the price of the item by the quantity and add to the total price
		total_price+= item['price']*item['quantity']
	# return the total price
	return total_price

# call the function on our cart
print(get_total(cart1))
```

Great! Now we can get the total price of our shopping cart


```console
22.27
```

## Getting the total price -- dictionary version

Let's say we had set up the dictionary version of our cart though. How could we get the total price there?
* It might be a little more tricky, but it is possible too! Let's plan out this function with pseudocode

```python
# function takes 1 argument -- a shopping cart (dictionary)
def get_total(cart):
	pass
	# initialize total price to 0

	# get the keys of all items in the dictionary

	# convert the keys to a list

	# loop through the list of keys (for each item in the cart)
		# multiply the price of the item by the quantity and add to the total price

	# return the total price
```

This one is a bit longer because we are basically getting all the keys in the dictionary and converting them to a list so we can iterate through the dictionary items. Now we can fill in the python code.

```python
# function takes 1 argument -- a shopping cart (dictionary)
def get_total(cart):
	# initialize total price to 0
	total_price = 0

	# get the keys of all items in the dictionary
	all_items = cart.keys()

	# convert the keys to a list
	item_list = list(all_items)

	# loop through the list of keys (for each item in the cart)
	for item in item_list:
		# multiply the price of the item by the quantity and add to the total price
		total_price+= cart[item]['price']*cart[item]['quantity']

	# return the total price
	return total_price


print(get_total(cart2))
```

We can see that we get the same answer here too

```console
22.27
```

# Overview

This lesson is *pretty* similar to the lesson from last class (and the challenge is too), except that we'll be asking you to work with nested data structures and think a little more abstractly about how to work with them:
* how to add new items
* how to update existing items

Pseudocode is hard! But this type of planning will really help us figure out how to 'put together the pieces' and take on projects that are larger in scope.
