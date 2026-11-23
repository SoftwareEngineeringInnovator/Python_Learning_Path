# Dictionary values and key rules
student = {
    "name": "Ben", # "name": - key, "Jessica" - value
    "age": 18,
    "gpa": 3.8,
    "graduated": False,
    "subjects": ["Math", "English", "Science"]
}

# Rules for dictionary keys

# 1. Keys must be unique

student = {
    "name": "Ben",
    "name": "Alex"
}

print(student)

# 2. Keys are not mutable types like list
# incorrect - Cant do this
# student = {
#     ["name"]: "Jessica"
# }

# print(student) # will create an error

#         ["name"]: "Jessica"
#         ^^^^^^^^^^^^^^^^^^^
#     }
#     ^
# TypeError: unhashable type: 'list'

scores = {
    "Jessica": 100,
    "David": 100,
    "Josh": 50
}

# Viewing Dictionary Content

car = {
    "brand": "Totota",
    "model": "Camry",
    "year": 2026
}

# .keys() - display all the keys
print(car.keys())

for key in car.keys():
    print(key)

# .values() - dislay allthe values

print(car.values())

for value in car.values():
    print(value)

#  .items() - display both key and the value together
    print(car.items())

# Dictonaries are ordered
student = {
    "name": "Ben", # "name": - key, "Jessica" - value
    "age": 18,
    "gpa": 3.8,
    "graduated": False,
    "subjects": ["Math", "English", "Science"]
}

print(student)

#  2. Dictionaries are mutable (changeable)
student["age"] = 19
print(student)

# 3. Dictionaries cannot have duplicates KEYS
