# Import workbook class
from openpyxl import Workbook

# Create a Workbook
wb = Workbook()

# Select Worksheet
ws = wb.active

# Rename the worksheet
ws.title = "Store Inventory"

# Different ways to write to cells
# Use Excel Style

ws["A1"] = "Product"

# .append
ws.append(["Bananas, 1.89, 30"])

# ws.cell
ws.cell(row=4, column=1, value="Orange")

# Create a product dictionary
product = {
    "name": "Apples",
    "price": 1.76,
    "quantity": 15
}

# .keys() method - to obtain all dictionary keys
print(product.keys())

# .values() - to obtain all dictionary values
print(product.values())

# .items() - to obtain all key value pairs
print(product.items())

# enumerate -
products = ["Apples", "Cherry", "Grape"]

for product in products:
    print(product)

for index, product in enumerate(products):
    print(index, product)

# Change the starting point of the counter by using enumerate
for index, product in enumerate(products, 1):
    print(index, product)

# Using enumerate with excel
for col_num, value in enumerate(products.values, 1):
    ws.cell(row=2, column=col_num, value=value)
