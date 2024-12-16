while True:
    try:
        number = int(input("Enter an integer between 0 and 10: "))
        if 0 <= number <= 10:  # Checks if the number is between 0 and 10 inclusive
            print(f"Multiplication table for {number}: ")
            for i in range(1, 11):
                print(f"{number} x {i} = {number * i}")  # Displays the multiplication table for 'number' from 1 to 10
            break  # Exits the loop if the user entered a valid value
        else:
            print(f"{number} is not between 0 and 10. Please try again.")  # Displays an error message if the number is outside the specified range
    except ValueError:  # Handles cases where the input is not an integer
        print("Invalid input. Please enter an integer between 0 and 10: ")
