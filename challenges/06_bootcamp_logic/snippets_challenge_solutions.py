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