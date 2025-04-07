def main():

    num_1 = int(input("\033[1;3m Please enter an integer to be divided:\033[0m "))
    num_2 = int(input("\033[1;3m Please enter an integer to divide by:\033[0m "))

    quotient = num_1 // num_2
    remainder = num_1 % num_2

    print(f"The result of this division is {quotient} with a remainder of {remainder}")

if __name__ == "__main__":
    main()