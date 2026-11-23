# ITP Week 2 Day 3 Exercise
# Modules, Dictionaries, Functions, and Excel Automation

# SCENARIO:
# You are creating an Excel report for a small store.
# The store wants to track products, prices, and inventory.


# 1. Import the random module and Workbook from openpyxl.


# 2. Create a workbook and rename the active
# worksheet to "Store Inventory".


# 3. Add these headers using ws.append():
# Product, Price, Quantity


# 4. Use the following list of dictionaries:

products = [
    {"name": "Apples", "price": 2.756},
    {"name": "Bananas", "price": 1.894},
    {"name": "Oranges", "price": 3.459},
    {"name": "Grapes", "price": 4.125}
]


# 5. Create a function named add_product(product).
#
# a. Get the name and price from the dictionary.
# b. Round the price to 2 decimal places.
# c. Generate a random quantity between 5 and 50.
# d. Use ws.append() to add the information to Excel.


# 6. Loop through products and call add_product()
# for each dictionary.


# 7. Use ws.iter_rows(values_only=True) to
# print the worksheet data.


# 8. Create a second worksheet named "Summary".
# Add "Total Products" to A1 and use len()
# to add the number of products to B1.


# 9. Save the workbook as "store_inventory.xlsx".


# BONUS:
# Use random.choice() to select a random product
# and print its name.

