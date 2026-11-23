# List - collection of values stored inside one variable

fruit1 = "apple"
fruit2 = "grape"
fruit3 = "mango"

fruits = ["apple", "grape", "mango"]

# Properties of list

# 1. List are ordered

colors = ["pink", "purple", " blue"]
print(colors)

# 2. List are muteable (changeable)

colors[0] = "purple"
print(colors)

# 3. List allow duplicates values

scores = ["90", "90", "85", "100"]
print(scores)

# 4. List can conatin different data types

student = ["Jordan", 17, 3.8, True]
print(student)

# Every item in a list has a position called an index
# Python starts counting indexes at 0 instea of 1.
# Positive indexing - counting from beginning of the list

fruits = ["apple", "kiwi", "cherry", "strawberry"]
print(fruits)
print(fruits[0])
print(fruits[2])

# Negative indexing - counting backwards from the end

sports = ["golf", "tennis", "soccer", "football"]
print(sports[-1])

# Slicing List - retriving a section of the list

# Syntax for slicing
# list[start:stop]
# start is INCLUDED, stop is EXCLUDED

numbers = [10, 20, 30, 40, 50, 60, 70, 80]
print(numbers)
print(numbers[1:4])

# start from beginning - tells Python to begin at first item

print(numbers[:3])

# Continue to the end

print(numbers[3:])

# Copy the whole list

print(numbers[:])

# use a step
# list[start:stop:step]

print(numbers[::2])

print(numbers[0:8:1])

print(numbers[0:8:2])

fruits = [
    "apple",
    "orange",
    "cherry",
    "kiwi",
    "grape",
    "mango"
]

print(fruits[::3])

# start at 1, skip, move 2
print(fruits[1::2])