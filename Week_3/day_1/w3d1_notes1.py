# Example 1: Dictionary with Lists
# A dictionary can store lists as values.

store = {
    "aisle_1": ["fruits", "vegetables", "dairy"],
    "aisle_2": ["meat", "frozen", "bread"]
}

print(store["aisle_2"][1])

# Example 2: Dictionaries Inside Dictionaries
# A dictionary can contain another dictionary, which can also contain lists.

complex_store = {
    "one_aisle": {
        "dairy": [
            {"name": "milk", "price": 2.59},
            {"name": "cheese", "price": 1.59}
        ]
    }
}

print(complex_store["one_aisle"]["dairy"][0]["price"])

# Example 3: List of Dictionaries
# A list can contain multiple dictionaries.

students = [
    {"name": "Alice", "grade": "A"},
    {"name": "Bob", "grade": "B"},
    {"name": "Charlie", "grade": "C"}
]

print(students[1]["name"])

# Example 4: Nested Shopping Cart
# Let's combine dictionaries and lists to represent an online shopping cart.

cart = {
    "electronics": [
        {"item": "Laptop", "price": 799.99, "quantity": 1},
        {"item": "Headphones", "price": 59.99, "quantity": 2}
    ],
    "groceries": [
        {"item": "Bananas", "price": 0.59, "quantity": 6},
        {"item": "Eggs", "price": 2.99, "quantity": 1}
    ]
}

print(cart["electronics"][0]["price"])
print(cart["groceries"][0]["quantity"])

# JSON stands for JavaScript Object Notation
# Example JSON Data
{
    "firstName": "Jane",
    "lastName": "Doe",
    "age": 35,
    "hobbies": ["running", "singing"], # JSON it is called and array
    "children": [
        {"firstName": "Alice", "age": 6}, # JSON object
        {"firstName": "Bob", "age": 8}
    ]
}

# JSON RULES

# 1. Keys must ALWAYS use double quotes

# 2. Strings MUST use double quotes

# 3. Boolean values are lowercase - true or false

# 4. JSON uses null instead of None

# 5. JSON does not alllow triling comas

# 6. JSON does not support comments

# Python Vs. JSON

student_dict = {
    "name": "Alice",
    "age": 25
}

student_json = '{"name":Alice, "age";25}'

print(type(student_dict))
print(type(student_json))