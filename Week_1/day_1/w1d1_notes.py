# print() - function that tell python to display information on the screen

# function - reusable set of instructions that performs a particualr task
print("Hello, world")
print("Welcome to Python class!")
print("Today we are learning to code")
print("Let's get started")
# Python will add a new line after each call to print().

# Strings - data type used to represent text
# Strings are written inside of quotation marks

# Strings can be single or double quotes

print("Hello")
print('Hello')
print("It's a beautiful day!")
print('She said, "I love Python!"')
print("123 Main Stree")

# print("123" + 123) - TypeError: can only concatenate str (not "int") to str

# Comcatenation - joining strings together

print("Hello" + "World") # Python joins the string exactly as written
print("Hello" + " " + "World")
print("Hello " + "World")

# Numbers
print(5 + 6) # Addition
print("5" + "6") # Concatenation

# Repeat Things
print("Hello!" * 3)
print("Hello! " * 3)
print("_" * 20)
print("WELCOME TO PYTHON!")
print("_" * 20)

# Multilines Strings
# \n - new line escape sequence
# It tells Python move to the next line
print("Good evening!\nWelcome to class. \nLet's learn Python!")

# Triple Quotes
print("""
Welcome to Python class!

Today's Lesson:
1. Print Statements
2. Strings
3. Comments
4. Variables
5. User Input
""") # Preserve the lines breaks as written

print("""Hello!
Welcome to Python!
We are learning how to code!""")

# Variables
student_name = "Ben"
student_age = 18
print(student_name)
print(student_age)

my_variable = "a string"
print(my_variable)
print("This is " + my_variable)

# age = 25
# print(age)
# print("I am " {age} "years old.")

# pi = 3.14
# print(pi)
# print("This is a constant " + pi)
