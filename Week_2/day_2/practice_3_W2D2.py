
# ITP Week 2 Day 2 (In-Class) Practice 3
# Functions

# 1. Create a function named greeting that prints
# "Welcome to Python!" and call the function.
def greeting():
    print("Welcome to Python!")

greeting()

# 2. Create a function named introduce that accepts

# two parameters: name and age.
def introduce(name, age):
# Print a sentence introducing the person.
    print("My name is", name, "and I am", age, "years old.")

# Call the function with your own information.
introduce("Fredy", 47)


# 3. Next, we will use a pre-made list:

fruits = ["apple", "banana", "cherry", "mango"]

# Create a function named show_fruits that accepts a list
def show_fruits(fruit_list):

# as a parameter and prints each fruit using a for loop.
    for fruit in fruit_list:
        print(fruit)

# Call the function using the fruits list.
show_fruits(fruits)


# 4. Create a function named multiply that accepts
def multiply(x, y):

# two numbers and returns their product.
    return x * y

# Store the returned value in a variable and print it.
result = multiply(5,7)
print("Multiplication result:", result)


# 5. Create a function named say_goodbye that only
def say_goodbye():

# prints "Goodbye!" without using return.
    print("Goodbye!")

# Store the function call in a variable and print it.
goodbye_result = say_goodbye()

# What value does Python return automatically?
print(goodbye_result)
