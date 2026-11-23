# Enumarate() - built-in function allows us to loop throug items while counting

students = ["Amy", "John", "Maria"]

for number, student in enumerate(students):
    print(number, student)

for number, student in enumerate(students, 1):
    print(number, student)

# Writting to Cells Using ws.cell()

ws.cell(row=1, column=1, value="Product")