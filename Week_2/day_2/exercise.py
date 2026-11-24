# ITP Week 2 Day 2 Exercise

# Import the workbook that you updated in today's practice from
# Import load_workbook from openpyxl
from openpyxl import load_workbook

# "./spreadsheets/inventory.xlsx"
# Load the inventory workbook created in Week 2 Day 1
wb = load_workbook("./spreadsheets/Friendly_Store_Inventory.xlsx")

# access and store the appropriate worksheet to the variable 'ws'
# Select the inventory worksheet
ws = wb["CURRENT_MONTH_INVENTORY"]

# Add heading for reorder amounts column F
ws["F1"] = "order_amount"

# Define a function called add_order_amount that takes in a single parameter called 'row'
# Define a function to calculate reorder amounts
def add_order_amount(row):
    
    # Retrieve inventory values
    max_amount = ws.cell(row = row, column = 3).value
    threshold = ws.cell(row = row, column = 4).value
    quantity = ws.cell(row = row, column = 5).value

    # IF the quantity is less or equal to than the threshold,

        # than calculate the order_amount (max_amount - quantity) 
        # assign the value to that row, column 6
# TIP: create variables for quantity, threshold, max_amount that retrieves the values first for cleanliness
    
    # Check if quantity is at or below reorder threshold
    if quantity <= threshold:

        # Calculate the amount to be ordered
        order_amount = max_amount - quantity

        # Write reorder amount to column F
        ws.cell(row = row, column = 6, value = order_amount)

# Perform a for..in loop through the range(2, len(inventory.rows))
# Call the function add_order_amount() passing in the number of the range

# Loop through all inventory rows, skipping the header
for row in range(2, ws.max_row + 1):
    add_order_amount(row)

# Save the updated inventory workbook
wb.save("./spreadsheets/Friendly_Store_Reorder.xlsx")

