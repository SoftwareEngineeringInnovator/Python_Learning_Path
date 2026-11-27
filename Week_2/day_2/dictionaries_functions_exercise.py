# ITP Week 2 Day 4 Exercise

# Import random module
import random

# 1. Dictionary Loop
inventory = {
    "soda_cans": 45,
    "chips": 12,
    "sandwiches": 34,
    "candy": 0
}

# SCENARIO: A person came in and bought one of everything!

# for item in inventory:
    # decrement item by using an assignment operator
    # NOTE: recall that item represents the key of the key:value pair
for item in inventory:
    if inventory[item] > 0:
        inventory[item] -=1

# Display updated inventory
print("Updated Inventory:")

for item in inventory:
    print(item, ":", inventory[item])

# 2. Implicit Functions
# (When we work with global variables/objects and don't return anything,
# these functions are implicit return functions!)

# a. Dictionaries - create a function that takes in a dictionary which updates the "role" key value pair and makes it uppercase

user_1 = {
    "firstName": "Stephanie",
    "lastName": "Lentell",
    "role": "Instructor",
    "id": "95485"
}

user_2 = {
    "firstName": "Brion",
    "lastName": "Lentell",
    "role": "Instructor",
    "id": "67344"
}

user_3 = {
    "firstName": "Daniel",
    "lastName": "Kim",
    "role": "Instructor",
    "id": "74324"
}

# Function to update instructor role
def update_role(user):
    user["role"] = user["role"].upper()
    user["id"] = str(random.randint(10000, 99999))

# b. Dictionaries - Run the functions (3 times for each user!)
update_role(user_1)
update_role(user_2)
update_role(user_3)

instructor_list = [user_1, user_2, user_3]
# print(instructor_list)

# c. List - create a function that takes in the list and
# checks if the each user's role is equal to "INSTRUCTOR".
# if it is the same, print VALID else print INVALID (try to use a loop here!)
def role_check(users):
    for user in users:
        if user["role"] == "INSTRUCTOR":
            print("VALID")
        else:
            print("INVALID")

# Validate all instructor roles
role_check(instructor_list)
print(user_1)
print(user_2)
print(user_3)

# d. import the random module and update the function to re-assign the id of each user

# e. don't forget to run it!

# 3. Explicit Functions
user_info = [46453, "Devin", "Smith"]

# Each element by index of user_info follows the format of: id, first_name, last_name

# Create a function with a parameter user_list
# - return a dictionary with the follow key value pairs:
# - id: user_list[0]
# - first_name: user_list[1]
# - last_name: user_list[2]
def create_user(user_list):
    return {
        "id": user_list[0],
        "first_name": user_list[1],
        "last_name": user_list[2]
    }

# Call the function and store the returned dictionary
new_user = create_user(user_info)

# Display the new user's information
print(new_user)