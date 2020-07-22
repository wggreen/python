def main():
    daily_sales = []
    for x in range(1, 8):
        sales = int(input("What were the sales for the day? "))
        daily_sales.append(sales)
    sum = 0
    for day in daily_sales:
        sum += day
    print("The total sales for the week were", sum)

main()
        
