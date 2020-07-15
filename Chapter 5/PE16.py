import random

even = 0
odd = 0
for x in range(100):
    number = random.randint(1, 100)
    if number % 2 == 0:
        even += 1
    else:
        odd += 1
print(even, "of the 100 numbers were even")
print(odd, "were odd")
