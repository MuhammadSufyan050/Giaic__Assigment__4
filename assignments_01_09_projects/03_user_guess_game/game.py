import random

print("\033[1;3mGuess the number between 1 and 50.\033[0m")
number = random.randint(1,50)

while True:
    guess = int(input("Enter your guess number: "))
    if guess < number:
        print("To low number.")
    elif guess > number:
        print("To high number.")
    else:
        print("Congratulation you got it right")
        break
