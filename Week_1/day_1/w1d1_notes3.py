# input() = pause the program, waits for the user to type something and return
# response as a string

name = input("what is your name? ")
print("Hello, ", name)
print(type(name))

# prompt - text inside of parenthesis, tell the user what information to enter

age = input("How old are you? ")
print("You are, ", age, "years old.")
print(type(age))

# Casting - turning a data type into another

# int() - convert valid numeric string into an integer

age = int(input("How old are you? "))
next_year = age + 1
print("Next year you will be", next_year)
print(type(age))

age_text = input("How old are you? ")
age = int(age_text)
next_year = age + 1
print("Next year you will be", next_year)
print(type(age))

# float() - convert valid number into decimal number
price = float(input("Enter the price: "))
tax = price * 0.06
total = price + tax
print("Your total is:", total)

# f- string(format string) - combine variables with text

name = "Fredy"
age = 47
# usual way
print("My name is", name, "and I am", age, "years old")

# f-string format
print(f"My name is {name} and I am {age} years old")

name = input("Enter your name: ")
favorite_food = input("What's your favorite food? ")

print(f"Hello, {name}! I heard you love {favorite_food}.")