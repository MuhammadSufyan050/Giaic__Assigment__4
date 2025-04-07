import random
nums_sides = 6 

def main():

    die_1 = random.randint(1, nums_sides)
    die_2 = random.randint(1, nums_sides)

    total = die_1 + die_2

    print("Dice have", nums_sides, "sides each.")
    print("First Die: ", die_1)
    print("Second Die: ", die_2)
    print("Total of two dice: ", total)

if __name__ == "__main__":
    main()