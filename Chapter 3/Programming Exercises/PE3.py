age = int(input("What's the person's age? "))
if age <= 1:
    print("They're an infant.")
if age > 1 and age < 13:
    print("They're a child.")
if age >= 13 and age < 20:
    print("They're a teenager.")
if age >= 20:
    print("They're an adult.")
