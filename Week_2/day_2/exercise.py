
# ITP Week 2 Day 2 Exercise
# Functions, Parameters, Scope, and Return

# 1. Functions with Dictionaries

student_1 = {
    "name": "Amy",
    "major": "Computer Science",
    "grades": [90, 85, 95]
}

student_2 = {
    "name": "John",
    "major": "Cybersecurity",
    "grades": [80, 88, 92]
}

# a. Create a function named show_student that accepts
# a dictionary as a parameter and prints the student's
# name and major.
def show_student(student):
    print("Student name:", student["name"])
    print("Student major:", student["major"])

# b. Call the function for both students.

# Call the function for Amy
show_student(student_1)

# Call the function for John
show_student(student_2)

# 2. Explicit Returns

# a. Create a function named calculate_average that
# accepts a list of grades as a parameter.
def calculate_average(grades):
    total = 0

# b. Use a for loop to calculate the total of the grades.
    for grade in grades:
        total = total + grade

# c. Return the average using the total and len().
    return total / len(grades)

# d. Call the function using each student's grades.

# Calculate and store the average for each student
average_amy = calculate_average(student_1["grades"])
average_john = calculate_average(student_2["grades"])

# Store and print both returned averages.

# Print both students' averages
print("Amy's average:", average_amy)
print("John's average:", average_john)

# 3. Scope and Global Variables

students_processed = 0

# a. Create a function named process_student that
# accepts a student dictionary as a parameter.
def process_student(student):
    global students_processed

# b. Inside the function, use the global keyword
# to increase students_processed by 1.
    students_processed = students_processed + 1

# c. Print the student's name inside the function.
    print("Processing student:", student["name"])

# d. Call the function for both students.
process_student(student_1)
process_student(student_2)

# e. Print students_processed outside the function.
print("Total students processed:", students_processed)

# 4. Challenge: Combining Functions

# Create a function named check_pass that accepts
def check_pass(grades):

# a list of grades as a parameter.
# Use calculate_average() inside your new function.
    average = calculate_average(grades)

# If the average is 70 or higher, return "Passed".
# Otherwise, return "Failed".
    if average >= 70:
        return "Passed"
    else:
        return "Failed"

# Call check_pass() for both students and print the results.

# Check whether both students passed or failed
amy_result = check_pass(student_1["grades"])
john_result = check_pass(student_2["grades"])

# Print the results
print("Amy's result:", amy_result)
print("John's result:", john_result)