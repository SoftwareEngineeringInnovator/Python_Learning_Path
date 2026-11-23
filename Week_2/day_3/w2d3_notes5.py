from openpyxl import Workbook

wb = Workbook()
ws = wb.active

ws.append(["Name", "Price", "Quantity"])

# Define a function
def add_product(product):
    ws.append([
        product["name"],
        product["price"],
        product["quantity"]
    ])

skittles = {
    "name": "Skittles",
    "price": 2.00,
    "quantity": 100
}

add_product(skittles)

wb.save("products.xlsx")