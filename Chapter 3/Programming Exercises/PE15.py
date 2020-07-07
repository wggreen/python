seconds = int(input("How many seconds? "))

if seconds >= 86400:
    days = seconds // 86400
    seconds -= 86400 * days
    hours = seconds // 3600
    seconds -= 3600 * hours
    minutes = seconds // 60
    seconds -= 60 * minutes
    print(days, "days,", hours, "hours,", minutes, "minutes and", seconds, "seconds")
if seconds >= 3600 and seconds < 86400:
    hours = seconds // 3600
    seconds -= 3600 * hours
    minutes = seconds // 60
    seconds -= 60 * minutes
    print(hours, "hours,", minutes, "minutes and", seconds, "seconds")
if seconds >= 60 and seconds < 3600:
    minutes = seconds // 60
    seconds -= 60 * minutes
    print(minutes, "minutes and", seconds, "seconds")
