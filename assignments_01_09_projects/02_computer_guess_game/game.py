import random

def guess_number():
    """Guess the number game by the computer."""
    number = random.randint(1, 50)
    guesses_left = 7 

    print("Welcome to the number guessing game")
    print("I am thinking a number between 1 to 50")

    while guesses_left > 0:
        print(f"\nYou have {guesses_left}.")

        try:
            guess = int(input("Take a guess of another number."))

        except ValueError:
            print("Invalid input: Please enter a number.")
            continue

        if guess < number:
            print("To Low number. Tell another.")

        elif guess > number:
            print("To High number. Tell another.")
        else:
            print(f"Congratulation! you got the correct number {7 - guesses_left + 1} tries.")
            return
        
        guesses_left -= 1
        print(f"\nYou ran out of guess. The number was {number}.")

if __name__ == "__main__":
    guess_number()