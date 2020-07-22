def main():
    
    monthly_rainfall = []
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    
    for x in range(12):
        rainfall = int(input("What was the month's total rainfall? "))
        monthly_rainfall.append(rainfall)
        
    total = 0
    
    for x in monthly_rainfall:
        total += x
    
    average = total/12
    
    lowest = min(monthly_rainfall)
    lowest_month = months[monthly_rainfall.index(lowest)]
    
    highest = max(monthly_rainfall)
    highest_month = months[monthly_rainfall.index(highest)]

    print("The total rainfall for the year was", total)
    print("The average rainfall per month was", format(average, '.2f'))
    print("The month with the least rainfall was", lowest_month)
    print("The month with the most rainfall was", highest_month)

main()
    
