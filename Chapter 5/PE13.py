def main():
    def falling_distance(falling_time):
        dist = 0.5 * (9.8 * (falling_time**2))
        return dist
    for x in range(1, 11):
        distance = falling_distance(x)
        print("After", x, "seconds, the object will fall", format(distance, '.2f'), "meters")
main()
