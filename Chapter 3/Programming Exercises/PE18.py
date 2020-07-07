vegetarian = input("Is anyone in your party a vegetarian? ")
vegan = input("Is anyone in your party a vegan? ")
gluten_free = input("Is anyone in your party gluten-free? ")

print("Here are your restaurant choices:")

if (vegetarian == "no" or vegetarian == "No") and (vegan == "no" or vegan == "No") and (gluten_free == "no" or gluten_free == "No"):
    print("\tJoe's Gourmet Burgers")
    print("\tMain Street Pizza Company")
    print("\tCorner Cafe")
    print("\tMama's Fine Italian")
    print("\tThe Chef's Kitchen")
if (vegetarian == "yes" or vegetarian == "Yes") and (vegan == "no" or vegan == "No") and (gluten_free == "no" or gluten_free == "No"):
    print("\tMain Street Pizza Company")
    print("\tCorner Cafe")
    print("\tMama's Fine Italian")
    print("\tThe Chef's Kitchen")
if (vegetarian == "no" or vegetarian == "No") and (vegan == "yes" or vegan == "Yes") and (gluten_free == "no" or gluten_free == "No"):
    print("\tCorner Cafe")
    print("\tThe Chef's Kitchen")
if (vegetarian == "no" or vegetarian == "No") and (vegan == "no" or vegan == "no") and (gluten_free == "yes" or gluten_free == "yes"):
    print("\tMain Street Pizza Company")
    print("\tCorner Cafe")
    print("\tThe Chef's Kitchen")
if (vegetarian == "yes" or vegetarian == "Yes") and (vegan == "no" or vegan == "No") and (gluten_free == "yes" or gluten_free == "Yes"):
    print("\tMain Street Pizza Company")
    print("\tCorner Cafe")
    print("\tThe Chef's Kitchen")
if (vegetarian == "no" or vegetarian == "No") and (vegan == "yes" or vegan == "Yes") and (gluten_free == "yes" or gluten_free == "yes"):
    print("\tCorner Cafe")
    print("\tThe Chef's Kitchen")
if (vegetarian == "yes" or vegetarian == "Yes") and (vegan == "yes" or vegan == "Yes") and (gluten_free == "yes" or gluten_free == "Yes"):
    print("\tCorner Cafe")
    print("\tThe Chef's Kitchen")
