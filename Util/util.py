def valid_input_assets():
    while True:
        user_input = input("How many assets: ")
        try:
            number = int(user_input)
            if number >= 0:
                break
            else:
                print("Invalid input. Try again.\n")
        except ValueError:
            print("Invalid input. Try again\n")
    return number

def valid_input_int(from_a, to_b):
    while True:
        user_input = input("Enter: ")
        try:
            number = int(user_input)
            if from_a <= number <= to_b:
                break
            else:
                print("Invalid input. Try again.\n")
        except ValueError:
            print("Invalid input. Try again\n")

    return number

def category_type(choice):
    match choice:
        case 1:
            return "stocks"
        case 2:
            return "reits"
        case 3:
            return "bonds"

def category_input():
    print("\nCategory: ")
    print("[1]Stocks.\n[2]REITs.\n[3]Bonds.")
    user_input = valid_input_int(1,3)

    return category_type(user_input)

def comparing_allocations_stocks(current_allocation, target_allocation):
    if current_allocation > target_allocation:
        return "Sell Stocks."
    elif current_allocation == target_allocation:
        return "Stocks are ok!"
    else:
        return "Buy Stocks."

def comparing_allocations_reits(current_allocation, target_allocation):
    if current_allocation > target_allocation:
        return "Sell REITs."
    elif current_allocation == target_allocation:
        return "REITs are ok!"
    else:
        return "Buy REITs."

def comparing_allocations_bonds(current_allocation, target_allocation):
    if current_allocation > target_allocation:
        return "Sell Bonds."
    elif current_allocation == target_allocation:
        return "Bonds are ok!"
    else:
        return "Buy Bonds."
