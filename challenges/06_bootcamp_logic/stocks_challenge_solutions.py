print("Challenge 3.2: Playing with the stock market")

print()

amazon = 3000
apple = 100
fb = 250
google = 1400
msft = 200

print("Challenge 3.2.1: Taking user input")

name = input("What is your name?")
# extra points for checking errors in the user input
savings = int(input("How much savings do you have?"))
stock = input("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft.")
print()

print("Challenge 3.2.2: Perform user-specific calculations")

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

print("Challenge 3.2.3: Output for the user the result")

if price == "NA":
    print("Incorrect stock name entered.")
else:
    print(f"{name} has ${savings} in savings and he can buy {num_of_stocks} shares of {stock} at the current price of ${price}.")

