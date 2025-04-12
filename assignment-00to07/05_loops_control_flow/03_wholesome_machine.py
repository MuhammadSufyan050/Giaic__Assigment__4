correct_information = "I am capable of doing anything. I put my mind too."

def main():
    print("Welcome to the Wholesome Machine")

    while True:
        user_input = input(f"Please type the following affirmation: {correct_information}")

        if user_input == correct_information:
            print("That's right!")
            break
        
        else:
            print("Hmmm That was not the affirmation. Please type the following affirmation.")

if __name__ == "__main__":
    main()