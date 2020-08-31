# Before class

* Thing 1 to do before class

# Outline of class agenda

1. Handling exceptions in buggy code
2. Raising exceptions for a better development experience

# Exceptions

## Handling Exceptions

When an error occurs in your code, python stops running your script and generates an error message. However, we can write additional code to work around errors for debugging or continuing to run the script. 

### Try/except


```python
try:
  print(x)
except:
  print("Something went wrong!")
```

    Something went wrong!


### Multiple exceptions


```python
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
```

    Variable x is not defined


### Else


```python
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
```

    Hello
    Nothing went wrong


### Finally


```python
try:
  print("Hello")
except:
  print("Something went wrong")
finally:
  print("We made it to the end!")
```

    Hello
    We made it to the end!


## Challenge

Write code that handles a `TypeError`. You can use Python's [official documentation](https://docs.python.org/3/library/exceptions.html#bltin-exceptions) for possible ways to do this.

## Raising Exceptions

There are situations where you may want to raise an error if a condition isn't met. The `raise` keyword allows you to do this.


```python
x = 10
if x > 5:
    # raise a generic Exception
    raise Exception(f'x should not exceed 5. The value of x was: {x}')
```


    ---------------------------------------------------------------------------

    Exception                                 Traceback (most recent call last)

    <ipython-input-9-6849d6299e06> in <module>
          1 x = 10
          2 if x > 5:
    ----> 3     raise Exception(f'x should not exceed 5. The value of x was: {x}')
    

    Exception: x should not exceed 5. The value of x was: 10



```python
x = "hello"

if not type(x) is int:
  # raise a specific Exception
  raise TypeError("Only integers are allowed")
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-12-8eeeb1fcd402> in <module>
          3 if not type(x) is int:
          4   # raise a specific Exception
    ----> 5   raise TypeError("Only integers are allowed")
    

    TypeError: Only integers are allowed

