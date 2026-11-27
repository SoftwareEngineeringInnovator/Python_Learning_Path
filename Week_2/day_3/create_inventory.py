# Import workbook class
from openpyxl import Workbook

# Create a Workbook
wb = Workbook()

# Select Worksheet
ws = wb.active

# Rename the worksheet
ws.title = "Store Inventory"

# Define Excel Columns
columns = {
    "name": "Product",
    "price": "Price",
    "quantity": "Quantity"
}

# Add Headers
ws.append(list(columns.values()))

# Create a list of product dictionaries
products = [
    {
        "name": "Apples",
        "price": 2.76,
        "quantity": 15
    },
    {
        "name": "Bananas",
        "price": 1.09,
        "quantity": 30
    },
    {
        "name": "Oranges",
        "price": 3.46,
        "quantity": 12
    },
    {
        "name": "Grapes",
        "price": 4.13,
        "quantity": 45
    }
]

# Accessing a list of dictionaries
print(products[0])

# Accessing a list of dictionary with the value
print(products[0]["name"])

# Loop the list to get the value of the keys
for product in products:
    print(product["name"])

# Nested Loops
for row_num, product in enumerate(products, 2):
    for col_num, value in enumerate(product.values(), 1):
        ws.cell(
            row = row_num,
            column = col_num,
            value = value
        )

# Create a Function to add a product - add_product
def add_product(worksheet, product):
    row = []
    for key in columns:
        row.append(product.get(key))
    worksheet.append(row)

# Loop through products
for product in products:
    add_product(ws, product)

# Save the workbook
wb.save("Store_inventory.xlsx")

# Different ways to create functions for the above process

def write_product(worksheet, product, row_number):
    for col_num, value in enumerate(product.values(), 1):
        ws.cell(
            row = row_number,
            column = col_num,
            value = value
    )