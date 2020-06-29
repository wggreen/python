color1 = input("Enter a color: ")
color2 = input("Enter a second color: ")
if (color1 != "red" and color1 != "blue" and color1 != "yellow") or (color2 != "red" and color2!= "blue" and color2 != "yellow"):
    print("Error")
if color1 == "red":
    if color2 == "red":
        print("You can't pick the same color twice")
    if color2 == "blue":
        print("Red and blue makes purple")
    if color2 == "yellow":
        print("Red and yellow make orange")
if color1 == "blue":
    if color2 == "blue":
        print("Ypu can't pick the same color twice")
    if color2 == "red":
        print("Blue and red make purple")
    if color2 == "yellow":
        print("Blue and yellow make green")
if color1 == "yellow":
    if color2 == "yellow":
        print("You can't pick the same colors twice")
    if color2 == "red":
        print("Yellow and red make orange")
    if color2 == "blue":
        print("Yellow and blue make green")
