### Quick Review 

Here's what we've learned so far: 

We've learned about **variables**, which are unique names we create to store values. The **value** on the right hand side of the `=` sign gets **assigned** to the **variable** on the left hand side. 

```python
marks_favorite_basketball_player = "LeBron James"
marks_favorite_number = 3 
```

When naming our **variables**, we should generally use lowercase descriptive names and separate words within the name with underscores `_`.  

We can use print statements to print out text and the values of variables. For example: 

```python
salary = 50000
raised_salary = salary * 1.1
print("The employee's old salary was:")
print(salary)
print("The employee's new salary is:")
print(raised_salary)
```

This will print out:
```python
>>>The employee's old salary was:
>>>50000
>>>The employee's new salary is:
>>>55000.0
```

### Advanced Printing 

Let's combine the four print statements into two print statements using 'f-strings' or 'format-strings':

```python
salary = 50000
raised_salary = salary * 1.1
print(f"The employee's old salary was: {salary}")
print(f"The employee's salary is: {raised_salary}")
```

This will print out:
```python
>>>The employee's old salary was: 50000
>>>The employee's new salary is: 55000.0
```

To use a format-string you just write a print statement as normal, but you prepend an "f" before the opening quotation mark and enclose the variable you want to print in curly braces "{}". Let's look at another example!

```python
a = 5
b = 2
print(f"The value of a is {a}. The value of b is {b}. The value of a+b is {a+b}.")
```

You can see we can even include expressions such as "a+b" in a format-string and it will be evaluated when it prints out. 

*Additional, but optional, reading resources (these will also be included at the bottom): https://realpython.com/python-f-strings/*

### Challenge 1: Printing the temperature in different units

Can you re-write the code below to use format-strings instead so that only two `print()` statements are needed, one for fahrenheit and one for celsius?

```python
current_temp_in_f = 85
# This is the formula for converting between fahrenheit and celsius
current_temp_in_c = 5/9*current_temp_in_f - 32
print("Current temperature in degrees fahrenheit:")
print(current_temp_in_f)
print("Current temperature in degrees celsius:")
print(current_temp_in_c)
```

Put your solution in a file called `print_exercise_1.py` and run it using `python3 print_exercise_1.py` to verify you get the expected output. 

### Challenge 2: Storing and calculating 2020 NBA playoff statistics 

In the 2020 NBA playoffs, Jamal Murray, Fred VanVleet, and James Harden rank #1, #2, and #3 respectively for the number of 3-point shots made at 46, 43, and 37. 

#### Challenge 2.1: Store the number of three point shots made in variables for each player 

In the file `nba_challenge.py`, create variables to track the number of 3-point shots Fred VanVleet and James Harden have made. There already exists a variable for Jamal Murray.  

#### Challenge 2.2: Print out the number of three point shots using the variables created for each player in 2.1 

Note: Make sure to use the variables you created in Challenge 2.1 in the print statements! 

#### Challenge 2.3: Store the number of three point shot attempts in variables for each player 

In the 2020 NBA playoffs, Jamal Murray, Fred VanVleet, and James Harden attempted 93, 110, 109 three point shots total. Create variables to store these values in `nba_challenge.py`, similar to what you did in Challenge 2.1. 

#### Challenge 2.4: Build on your print statement! 

Copy the print statements you wrote in Challenge 2.2 and extend them by printing both the number of three point shots each player made as well as the number of three point shots each player attempted. Try to use only one `print()` statement for each player and remember that you can use 'f-strings' to insert variables into lines of text (reference the examples above if you forgot how to do this). 

#### Challenge 2.5: Calculate and print the three point percentage for each player

The three point percentage is given by the following formula: `3 point shots made/3 point shots attempted`

### Challenge 3: Using arithmetic operations 

#### Challenge 3.1: Calculate, store, and print total points scored

In the 2020 WNBA season, Seattle Storm player Breanna Stewart played 20 games and averaged 19.7 points per-game. Using this information, calculate the total number of points Breanna Stewart scored in the 2020 WNBA season and cast the result to an integer using `int()`.  

#### Challenge 3.2: Average defensive rebounds

In the 2020 WNBA season, the Seattle Storm's top 3 defensive rebounders were

1. Breanna Stewart with 7.3 defensive rebounds per-game
2. Natasha Howard with 4.7 defensive rebounds per-game
3. Alysha Clark with 3.4 defensive rebounds per-game

Calculate, store, and print the average defensive rebounds per-game among these three players for the Seattle Storm. Print your answer as a floating point number, not an integer. 