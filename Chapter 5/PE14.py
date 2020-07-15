def main():
    def kinetic_energy(m, v):
        ke = 0.5 * (m * (v**2))
        return ke
    mass = int(input("What's the object's mass? "))
    velocity = int(input("What's the object's velocity? "))
    energy = kinetic_energy(mass, velocity)

    print("The object has a kinetic energy of", format(energy, '.2f'))

main()
