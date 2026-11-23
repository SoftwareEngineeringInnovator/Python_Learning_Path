# import Workbook
from openpyxl import Workbook

# create workbook
wb = Workbook()

# select worksheet
ws = wb.active

# rename worksheet
ws.title = "Inventory"

item_oreo = {
    "product_id": 2223,
    "name": "Oreo",
    "inventory": 743
}

# add headers
ws.append(["Product ID", "Name", "Inventory" ])

ws.append([
    item_oreo["product_id"],
    item_oreo["name"],
    item_oreo["inventory"]
])

wb.save("inventory.xlsx")