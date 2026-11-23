# import() Workbook
from openpyxl import Workbook

# Create the Workbook
wb = Workbook()

# Select the worksheet
ws = wb.active

# Rename the worksheet
ws.title = "Inventory"

# Add data to the cells - Excel style
ws["A1"] = "Product" # Heading
ws["B1"] = "Quantity" # Heading

ws["A2"] = "Apples" # Information under heading - Product
ws["B1"] = 25 # Information under heading - Quantity

# .append()
ws.append(["Product", "Quantity", "Price"])
ws.append(["Apples", 25, 2.50])

# Save the workbook
wb.save("Inventory.xlsx")

print("Inventory.xlsx")

# create workbook
wb = Workbook()

# select worksheet
ws = wb.active

# rename the worksheet
ws.title = "Student Tracker"

# Add headers
ws.append(["Student", "Grade Level", "Score"])

# add students
ws.append(["Amy", 12, 95])
ws.append(["John", 11, 87])
ws.append(["Joann", 12, 92])

# save workbook
wb.save("student_tracker.xlsx")

print("Student tracker created.")