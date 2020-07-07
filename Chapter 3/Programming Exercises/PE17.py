print("Reboot the computer and try to connect.")

answer = input("Did that fix the problem? ")

if answer == "no" or answer =="No":
    print("Reboot the router and try to connect.")
    answer2 = input("Did that fix the problem? ")
    if answer2 == "no" or answer2 == "No":
        print("Make sure the cables between the router and modem are plugged in firmly.")
        answer3 = input("Did that fix the problem? ")
        if answer3 == "no" or answer3 == "No":
            print("Move the router to a new location.")
            answer4 = input("Did that fix thr problem? ")
            if answer4 == "no" or answer4 == "No":
                print("Get a new router.")
