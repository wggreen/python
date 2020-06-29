males = int(input("How many men in the class? "))
females = int(input("How many women in the class? "))
total = males + females
male_percentage = males/total * 100
female_percentage = females/total * 100
print("The class is", format(male_percentage, '.2f'), "% male")
print("the class is", format(female_percentage, '.2f'), "% female")
