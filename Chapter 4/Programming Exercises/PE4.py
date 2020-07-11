speed = float(input("What's the vehicle's speed? "))
time = int(input("How many hours has it traveled? "))
print("Hour \tDistance Traveled")

for x in range(1, time+1):
    distance = speed * x
    print(x, "\t", format(distance, '.0f'), sep="")
    
