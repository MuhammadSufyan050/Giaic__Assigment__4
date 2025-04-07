def main():

    c = 299792458
    m = float(input("Enter kilos of mass: "))

    print("e = m * C^2...")
    print("Mass = " + str(m) + " kg")
    print("C = " + str(c) + " m/s") 
    print("e = " + str(m * c ** 2) + " jules")

if __name__ == "__main__":
    main()