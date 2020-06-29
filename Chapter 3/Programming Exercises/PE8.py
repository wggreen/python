people = int(input("How many people are you trying to feed? "))
dogs = int(input("How many hot dogs will each person get? "))
total = people * dogs

dogs_packages_needed = total // 10
buns_packages_needed = total // 8

if dogs_packages_needed > 0:
    leftover_dogs = total % 10
    if leftover_dogs != 0:
        dogs_packages_needed += 1
if buns_packages_needed > 0:
    leftover_buns = total % 8
    if leftover_buns != 0:
        buns_packages_needed += 1

total_dogs = 10 * dogs_packages_needed
total_buns = 8 * buns_packages_needed

leftover_dogs = total_dogs - total
leftover_buns = total_buns - total

print("The number of hot dog packages required for the cookout is:", dogs_packages_needed)
print("The number of hot dog bun packages required for the cookout is:", buns_packages_needed)

print("The amount of hot dogs left over is:", leftover_dogs)
print("The amount of hot dog buns left over is:", leftover_buns)
