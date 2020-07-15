def main():
    feet = int(input("How many feet? "))
    
    def feet_to_inches(num):
        inches = num * 12
        return inches

    inch = feet_to_inches(feet)

    print("That's", inch, "inches")

main()
