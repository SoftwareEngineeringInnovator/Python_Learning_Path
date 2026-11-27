
# ITP Week 2 Day 1 (In-Class) Practice
# Dictionary

# Create a dictionary named my_student with the following:
# name: [YOUR_NAME], age: [YOUR_AGE], major: "Computer Science"
my_student = {
    "first_name": "Fredy",
    "last_name": "Chilito-Ramos",
    "age": 47,
    "major": "Computer Science"
}
# Print the dictionary and verify its type using type()
print(my_student)
print(type(my_student))

# Next, we will use a pre-made dictionary:

student_1 = {
    "first_name": "Scooby",
    "last_name": "Doo",
    "gpa": 3.2,
    "enrolled": True
}

# Access and print the student's first_name using []
print(student_1["first_name"])

# Use .get() to retrieve the student's gpa
print(student_1.get("gpa"))
print(student_1["gpa"])

# Update the gpa to 3.8
student_1["gpa"] = 3.8

# Display new updated GPA
print("Updated GPA:", student_1["gpa"])

# Add a new key called "graduated" with the value False
student_1["graduated"] = False

# Verify new key called "graduated"
print("Graduated:", student_1["graduated"])

# Remove the "enrolled" key using .pop()
student_1.pop("enrolled")

# Verify the use of method .pop() to pop the "enrolled" status
print(student_1)

# Print all keys, values, and items using dictionary methods

# Display all dictionary keys
print("Keys:", student_1.keys())

# Dislay all dictionary values
print("Values:", student_1.values())

# Display all dictionary key-value pairs
print("Items:", student_1.items())