# break, continuo and else

# breal - stop the loop completely
for number in range(5):
    if number == 3:
        break
    print(number)

# continue - skip the current iteration
for number in range(5):
    if number == 3:
        continue
    print(number)

#  else

for number in range(3):
    print(number)
else:
    print("Loop is finished")