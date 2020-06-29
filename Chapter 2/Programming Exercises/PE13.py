r = float(input("How long is the row (in feet)? "))
e = float(input("How much space is needed for the end-post assembly? "))
s = float(input("How much space is there between the vines? "))

v = (r-(2*e))/s

print("You can fit", v, "grapevines in the row")
