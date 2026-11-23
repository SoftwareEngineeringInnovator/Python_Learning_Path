# Logical Operators

# and - both conditions must be true
age = 20
has_id = True

print(age >= 18 and has_id)

age = 21
has_certification = False

if age >= 18 and has_certification:
    print("Eligible")
else:
    print("Not Eligible")

# or - At least ONE condition must be true
has_ticket = False
has_guest_pass = True

if has_ticket or has_guest_pass:
    print("Entry allowed")
else:
    print("Entry denied")

# not - reversed a Boolean result
is_logged_in = False
print(not is_logged_in)

if not is_logged_in:
    print("Please log in")
else:
    print("Welcome back")

#  Identity Operators - check wether two variables refer to the same exact object in memory

list1 = ["apple", "banana"]
list2 = ["apple", "banana"]

print(list1 == list2)
print(list1 is list2)

list1 = list2
print(list1 is list2)

result = None

if result is None:
    print("No result available")

#  Conditional Statement

print("Good morning")
print("Welcome to class")
print("Let's begin")

# if - check conditions
# elif (else if) - check another condition when the earlier conditions are not met
# else - run when no previous condition are met

# if condition:
    # Code to run if the condition is true

age = 20

if age >= 18:
    print("You are an adult")

score = 95

if score >= 70:
    print("Cogratulations you passed")

temperature = 65

if temperature > 80:
    print("It is hot outside")

balance = 100
purchase = 125

if balance >= purchase:
    print("Purchase approved")
else:
    print("Insuficient funds")

light = "yellow"

if light == "green":
    print("Go")
elif light == "yellow":
    print("Slow down")
elif light == "red":
    print("STOP")
else:
    print("Unknown light")