cookies = int(input("How many cookies do you want to make? "))
ratio = cookies/48
sugar = ratio * 1.5
butter = ratio
flour = ratio * 2.75
print("You will need:\n")
if sugar != 1:
    print(format(sugar, '.2f'), "cups of sugar")
else:
    print("1 cup of sugar")
if butter != 1:
    print(format(butter, '.2f'), "cups of butter")
else:
    print("1 cup of butter")
if flour != 1:
    print(format(flour, '.2f'), "cups of flour")
else:
    print("1 cup of flour")
