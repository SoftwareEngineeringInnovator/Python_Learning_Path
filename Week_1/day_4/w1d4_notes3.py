# Loop - allow program to repeat instructions automatically

for number in range(10):
    print("Welcome to my page")

# While Loop - Repeat condition while remains true
# For Loop - Iterate through collection or a specific range

# While Loops
# Check condition before each repetition

age = 16
while age < 21:
    print("Current age:", age)
    age += 1 # age = age +1

countdown = 5
while countdown > 0:
    print(countdown)
    countdown -=1 # countdown = countdown - 1
    print("Blast off")

attempts = 0
while attempts < 3:
    password = input("Enter Password: ")
    if password == "python123":
        print("Access granted")
        break
    print("Incorrect Password")
    attempts += 1

# Infinite Loops - Loop that never ends on its own

# while True:
#     print("Hello")

letters = ["a", "b", "c"]

index = 0

while index < len(letters):
    print(letters[index])
    index +=1

# For Loops

names = ["Dan", "John", "Chuck", "Bob"]

for name in names:
    print("Hello", name)

numbers = [10, 20, 30]

for number in numbers:
    print(number + 5)

sales = [100, 200, 300, 150]

total = 0

for sale in sales:
    total += sale
print("Total sales:", total)

for letter in "Python":
    print("letter")

# Pass - place holder

for number in [1, 2, 3]:
    pass

# range() - produce a sequence of integers

# range(stop) - start at 0 and stop before stop number
for number in range(5):
    print(number)

# range(start, stop)
for number in range(1, 3):
    print(number)

# range(start, stop, step)
for number in range(2, 15, 3):
    print(number)

#  range() with lists

pokemon = ["charmander", "squirtle", "bulbasur"]

for i in range(len(pokemon)):
    print(i, pokemon[i])

#  enumerate() - index and value

for index, name in enumerate(pokemon):
    print(index, name)