# Global Scope - defined outside of a function

school = "University of Maryland"

def show_school():
    print(school)

show_school()

# Local Scope - Variable created inside a function

def my_fucntion():
    message = "I am inside the function"
    print(message)
# print(message)
print(school)

name = "Jedi"

def change_name():
    name = "Storm_Trooper"
    print("Inside:", name)
change_name()
print("Outside:", name)

# Global Keyword - change global variables from inside of a function

score = 50

def update_score():
    global score
    score = 100
print("Before:", score)
update_score()
print("After:", score)
