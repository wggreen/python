for x in range(1, 26):
    if x == 1:
        print("After 1 year, the ocean has risen 1.6 millimeters")
    else:
        rise = x * 1.6
        print("After", x, " years, the ocean has risen", format(rise, '.2f'), "millimeters")
