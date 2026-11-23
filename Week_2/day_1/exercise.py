
# ITP Week 2 Day 1 Exercise
# Dictionaries, Loops, and Nested Dictionaries

# 1. Dictionary Loop

inventory = {
    "soda_cans": 45,
    "chips": 12,
    "sandwiches": 34,
    "candy": 0
}

# SCENARIO: A customer bought one of every available item!

# Use a for loop to decrease each item's quantity by 1
# Do not allow any quantity to go below 0

# Print each item and its updated quantity using .items()


# 2. Nested Dictionaries

students = {
    "student1": {
        "name": "Amy",
        "grades": [90, 85, 95]
    },
    "student2": {
        "name": "John",
        "grades": [80, 88, 92]
    }
}

# a. Print John's second grade

# b. Update Amy's first grade to 100

# c. Add a new grade of 95 to John's grades list

# d. Add a new key "major" with the value "Computer Science"
#    to Amy's dictionary

# e. Loop through students using .items()
#    and print each student's name and grades

# f. Calculate and print each student's average grade
#    Hint: Use sum() and len()
