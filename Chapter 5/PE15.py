def main():
    score_one = int(input("Enter the first score: "))
    score_two = int(input("Enter the second score: "))
    score_three = int(input("Enter the third score: "))
    score_four = int(input("Enter the fourth score: "))
    score_five = int(input("Enter the fifth score: "))

    def calc_average(one, two, three, four, five):
        avg = (one + two + three + four + five) / 5
        return avg
    
    average = calc_average(score_one, score_two, score_three, score_four, score_five)

    def determine_grade(score):
        if score < 60:
            letter = "F"
        elif score >= 60 and score <= 69:
            letter = "D"
        elif score >= 70 and score <= 79:
            letter = "C"
        elif score >= 80 and score <= 89:
            letter = "B"
        elif score >= 90 and score <= 100:
            letter = "A"
        return letter

    print("\nScore \tLetter Grade")

    grade = determine_grade(score_one)
    print(score_one, " \t", grade, sep="")
    grade = determine_grade(score_two)
    print(score_two, " \t", grade, sep="")
    grade = determine_grade(score_three)
    print(score_three, " \t", grade, sep="")
    grade = determine_grade(score_four)
    print(score_four, " \t", grade, sep="")
    grade = determine_grade(score_five)
    print(score_five, " \t", grade, sep="")

    print("Average score:", format(average, '.2f'))
    
main()
