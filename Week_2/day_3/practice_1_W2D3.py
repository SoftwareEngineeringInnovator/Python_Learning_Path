
# ITP Week 2 Day 3 (In-Class) Practice
# Modules, Libraries, and OpenPyXL

# 1. Import the math module.
import math

# Create a variable called number with the value 7.8
number = 7.8

# Use math.ceil() to round the number up.
print(math.ceil(number))

# Use math.floor() to round the number down.
print(math.floor(number))

# Use math.sqrt() to find the square root of 64.
print(math.sqrt(64))


# 2. Import the random module.
import random
fruits = ["apple", "banana", "orange", "mango"]

# Use random.choice() to select a random fruit.
print(random.choice(fruits))

# Use random.randint() to generate a number between 1 and 20.
print(random.randint(1, 20))

# 3. Working with Excel

from openpyxl import Workbook

# Create a new workbook and select the active worksheet.
wb = Workbook()
ws = wb.active

# Rename the worksheet to "My First Excel File".
ws.title = "My First Excel File"

# Verify the worksheet name
print("Worksheet name:", ws.title)

# Add "Name" to cell A1 and "Age" to cell B1.
ws["A1"] = "Name"
ws["B1"] = "Age"

# Verify both column headings
print("Column A:", ws["A1"].value)
print("Column B:", ws["B1"].value)

# Add your name to A2 and your age to B2.
ws["A2"] = "Fredy"
ws["B2"] = 47

print("Name:", ws["A2"].value)
print("Age:", ws["B2"].value)

# Print the value stored in cell A2.
print(ws["A2"].value)

# Save the workbook as "my_first_excel.xlsx".
wb.save("spreadsheets/my_first_excel.xlsx")