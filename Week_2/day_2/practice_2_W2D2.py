# ITP Week 2 Day 2 (In-Class) Practice 2

# Functions Parameters and Arguments

# Lets take those functions we built in practice_1 and make them more dynamic:

# Rewrite the functions from practice_1 using parameters:

# add_num
def add_num(x, y):
    print(x + y)

print("I should see the number 7 below from add_num: ")
add_num(3, 4)

# subtract_num
def subtract_num(x, y):
    print(x - y)

print("I should see the number -2 below from subtract_num: ")
subtract_num(6, 8)

# multiply_num
def multiply_num(x, y):
    print(x * y)

print("I should see the number 18 below from multiply_num: ")
multiply_num(2, 9)

# divide_num
def divide_num(x, y):
    if y == 0:
        print("Error - Can Not Divide By Zero")
    else:
        print(x / y)

print("I should see the number 2 below from divide_num: ")
divide_num(10, 5)

# Don't forget to call your functions to make sure they work

#Uncomment to call your functions:


# Extra Time?

# Now take in 2 users inputs and pass them 
# in as arguments when calling the functions

# Ask user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Pass the user's numbers to the addition function
print("Results from adding the two user's inputs:")
add_num(num1, num2)

print("Results from subtracting the two user's inputs:")
subtract_num(num1, num2)

print("Results from multiplying the two user's inputs:")
multiply_num(num1, num2)

print("Results from dividing the two user's inputs:")
divide_num(num1, num2)