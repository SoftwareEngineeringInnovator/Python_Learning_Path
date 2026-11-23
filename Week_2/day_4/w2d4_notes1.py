# Dictionary - stores information using key: value pairs
# Key : the name or label used to identify information
# value: the actual information store under the label

student = {
    "name": "Jessica", # "name": - key, "Jessica" - value
    "age": 18,
    "grade": 12,
    "gpa": 3.8
}

print(student)

# 1. Square brackets
print(student["gpa"])

# List
fruits = ["apple", "orange", "cherry"]
print(fruits[1])

# Get
fruits = {
    "first": "apple",
    "second": "orange",
    "third": "cherry"
}

first_fruit = fruits.get("second")
print(first_fruit)

student = {
    "name": "Jessica", # "name": - key, "Jessica" - value
    "age": 18,
}

# Retrieving value that does not exist using []
# print(student["gpa"]) - this method does not allow Python for keep running,
# better if you use the get() method

# Retriving value that does not exist using .get()
print(student.get("gpa"))

# Dictionary Car
car = {
    "brand": "Toyota",
    "year": "2026"
}

car_brand = car["brand"]
print("My car is a", car_brand)

car["brand"] = "Honda"
print(car_brand)
print(car["brand"])


