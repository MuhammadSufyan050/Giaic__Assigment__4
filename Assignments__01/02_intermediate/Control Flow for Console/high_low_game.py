import random
print("Welcome to the High-Low Game!")
print("-------------------------------")

NUM_ROUNDS = 5
score = 0
for round_num in range(1, NUM_ROUNDS + 1):

  my_random_num: int = random.randint(1, 100)
  computer_random_num: int = random.randint(1, 100)

  print("-"* 50)
  print(f"Round {round_num}")
  print("-"* 50)

  print(f"Your number is {my_random_num}")


  user_guess = input("Do you think your number is higher or lower than the computers?: ")

  if (
      (user_guess == "higher" and computer_random_num > my_random_num)
      or
      (user_guess == "lower" and computer_random_num < my_random_num)
    ):
    print(f"You got a point +1, The computer number is {computer_random_num}")
    score += 1
  else:
    print(f"Wrong answer, The computer number is {computer_random_num}")

print(f"Your final score is {score}")

if score == NUM_ROUNDS:
  print("Wow! You played perfectly!")
elif score > 2:
  print("Good job, you played really well!")
else:
  print("Better luck next time!")