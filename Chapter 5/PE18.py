def main():

    def is_prime(num):
        even_divisors = 0
        if num <= 1:
            return False
        else:
            for x in range(1, num+1):
                if num % x == 0:
                    even_divisors += 1
                    if even_divisors > 2:
                        return False
        return True

    for x in range(1, 101):
        if (is_prime(x)):
            print(x, "is prime")
        else:
            print(x, "isn't prime")

main()
