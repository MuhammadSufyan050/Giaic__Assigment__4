import random

def main():

    secret_number = random.randint(0, 99)
    print("I am thinking of a number between 0 and 99...")

    guess = int(input("Enter a guess: "))

    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is to low.")
        else:
            print("Your guess is to high.")

        guess = int(input("Enter a guess: "))

    print(f"Congratulation! The number was {secret_number}")

if __name__ == "__main__":
    main()