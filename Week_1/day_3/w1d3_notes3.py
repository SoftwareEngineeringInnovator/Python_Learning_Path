# Conditional Statements Continuo

grade = 85

if grade >= 90:
    print("Grade: A")
elif grade >= 80:
    print("Grade: B")
elif grade >= 70:
    print("Grade: C")
elif grade >= 60:
    print("Grade: D")
else: 
    print("Grade: F")

# Employee ID Assigment

employee_id = 5048

if employee_id >= 9000:
    print("VIP Department")
elif employee_id >= 8000:
    print("Executive Department")
elif employee_id >= 7000:
    print("Management Department")
elif employee_id >= 6000:
    print("Sales Department")
elif employee_id >= 5000:
    print("Operations Department")
elif employee_id >= 4000:
    print("Communications Department")
elif employee_id >= 3000:
    print("Logistics Department")
elif employee_id >= 2000:
    print("Administration Department")
else:
    print("Security Department")

# Weather Recommendations
# We can use conditional statements to recommend clothing based on the weather.

temperature = 72

if temperature >= 90:
    print("It is very hot. Wear light clothing.")
elif temperature >= 75:
    print("It is warm. A t-shirt is fine.")
elif temperature >= 60:
    print("The weather is mild. Bring a light jacket.")
elif temperature >= 40:
    print("It is chilly. Wear a jacket.")
else:
    print("It is cold. Wear a heavy coat.")

# Using input() with conditions
# We can make the program interactive by allowing the user to enter the temperature.

temperature = int(input("Enter the temperature: "))

if temperature >= 90:
    print("Wear light clothing.")
elif temperature >= 75:
    print("Wear a t-shirt.")
elif temperature >= 60:
    print("Bring a light jacket.")
else:
    print("Wear a coat.")

age = 20
has_license = True

if age >= 16:
    if has_license:
        print("You can drive")
    else:
        print("You need a license")
else:
    print("you are too young")

grade = 85
attendance = 90

if grade >= 70:
    if attendance >= 80:
        print("Student passed")
    else:
        print("attendance too low")
else:
    print("grade too low")

user_age = 16
has_permission = True

if age >= 18:
    print("Access granted")
else:
    if has_permission:
        print("Access granted with permission")
    else:
        print("Access denied")