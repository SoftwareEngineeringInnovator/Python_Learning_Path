# Looping through dictionaries

fruits = ["apple", "orange", "grape"]

for fruit in fruits:
    print(fruit)

fruits = {
    "red": "apple",
    "purple": "grape",
    "green": "avocado"
}

# Loop through keys
for key in fruits:
    print(key) # print the key from the dictionary

# loop through key and value . items()

for key, value in fruits.items():
    print(key, value)

grades = {
    "Jessica": 95,
    "Ben": 100,
    "David": 67,
    "Marie": 85
}

for student, score in grades.items():
    print(f"{student} scored {score}")

# Nested Dictionaries
# Nested dictionary - dictionary stored inside another dictionary

students = {
    "student1": {
        "name": "Jessica",
        "age": 17,
        "grade": 12
    },
    "student2": {
        "name": "Ben",
        "age": 18,
        "grade": 12
    }
}

# Access information
print(students["student1"]["name"])

print(students["student2"]["age"])

menu = {
    "pizza": {
        "price": 12.99,
        "category": "Italian",
        "available": True
    },
    "burger": {
        "price": 8.99,
        "category": "American",
        "available": True
    },
    "tacos": {
        "price": 9.99,
        "category": "Mexican",
        "available": False
    }
}

print(menu["pizza"]["price"])
print(menu["pizza"]["available"])
print(menu["tacos"]["available"])

students = {
    "student1": {
        "name": "Jessica",
        "age": 17,
        "subjects": ["Math", "English", "Science"],
        "grades": [90, 85, 75],
        "contact": {
            "jessica@example.com"
            "phone": 123-4567
        }
    },
    "student2": {
        "name": "Ben",
        "age": 18,
        "subjects": ["History", "Music", "Art"],
        "grades": [95, 100, 70],
        "contact": {
            "ben@example.com"
            "hone": 456-7890
            }
    }
}

print(students["student1"]["subjects"][1])