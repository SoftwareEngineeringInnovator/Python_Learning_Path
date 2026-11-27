# Modify Dictionaries

car = {
    "brand": "Ford",
    "year": 1964
}

# Changing existing value
print("Before", car)
car["year"] = 2026
print("After", car)

# Add a new key-value pair

car["color"] = "Pink"
print(car)

# update() - change or add multiple entries in one operation

student = {
    "name": "Ben",
    "age": 17,
    "grade": 11
}

student.update({
    "age": 18,
    "grade": 12,
    "gratudated": False
})
print(student)

# check if a key exist

student = {
    "name": "Jessica",
    "age": 17
}

if "age" in student:
    print("Age information exists")
else:
    print("Age information missing")

if "gpa" in student:
    print(student["gpa"])
else:
    print("GPA not found")

#  not in

car = {
    "brand": "Ford",
    "year": 2022
}

if "color" not in car:
    car["color"] = "Unknown"

print(car)

# in checks KEYS not values
print("Ford" in car.values())

print(len(car))

# removing dictionary items

# .pop() - remove an item using its key

fruits = {
    "red": "apple",
    "yellow": "lemon",
    "purple": "grape"
}

fruits.pop("yellow")
print(fruits)

# .popitem() - remove the most recent inserted key:value pair

fruits.popitem()
print(fruits)

# del - remove a specific entry

sports = {
    "first": "football",
    "second": "golf",
    "third": "soccer"
}

del sports["first"]
print(sports)

# .clear()
sports.clear()
print(sports)