length = float(input("What's the length of the first rectangle? "))
width = float(input("What's the width of the first rectangle? "))
length2 = float(input("what's the length of the second rectangle? "))
width2 = float(input("What's the width of the second rectangle? "))
area = length * width
area2 = length2 * width2
if area > area2:
    print("The area of the first rectangle is bigger.")
if area < area2:
    print("The area of the second rectangle is bigger.")
if area == area2:
    print("The two rectangles have the same area.")
