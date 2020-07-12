weight = int(input("What's your starting weight? "))
print("Month \tWeight")

for x in range(1, 7):
    weight -= 4
    print(x, "\t", weight)
    
