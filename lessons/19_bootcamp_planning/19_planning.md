# Bootcamp class 19 - Planning (with pseudocode)

### A game plan for your code

Sooner or later, we're all stumped by complex problems that require some thought and careful planning to solve by coding. We can think of coding as three steps:

- Pseudocoding or a rough plan of the code we will write,
- Writing actual code
- And finally, optimizing or cleaning up the code we wrote.

### What is pseudocode?

It is not a new language. **Pseudocode** is a way of expressing your code in your own words without worrying too much about language syntax. It is tempting to jump into writing code and figuring things out on the way, but pseudocoding helps us:

- Break down a large task into smaller tasks, described in our own words
- Create a blueprint for our code implementation
- Identify steps that might need further research (looking up code solutions on stackoverflow, etc)

Pseudocoding helps us understand the requirements of the program before we spend our efforts in writing complex code.

# Demo 1

Let's take a simple function that calculates the average of numbers in a list

```python
def average(nums):
    pass
```

The keyword `pass` is a placeholder you can use when you have nothing written inside the body of your function. If you run the function as is, nothing happens, which is what we want until we write actual code

### Pseudocoding

```python
def average(nums):
    # sum of nums list
    # divide sum by the number of values in nums list
    # return output
    pass
```

### Writing actual code

```python
def average(nums):
    # sum of nums
    total = sum(nums)
    # divide sum by the number of values in nums list
    average = total/len(nums)
    # return output
    return average
```

### Optimizing code

```python
# optimize code to fit in fewer lines
def average(nums):
    return sum(nums)/len(nums)
```

```python
print(average([2002, 30, 44]))
```

# Demo 2

Using our knowledge of python's block code and indentation, we can structure our pseudocode accordingly.

### Pseudocoding

```python
def should_wear_jacket(temperature):
    # if temperature is less than 65 degrees
        # then yes
    # else
        # then no
    pass
```

### Writing actual code

```python
def should_wear_jacket(temperature):
    if temperature < 65:
        print('Yes')
    else:
        print('No')

should_wear_jacket(50)
should_wear_jacket(75)
```

# Demo 3

In complex problems, we don't have to have our solution all figured out:

```python
names = ['Max Bartlett', 'Angelita Norris', 'Stewart Mueller', 'Dominique Henry', 'Carmela Gross', 'Bettie Mcmillan', 'Sara Ellison', 'Ira Anthony', 'Pauline Riley', 'Ben Weber',
         'Joanne Mcknight', '|Loren Gould', 'Jamar Singh', 'Amanda Vance', 'Tyrell Andrade', 'Jana Clements', 'Eddy Mcbride', 'Marsha Meyer', 'Elbert Shannon', 'Alyce Hull']
```

```python
# this function converts the list of names into email ids
def create_email_ids(names):
    pass

# returns the following list
# ['max.bartlett@gmail.com', 'angelita.norris@gmail.com', ...]
```

### Pseudocoding

```python
def create_email_ids(names):
    # email_ids list

    # name (looping names list)
        # format name to email id
        # add email id to email_ids list

    # return email_ids list
```

### Writing actual code (of what we have figured out)

```python
# Formats Max Bartlett -> max.bartlett@ripplemedia.com
def format_to_email(name):
    # lower case name
    # replace space between first name and last name with '.'
    # concatenate '@gmail.com'
    # return final string
    pass


def create_email_ids(names):
    email_ids = []

    # name (looping names list)
    for name in names:
        # format name to email id
        email = format_to_email(name)
        # add email id to email_ids list
        email_ids.append(email)

    return email_ids
```

### Filling out the remaining details

```python
# Formats Max Bartlett -> max.bartlett@ripplemedia.com
def format_to_email(name):
    # lower case name
    lower_names = name.lower()
    # replace space between first name and last name with '.'
    dotted_names = '.'.join(lower_name.split(' '))
    # concatenate '@gmail.com'
    email_id = dotted_names + '@gmail.com'
    # return final string
    return email_id


def create_email_ids(names):
    email_ids = []
    # name (looping names list)
    for name in names:
        # format name to email id
        email_id = format_to_email(name)
        # add email id to email_ids list
        email_ids.append(email_id)

    return email_ids
```

### Optimizing code

```python
# optimized version of code
def format_to_email(name):
    lower_names = name.lower()
    dotted_names = '.'.join(lower_names.split(' '))
    return dotted_names + '@gmail.com'


def create_email_ids(names):
    email_ids = []
    for name in names:
        email_id = format_to_email(name)
        email_ids.append(email_id)
    return email_ids


create_email_ids(names)
```

# Final thoughts

By following the steps of psuedocoding, writing actual code and optimizing that code, we take the pressure off getting things right on the first attempt. Whether you pseudocode on paper, whiteboard or in a code editor, it is a skill all programmers should have in their repertoire.

Most imporantly, the level of detail you put into your pseudocode is up to you, write it in the way it makes sense to you!
