print("Challenge 3.1: Debug code snippets")

print()

print("Code Snippet 1:")

a = 1
b = 1
c = (a > b)

# 1 is not greater than 1 hence modifying the print statement
print("The value of c is False since a is not greater than b, but equal to b.")

print()

print("Code Snippet 2:")

d = (True or (5 > 7) or not (8 < 20))

# The value of d is True
print("The value of d is True since the operator is OR.")

print()


print("Code Snippet 3:")

m = "GOAT"
n = "goat"

o = (m == n)

# Python is case-sensitive
print ("The value of o is False since Python is case-sensitive.")

print()

print("Code Snippet 4:")

u = 5
v = 2

# '=' is the assignment operator; '==' is the comparison operator
if u * v == 10:
    print("The product of a and b is 10")
else:
    print("The product of a and b is not 10")

print()

print("Code Snippet 5:")
x = 15
y = 25

z = 30

if z < x:
    print("z is less than x")

# Missing the semicolon after the elif condition
elif z > x and z < y:
    print("z is between x and y")

# Missing the semicolon after else
else:
    print("z is greater than y")


print()
print()
print()

print("Challenge 3.2: Playing with the stock market")

print()

print("Challenge 3.2.1: Creating variables")

amazon = 3000
apple = 100
fb = 250
google = 1400
msft = 200

print()


print("Challenge 3.2.2: Taking user input")

name = input("What is your name?")
# extra points for checking errors in the user input
savings = int(input("How much savings do you have?"))
stock = input("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft.")
print()

print("Challenge 3.2.3: Perform user-specific calculations")

'''
Your code should look like this:

if stock == "amzn":
    ...
elif ...
else ...
'''
num_of_stocks = 0

if stock == "amzn":
    price = amazon
    num_of_stocks = savings/price
elif stock == "aapl":
    price = apple
    num_of_stocks = savings/price
elif stock == "fb":
    price = fb
    num_of_stocks = savings/price
elif stock == "goog":
    price = google
    num_of_stocks = savings/price
elif stock == "msft":
    price = msft
    num_of_stocks = savings/price
else:
    price = "NA"

print()

print("Challenge 3.2.4: Output for the user the result")

if price == "NA":
    print("Incorrect stock name entered.")
else:
    print(f"{name} has ${savings} in savings and he can buy {num_of_stocks} shares of {stock} at the current price of ${price}.")

