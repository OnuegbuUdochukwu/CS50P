def main():
    mass = int(input("m: "))
    print(energy(mass))

def energy(m):
    lightSpeed = pow(300000000, 2)
    return m * lightSpeed

main()

# Easier version
c = 300000000
lightSpeed = pow(c, 2)

mass = int(input("m: "))
einstein = mass * lightSpeed

einsteinExp = f"{einstein:e}"
print(f"E: {einstein}")

print(f"E-exp: {einsteinExp}")
