# Using multiple conditions with and & or

age = 15
has_license = True

if age >=16 and has_license:
    print("You can drive")
else:
    print("You cant drive")

gpa = 3.8
volunteer_hours = 50

if gpa >= 3.5 and volunteer_hours >= 40:
    print("Eligible for scholarship")
else:
    print("Not eligible")

order_total = 75
is_premium_number = False

if order_total >= 50 or is_premium_number:
    print("free shipping")
else:
    print("shipping applies") 

student_age = 20
is_student = True
is_military = False

if (age >= 18 and is_student) or is_military:
    print("You qualify for a discount")
else:
    print("Pay full price")