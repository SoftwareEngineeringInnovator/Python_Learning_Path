# Function - reuseable block of code that performs a specific task
print("Welcome to Class!")
print("Please open vs code")

def welcome_students():
    print("Welcome to class!")
    print("Please open VS code")

welcome_students()
welcome_students()

# Define Vs. Calling a Function

# 1. Define a Function - Tells Python what the function should do

# def - key word to define a fucntions
def say_hello():
    print("Hello everyone!") # indented block is the instructions given to the function
# Defining fucntion does not automatically run it.

# Call the function
say_hello()

def morning_routine():
    print("Wake up")
    print("Brush your teeth")
    print("Go eat breakfast")
    print("Go to work")
print("Starting my day...")
morning_routine()
print("I made it to work!")

# Function parameters and arguments
def greeting():
    print("Hello Jedi")
greeting()

# Parameter - a variable listed inside the parenthesis when function is defined
# Argument - actual value provided when calling the function
def greetings(name):
    print("Hello", name)
greetings("Ben")
greetings("Josh")

# Function with Numbers

def double_number(number):
    print(number * 2)

double_number(5)

# Functions with multiple parameters
#  Function can accept more than one piece of information
# By default, Python matches positional arguments in the order they are provided

def introduce(first_Name, last_name, age):
    print("First Name:", first_Name)
    print("Last Name:", last_name)
    print("Age:", age)

introduce("Ben", "Bennett", 34)

#  Keyword Argument
# introduce (
#     age = 35,
#     first_name = "Ben",
#     last_name = "Bennet"
# )

# Function with a list
def show_fruits(fruits):
    for fruit in fruits:
        print(fruit)
my_fruits = ["Strawberry", "Cherry", "Grape"]

show_fruits(my_fruits)

#  Function with a dictionary
def show_student(student):
    print("Name:", student["name"])
    print("Grade:", student["grade"])

    student_info = {
    "name": "Sarah",
    "grade": 12
}
show_student(student_info)