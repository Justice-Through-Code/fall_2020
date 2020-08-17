# Before class

* Reviewing functions, lists and dictionaries

# Outline of class agenda

-  Objected Oriented Programming versus Procedural Programming
- How to write Python classes to create objects
- Inheritance in Python  
 

# Object Oriented Programming

### So far...
We've been writing code in the style of **Procedural Programming**, i.e. we take blocks of logic and put them inside functions to manipulate data:


```python
from datetime import datetime

ash = {
    'name': 'Ash',
    'bio': 'Software Developer in NYC',
    'tweets': []
}

paul = {
    'name': 'Paul',
    'bio': 'PhD student at Columbia University',
    'tweets': []
}

def add_tweet(user, text):
        user['tweets'].append({ 'text': text, 'posted': datetime.now() })
        
        
add_tweet(ash, 'Today was the longest day of the summer.')
add_tweet(paul, 'Cambridge looks great during fall!')
```

However, there are other styles of programming! Here's the same code but applying concepts of **Objected Oriented Programming**:


```python
class Tweet():
    def __init__(self, text):
        self.text = text
        self.posted = datetime.now()
           
class User():
    def __init__(self, name, bio):
        self.name = name
        self.bio = bio
        self.tweets = []
        
    def add_tweet(self, text):
        self.tweets.append(Tweet(text))
    
ash = User('Ash', 'Software Developer in NYC')
ash.add_tweet('Today was the longest day of the summer.')

paul = User('Paul', 'PhD student at Columbia University')
paul.add_tweet('Cambridge looks great during fall!')


print(ash.name)
print(ash.tweets[0].text)
```

Before we dig into the syntax, here's the key idea behind OOP: We combine data and functionality and wrap it inside something called an **object**. When you're writing large programs or have a problem that is better suited to this method, you can use object oriented programming techniques.

## Creating a class


```python
class Person():
  def __init__(self, name):
    # self.name is an attribute of Person class
    self.name = name
```

## Instantiating a class


```python
person = Person('Mattan')
print(person.name) # 'Mattan'
```

## Adding a method to a class


```python
class Person():
  def __init__(self, name):
    self.name = name
  
  # greeting function is a method of Person class
  def greeting(self):
    return f'Hello, my name is {self.name}'
    
person = Person('Mattan')

print(person.greeting()) # 'Hello, my name is Mattan'
```

## Checking types


```python
print(ash)
print(type(ash))
print(ash.tweets[0])
print(type(ash.tweets[0]))

print(type(ash) == User)
print(type(ash.tweets[0]) == Tweet)
```

## Question
What if we wanted to add Mattan's age as part of the greeting?

**Example**


```python
print(person.greeting()) # 'Hello, my name is Mattan and I am 28 years old'
```

**Answer**


```python
class Person():
  def __init__(self, name, age):
    self.name = str(name)
    self.age = int(age)
    
  def greeting(self):
    return f'Hello, my name is {self.name} and I am {self.age} years old'
    
person = Person('Mattan', 28)

print(person.greeting()) # 'Hello, my name is Mattan and I am 28 years old'
```

## Let's dive deeper with other data types



```python
class Cart():
  def __init__(self):
    # self.items is an attribute of Cart class
    self.items = []
  
  # add function is a method of Cart class
  def add(self, name, price):
    item = {}
    item['name'] = name
    item['price'] = price
    self.items.append(item)
    
cart = Cart()

# add a few items
cart.add('oreos', 12)
cart.add('bananas', 2)

print(cart.items) # [{'name': 'oreos', 'price': 12}, {'name': 'bananas', 'price': 2}]
```

## Challenge 1

Create a method total that returns the total of all items added to Cart including a $ before it.

**Example**


```python
cart.add('oreos', 12)
cart.add('bananas', 2)

print(cart.total()) # $14
```

**Answer**


```python
def total(self):
  cart_total = 0
  for item in self.items:
    cart_total += item.price
  return cart_total
```

## Challenge 2


Create a method show that returns all items in Cart by name and price.

**Example**


```python
cart.add('oreos', 12)
cart.add('bananas', 2)

print(cart.show())

# oreos --- $12
# bananas --- $2
```

**Answer**


```python
def show(self):
  str_items = []
  for item in self.items:
    str_items.append(f'{item.name} --- ${item.price}')
  return '\n'.join(str_items)
```

## Challenge 3


Create a remove function that removes an item in the items list by it's name.

**Example**


```python
# add a few items
cart.add('oreos', 12)
cart.add('bananas', 2)

print(cart.items) # [{'name': 'oreos', 'price': 12}, {'name': 'bananas', 'price': 2}]

cart.remove('oreos')
print(cart.items) # [{'name': 'bananas', 'price': 2}]
```

**Answer**


```python
def remove(self, name):
  for i in range(len(self.items)):
    if self.items[i]['name'] == name:
      del self.items[i]
      break
```

## Inheritance
Objected Oriented Programming can truly be useful when it supports **inheritance**. Sometimes we want to create objects that have similar `attributes` and `methods` but also have their own unique ones. With **inheritance** you can create a **child** class that inherits all `attributes` and `methods` of the **parent** class. Let's see how that works:

### Parent Class or Super Class
Pretty simple. Nothing different from what we've learned so far.


```python
class JTCMember():
    def __init__(self, name, lang): 
        self.name = name
        self.lang = lang
        
    def greeting(self):
        print(f'Hello, my name is {self.name} and my favorite programming language is {self.lang}')
```

### Child Class or Sub Class
This is where the magic of **inheritance** happens.


```python
class Teacher(JTCMember):
    def __init__(self, name, lang, off_hrs):
        self.off_hrs = off_hrs
        # inherit parent's attributes (name, lang) and methods (greeting) 
        super().__init__(name, lang)
    # start is a unique method in the Teacher sub class
    def teach(self):
        print(f'{self.name} will now teach a class on {self.lang}')
        
class Student(JTCMember):
    def __init__(self, name, lang):
        # inherit parent's attributes (name, lang) and methods (greeting) 
        super().__init__(name, lang)
    # attend is a unique method in the Teacher sub class
    def attend(self):
        print(f'{self.name} will now attend a class on {self.lang}')
```


```python
ash = Teacher('Ash', 'Javascript', '5PM-7PM')
ash.greeting()
ash.teach()
print(ash.off_hrs)

yusuf = Student('Yusuf', 'Javascript')
yusuf.greeting()
yusuf.attend()
```

## Challenge 4

Create another sub class that inherits from `JTCMember` called `GuestSpeaker`. The subclass includes attributes `name, lang, industry`. Add a method `share` in the subclass that would print a sentence:

**Example**


```python
sam = GuestSpeaker('Sam', 'Python', "Finance")
sam.share() # Sam will now share their experience in the Finance industry.
```

**Answer**


```python
class GuestSpeaker(JTCMember):
    def __init__(self, name, lang, industry):
        # inherit parent's attributes (name, lang) and methods (greeting) 
        super().__init__(name, lang)
    # attend is a unique method in the Teacher sub class
    def share(self):
        print(f'{self.name} will now share their experience in the {self.lang} industry')
```
