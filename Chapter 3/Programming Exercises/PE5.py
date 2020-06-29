mass = float(input("What's the object's mass? "))
weight = mass * 9.8
if weight > 500:
    print("The object is too heavy.")
if weight < 100:
    print("The object is too light.")
