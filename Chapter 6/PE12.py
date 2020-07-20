def main():
    month = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
         'August', 'September', 'October', 'November', 'December')
    days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    file = open('steps.txt', 'r')

    for x in range(12):
        total = 0
        average = 0
        for y in range(days[x]):
            steps = int(file.readline())
            total += steps
        average = total / days[x]
        print ("The average steps taken for the month of", month[x], "is", format(average, ',.2f'), "steps.")

main()
            
