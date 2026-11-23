# List continuation

# len() - count how items are inside of a list
students = ["Alex", "Ben", "Marcus", "Marie"]
print(len(students))

# list() constructor
# list can be created by converting another iterable into one

letters = list("Python")
print(letters)

# Modifying Python List
students = ["Alex", "Ben", "Marcus", "Marie"]
print(students)

# change one item
students[1] = "Maria"
print(students)

# Change multiple items
students[1:3] = ["Brian", "Sophie"]
print(students)

# Yu can replace two items with three
students[1:3] = ["Brian", "Sophie", "Hope"]

# Adding items to list

# .append() - add ONE item to the end

shopping_list = ["milk", "bread"]
shopping_list.append("eggs")
print(shopping_list)

# .insert - add at a specific position
shopping_list.insert(1, "butter")
print(shopping_list)

# .extend() - add items from another collection
shopping_list = ["milk", "bread"]
more_items = ["eggs", "cheese", "butter"]

# .append() Vs. extend()

numbers = [1, 2]
numbers.append([3, 4])
print(numbers)

numbers = [1, 2]
numbers.extend([3, 4])
print(numbers)

# Removing Items From Lists

cars = ["BMW", "Honda", "Mazda", "Ford"]
cars.remove("Honda")
print(cars)

# If value appears multiple times only first occurence is removed
cars = ["BMW", "Honda", "Ford", "Mazda", "Ford"]
cars.remove("Ford")
print(cars)

# .pop() - Remove by INDEX
cars = ["BMW", "Honda", "Ford", "Mazda", "Ford"]
cars.pop(1)
print(cars)

cars = ["BMW", "Honda", "Ford", "Mazda", "Ford"]
removed_car = cars.pop(1)
print(cars)
print(removed_car)

# If pop() is called without index, it removes last item
numbers = [1, 2, 3, 4]
numbers.pop()
print(numbers)

# del - delete by index of the variable
fruits = ["apple", "orange", "grape"]
# del fruits(0)
print(fruits)

# del fruits
# print(fruits)

# .clear() - empty the list
fruits = ["apple", "orange", "grape"]
fruits.clear()
print(fruits)

# Checking if an item exists
students = ["Alex", "Mario", "Jen", "Maria"]
print("Mario" in students)
print("James" in students)

if "Maria" in students:
    print("Maria is enrolled")
else:
    print("Student is not in list")



