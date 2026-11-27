# Magic 8 ball!

import random
from openpyxl import Workbook

fortunes = ['It is certain',
              'It is decidedly so',
              'Yes',
              'Reply hazy try again',
              'Ask again later',
              'Concentrate',
              'My reply is no',
              'Outlook not so good',
              'Very doubtful']


def get_fortune():
    return random.choice(fortunes)

fate = get_fortune()

print(fate)

# Given the function above, it will randomly choose from the fortunes list and print one.
# Using this concept we will create our own function for a new workbook in openpyxl

# Create workbook
wb = Workbook()

# Select active worksheet
ws = wb.active

# Define column headings
ws["A1"] = "Random_Generated_Code"
ws["B1"] = "Random_Generated_Name"
ws["C1"] = "Random_Generated_Last_Name"

# Create a list called first_names and prepopulate with 10 custom first names
first_names = [
    "Amy",
    "John",
    "Jessica",
    "David",
    "Sarah",
    "Daniel",
    "Maria",
    "Alex",
    "James",
    "Emily"
]

# Create a list called last_names and prepopulate with 10 custom last names
last_names = [
    "Smith",
    "Johnson",
    "Williams",
    "Brown",
    "Jones",
    "Garcia",
    "Martinez",
    "Davis",
    "Wilson",
    "Anderson"
]

# Define a function called assign_names with a parameter 'row'
def assign_names(row):

    # - cell at row=row and column=1 assign the value to str(random.randint(111111, 999999))
    # Generate a random six-digit user ID
    ws.cell(row = row, column = 1, value=str(random.randint(111111, 999999)))

    # - cell at row=row and column=2 assign the value to a random choice of first name
    # Assign a random first name to column B
    ws.cell(row = row, column =2, value=random.choice(first_names))

    # - cell at row=row and column=3 assign the value to a random choice of last name
    # Assign a random last name to column C
    ws.cell(row = row, column = 3, value=random.choice(last_names))

# set up appropriately for a new workbook and worksheet

# loop through the range of 1-10 and for each number in the range
# - call/invoke the assign_names function while passing in the number as the 'row' argument
for row in range(2, 12):
    assign_names(row)

# save your new workbook!
wb.save("./spreadsheets/generating_random_names_exercise.xlsx")