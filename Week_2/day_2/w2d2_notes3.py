# print() - display a value
# return()  - gives value back to the function

def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(result)

# print()
def add_numbers(a, b):
    print(a + b)

result = add_numbers(5, 3)
print(result)

def calculate_total(price, quantity):
    return price * quantity

total = calculate_total(10, 5)
tax = total * 0.06
frinal_price = total + tax
print("Final Price:", frinal_price)

# print()
# def multiply(a, b):
#     print(a * b)
#     result = multiply(4, 5)
# result = multiply(4, 5)
# print(result)

# Explicit and Implicit

# Explicit Return - Happens when we write return statement ourselves
def get_number():
    return 100
number = get_number()
print(number)

# Return stops a function
def example():
    print("Step 1")
    print("Step 2")
    return "Finished"
    print("Step 3")
result = example()
print(result)

# Implicit Return - Function Finished without an explicit return

def say_hello():
    print("Hello")

result = say_hello()
print(result)

# Combinations
students = [
    {
        "name": "Amy",
        "grades": [90, 85, 95]
    },
    {
        "name": "John",
        "grades": [70, 755, 80]
    },
    {
        "name": "Sarah",
        "grades": [60, 65, 55]        
    }
]

# Create a function to calculate the average
def calculate_average(grades):
    total = 0

    for grade in grades:
        total += grade
    average = total / len(grades)

    return average

# Create a function to determine passing status
def check_status(average):
    if average >= 70:
        return "Passing"
    else:
        return "Failing"

# Create a function to display the report
def display_report(students):

    for student in students:
        # acces dictionary values
        name = student["name"]
        grades = student["grades"]

        # Call the average function
        average = calculate_average(grades)

        # Call the status function
        status = check_status(average)

        # Display student infor
        print("Student:", name)
        print("Grade:", grades)
        print("Average:", round(average, 2))
        print("Status:", status)