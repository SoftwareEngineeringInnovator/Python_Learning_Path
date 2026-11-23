# ITP Week 1 Day 2 Exercise

# We will replicate a number magic trick with Python! Below is the magic trick that we will convert! 
# Below that is the python instructions, you will need to complete.

# Step 1: Pick a number from 1 - 9
# Step 2: Multiple by 2
# Step 3: Add 10 to the total
# Step 4: Divide by 2
# Step 5: Subtract by the original number
# Final Number: 5

# assign a variable "step_1" to a number of your choice between 1 - 9

step_1 = 7

# assign a variable "step_2" to the product of step_1 and the number 2

step_2 = step_1 * 2

# assign a variable "step_3" to the sum of step_2 and the number 10

step_3 = step_2 + 10

# assign a variable "step_4" to the quotient of step_3 and the number 2

step_4 = step_3 / 2

# assign a variable "step_5" to the difference between step_4 and step_1

step_5 = step_4 - step_1

# print step_5 and you should see 5!

print("The Magic Number is ..." ,step_5)

# BONUS 1: can you convert step_1 to prompt a user's input?
    # HINT: you need to cast step_1 to a int because user input is a type string.


number = int(input("Please, tell me a number between 1 to 9 ..."))

# Step 1 - User Provide a number
user_number = number
print("Excelent choice, your number is:" ,number)

# Step 2 - Multiply user_number by number 2
double_the_number = user_number * 2
print("Now I will double your number:" ,number, "to", double_the_number)

# Step 3 - Add 10 to the double_the_number variable
add_10 = double_the_number + 10
print("Let me add 10 to the number :" ,double_the_number, "so, now we have", add_10)

# Step 4 - quotient of step_3 and the number 2
quotient_the_number = add_10 / 2
print("Let divide by 2 the:" ,add_10, "so, now we have", quotient_the_number)

# step_5 = step_4 - step_1
subtract_the_number = quotient_the_number - user_number
print("The Magic Number is ..." ,subtract_the_number)

# BONUS 2: can you REFACTOR using less variables?

initial_number = int(input("Please, tell me a number between 1 to 9 ..."))

userNumber = (initial_number * 2 + 10) / 2
magic_number = userNumber - initial_number
print("The Magic Number is ..." , magic_number)


