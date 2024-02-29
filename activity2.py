'''claryfing the conversion of the money'''
USD = 0.27
EURO = 0.25
GBP = 0.21

'''function to convert currency by multiplying amount with rate'''
def convert_currency(amount, rate):
    # function to convert currency by multiplying amount with rate
    return amount * rate

def main():
    # main function to handle currency conversion
    print("Welcome to Currency Converter")
    print("1. AED to other currencies")
    print("2. Other currencies to AED")

    # asking the person for their choice
    choice = input("Enter your choice: ")

    if choice == '1':
        # If person wants to convert AED to other currencies
        money = float(input("Enter amount in AED: "))
        print("Select currency to convert to:")
        print("1. Euro")
        print("2. British Pound")
        print("3. US Dollar")
        currency_choice = input("Enter your choice: ")
# declaring each choice of conversion by "if,elif, elif, else" based on the user input"
        if currency_choice == '1':
            # Convert AED to Euro
            converted_amount = convert_currency(money, EURO)
            print(str(money) + " AED is equal to " + str(converted_amount) + " euro")
        elif currency_choice == '2':
            # Convert AED to British Pound
            converted_amount = convert_currency(money, GBP)
            print(str(money) + " AED is equal to " + str(converted_amount) + " British Pound")
        elif currency_choice == '3':
            # Convert AED to US Dollar
            converted_amount = convert_currency(money, USD)
            print(str(money) + " AED is equal to " + str(converted_amount) + " US Dollar")
        else:
            print("Invalid choice")
    elif choice == '2':
        # If person wants to convert other currencies to AED
        amount = float(input("Enter amount: "))
        print("Select currency to convert from:")
        print("1. Euro")
        print("2. British Pound")
        print("3. US Dollar")
        currency_choice = input("Enter your choice: ")

        if currency_choice == '1':
            # Convert Euro to AED
            converted_amount = convert_currency(amount, 1/EURO)
            print(str(amount) + " Euro is equal to " + str(converted_amount) + "AED")
        elif currency_choice == '2':
            # Convert British Pound to AED
            converted_amount = convert_currency(amount, 1/GBP)
            print(str(amount) + " British Pound is equal to " + str(converted_amount) + " AED")
        elif currency_choice == '3':
            # Convert US Dollar to AED
            converted_amount = convert_currency(amount, 1/USD)
            print(str(amount) + " US Dollar is equal to " + str(converted_amount) + "AED")
        else:
            print("Invalid choice")
    else:
        print("Invalid choice")

if __name__ == "_main_":
    main()