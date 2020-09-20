# Bootcamp 1

**First, have students make a folder called `bootcamp_scripts` in the `class_scripts` folder in their `jtc_class_code` github repo (`.../jtc_class_code/class_scripts/bootcamp_scripts`).**

* We can use this folder over the rest of the bootcamp for stroring practice scripts made in lessons


** Tell students this is day 1 of Python Bootcamp and explain lesson outline**

Today is our first class of Python Bootcamp material! By the end of the lesson, you'll:

1. Be able to write python scripts that output or `print` things
2. Be able to include comments in your python scripts
3. Feel comfortable assigning and updating variables
4. Feel comfortable working with the Integer data type
5. Feel comfortable working with the Float data type


## 1. Print statements

* Demonstrate what printing is by printing a string in a new script called `print_exercise.py` in the `bootcamp_scripts` folder

```python
print('hi, this is your computer speaking')
```

### Printing requires parenthesis!

* Show what happens if you don't use parenthesis in the print statement -- explain the error

```python
print 'hi, this is your computer speaking'
```

### Printing multiple things

Show students that

* python scripts execute line by line
* print statements on multiple lines will print out in order


```python
print('hi, this is your computer speaking')
print('i can run a lot of python code')
```


* you can't have multiple print statements on the same line


```python
print('hi, this is your computer speaking') print('i can run a lot of python code')
```


## 2. Comments

* Show students how to add comments to code
* Explain some good commenting practice
* Show how commented out code does not evaluate

```python
# this line of code prints out a first line of text
print('hi, this is your computer speaking')

# this line of code prints out a second line of text
print('i can run a lot of python code')
```

#### Commenting out big chunks

* Show how to toggle commenting out big chunks of code

## 3. Assigning & updating variables

To learn about variables, let's make a new script in the `bootcamp_scripts` folder called `variables.py`

#### What are variables?

* We can explain what variables are using the box metaphor.
  * "Variables are boxes -- we can refer to the box by name and select which box we want, and each box also can have stuff stored inside it"

#### Assigning variables

* Explain that variable assignment always uses **a single equals sign**: `=`
* assign a string variable and run the script with no other code -- ask students why they get nothing back

```python
firstname = 'Paul'
```

* show that the assigned string variable can be printed by adding a print statement
  * Back to the box metaphor, this is like looking at the contents of the box
```python
# assign the variable
firstname = 'Paul'

# print out the contents of the variable
print(firstname)
```

#### Variable naming conventions

There are a few rules for naming variables when we assign them:

 * They can't start with numbers
 * They can't have spaces in them
 * Rules aside, one very useful convention is to use all lowercase letters in variable naming, and to separate each word with an underscore (`_`).
    * For example: `my_new_variable` or `birthday_year`
    
    
#### Updating variables

* show students that an existing variable can be reassigned
* explain that this 'overwrites' the previous value

```python
variable_a = 'this is variable a'
print(variable_a)
variable_a = 'this is variable b'
print(variable_a)
```

#### Variable errors

* Show what happens if you misspell a variable name and try to print a variable that doesn't exist

```python
# assign the variable
first_name = 'Paul'

# print out the contents of the variable (but we misspelled it)
print(firstname)
```

## 4. Integers

**For this section and the next, have students make a new script in `bootcamp_scripts` called `integers_floats.py`**

#### Primitive data types

* Give brief overview that there are 4 primitive data types

#### What are integers?

* Whole numbers

#### Math in python / working with integers

Show students these common math operations in python with print statements using integers

* Addition: `+`
* Subtraction `-`
* Multiplication `*`
* Division `/`
* Exponents `**` (i.e. `5**2` means 5 squared (to the 2nd power), or `3**9` means 3 to the 9th power)


```python
print(1+3)
print(1*3)
print(1-3)
```


#### Integers as variables

* Show that integers can be assigned to variables, and you can do math with the variables

```python
# assign a positive integer to a variable
positive_number = 10

# assign a negative integer to a variable
negative_number = -5

# add the values of the two variables and print
print(positive_number + negative_number)
```


## 5. Floats

* Floats, unlike integers, **do have decimal points**
* Show some math operations with floats too
* Show that some operations on integers (divison) return a float back

```python
print(1.1+3.1)
print(1.5*2)
print(1-3.736)
```


#### Order of operations

* Explain briefly that python math follows order of operations
* Show that parentheses matter

```python
var_a = 2+3*4
var_b = (2+3)*4
print(var_a)
print(var_b)
```

### Type conversion

* Show using `float()` to convert to float and `int()` to convert to integer
* Explain that you can lose info when going from float to integer


## Overview

So, what have we learned during this lesson?
* How to get python to print out things to the command line when you run scripts
* How to document code with comments that will not be run
* How to make variables, reference them by name, and assign/update/print their contents
* How to work with the two numeric basic data types: integers and floats
* All of these skills will be super important for progamming in python, and most will carry over to other coding languages too!
