
# ITP Week 2 Day 4 Exercise
# Modules, Functions, Dictionaries, and Excel Automation

# SCENARIO:
# You are continuing the store inventory project from Day 3.
# Create functions to read and analyze the Excel data.

# 1. Import load_workbook from openpyxl.

# 2. Load "store_inventory.xlsx" and select
# the "Store Inventory" worksheet.


# 3. Create a function named get_inventory that:
# a. Accepts a worksheet as a parameter.
# b. Loops through the rows, skipping the header.
# c. Creates a dictionary where each product name
#    is the key and its quantity is the value.
# d. Returns the dictionary.


# 4. Call get_inventory() and store the returned
# dictionary in a variable named inventory.


# 5. Create a function named check_stock that:
# a. Accepts the inventory dictionary as a parameter.
# b. Loops through the dictionary using .items().
# c. Prints "Low Stock" if quantity is below 20.
# d. Otherwise, prints "In Stock".


# 6. Call check_stock() using your inventory dictionary.


# 7. Create a function named total_stock that:
# a. Accepts the inventory dictionary as a parameter.
# b. Uses a loop to add all product quantities.
# c. Returns the total quantity.


# 8. Call total_stock(), store the returned value,
# and print the total number of items in stock.


# BONUS:
# Import the math module.
# Create a function that accepts the total stock
# and returns the number rounded up to the nearest 10.
# Hint: Use math.ceil().
