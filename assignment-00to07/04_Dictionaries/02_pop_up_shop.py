def calculate_total_cost():
    fruit_price = {
        "Apple": 5.0,
        "Mango": 18.0,
        "Banana": 4.0,
        "Watermelon": 15.0,
        "Pineapple": 20.0,
        "Strawberry": 18.0
    }

    total_cost = 0

    for fruit,price in fruit_price.items():
        while True:
            try:
                quantity = int(input(f"How many {fruit} do you want? "))
                if quantity < 0:
                    print("Invalid input. Please enter a non-negative number.")
                    continue
                total_cost += price * quantity
                break 

            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

        print(f"\n Your total cost is: ${total_cost: .2f}")

if __name__ == "__main__":
    calculate_total_cost()