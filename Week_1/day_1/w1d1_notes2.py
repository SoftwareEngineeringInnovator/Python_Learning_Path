# Variables naming rules

# Valid naming for variables
blue_sky = "sun" # Letters and underscore
pizza2 = "pepperoni" # numbers appear after letters
_score = 23 # start with underscore

# Invalid naming for variables
# 1student = "Carla" cannot start with a number
# fruit-basket = "Grape" Hyphen is not allowed
# student name = "Sarah" cannot contain a space

# Python is Case Sensitive
age = 18
Age = 20
AGE = 30

print(Age)

# Snake_Case Variables - words are separated by underscores
student_first_name = "Fredy"
student_last_name = "Chilito"
favorite_food = "Arroz Chaufa"

#  camelCase - capital letters after the first word
favoriteFood = "Arroz Chaufa"
carModel = "Mitsubishi"

# PascaleCase - every letter begins with a capital
FavoriteColor = "Red"
CarModel = "Mitsubishi"

# Variables can reassined

score = 50
print(score)

score = 75
print(score)

# Variables can be used to calculate
shirt_price = 20
pants_price = 35

total = shirt_price + pants_price
print(total)

# Update a variable using itself
point = 10
point = point + 5
# point += 5 - same as writing out point = point + 5
print(point)

# Reusing Variables
student_name = "Jordan"
student_age = 18
favorite_subject = "Computer Science"
print("Name:" , student_name)
print("Age:" , student_age)
print("Favorite Subject:" , favorite_subject)
