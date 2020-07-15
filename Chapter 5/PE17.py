def main():

    number = int(input("Enter a number: "))
    
    def is_prime(num):
        even_divisors = 0
        if num <= 1:
            return False
        else:
            for x in range(1, number+1):
                if num % x == 0:
                    even_divisors += 1
                    if even_divisors > 2:
                        return False
        return True

    result = is_prime(number)
    if result == True:
        print("It's prime")
    else:
        print("It's not prime")

main()
            
