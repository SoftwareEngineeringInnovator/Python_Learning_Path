# Module - Pyrthon file that contains already written code that can be reused in your program

# Using a Module - Use word import

import math

print(math.sqrt(16))

# import module entire
import math
print(math.pi)

# import specific function

from math import sqrt
print(sqrt(49))

# Display name available in module
# dir()
print(dir(math))

# You cann use help to find out the function under math library

help(math.sqrt)

# Import multiple functions

from math import sqrt, ceil, floor

print(sqrt(81))
print(ceil(4.2))
print(floor(4.8))

# Give a module a nickname

import random as rd

number = rd.randint(1, 10)
print(number)

# Function round() - round to specified precision - build in function, no need to import math

price = 12.587899

print(round(price))
print(round(price, 1))
print(round(price, 2))
print(round(price, 3))

