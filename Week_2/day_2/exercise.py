
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

# b. Call the function for both students.


# 2. Explicit Returns

# a. Create a function named calculate_average that
# accepts a list of grades as a parameter.

# b. Use a for loop to calculate the total of the grades.

# c. Return the average using the total and len().

# d. Call the function using each student's grades.
# Store and print both returned averages.


# 3. Scope and Global Variables

students_processed = 0

# a. Create a function named process_student that
# accepts a student dictionary as a parameter.

# b. Inside the function, use the global keyword
# to increase students_processed by 1.

# c. Print the student's name inside the function.

# d. Call the function for both students.

# e. Print students_processed outside the function.


# 4. Challenge: Combining Functions

# Create a function named check_pass that accepts
# a list of grades as a parameter.

# Use calculate_average() inside your new function.

# If the average is 70 or higher, return "Passed".
# Otherwise, return "Failed".

# Call check_pass() for both students and print the results.
