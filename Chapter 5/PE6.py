def main():

    def calculate_fat():
        fat = int(input("How many grams of fat do you eat per day? "))
        fat_calories = fat * 9
        print("That's ", fat_calories, " calories", sep="")

    def calculate_carbs():
        carbs = int(input("How many carbs do you eat per day? "))
        carb_calories = carbs * 4
        print("That's ", carb_calories, " calories", sep="")
        
    calculate_fat()
    calculate_carbs()

main()

