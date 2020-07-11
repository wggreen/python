budget = float(input("What's your monthly budget? "))

expenses = 0

print("\nYour monthly expenses so far are $", expenses, sep="")

more_expenses = input("\nDo you have an expense to add? ")

while more_expenses != "no" and more_expenses != "No":
    expense = float(input("\nEnter the cost of your monthly expense: "))
    expenses += expense
    print("\nYour monthly expenses so far are $", format(expenses, '.2f'), sep="")
    if expenses > budget:
       difference = expenses - budget
       print("You are $", format(difference, '.2f'), " over budget", sep="")
    if expenses < budget:
       difference = budget - expenses
       print("You are $", format(difference, '.2f'), " under budget", sep="")
    more_expenses = input("\nDo you have an expense to add? ")


