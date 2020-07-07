weight = float(input("What is your weight? (in pounds) "))
height = float(input("What is your height? (in inches) "))

bmi = (weight * 703) / (height ** 2)

if bmi < 18.5:
    print("You're underweight")
if bmi >= 18.5 and bmi <= 25:
    print("You're an optimal weight")
if bmi > 25:
    print("You're overweight")
