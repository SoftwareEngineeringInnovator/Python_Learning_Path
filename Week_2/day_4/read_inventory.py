# Import load_workbook
from openpyxl import load_workbook

# Load prior workbook from file - create_inventory.py
wb = load_workbook("./spreadsheets/store_inventory.xlsx")

# View and Select Worksheets
print(wb.sheetnames)

# Loop through worksheets if the workbook has multiple sheets
for sheet in wb:
    print(sheet.title)

# Select worksheet
ws = wb["Store Inventory"]

# Find Number of Rows and Columns
print(ws.max_row)
print(ws.max_column)

# loop through the header row
for cell in ws[1]:
    print(cell.value)

# loop through all the data
for row in ws.values:
    print(row)

# Skip the Header row
for row in ws.iter_rows(min_row = 2, values_only = True):
    print(row)

# Count product records
count = 0

for row in ws.iter_rows(min_row = 2, values_only = True):
    if row[0] is not None:
        count +=1
print("Total Products:", count)

# Create a Function to read data from Excel sheet
def get_prices(worksheet):
    prices = {}
    for row in worksheet.iter_rows(
        min_row = 2,
        values_only = True
    ):
        name = row[0]
        price = row[0]

        prices[name] = price
    return price

product_prices = get_prices(ws)
print(product_prices)