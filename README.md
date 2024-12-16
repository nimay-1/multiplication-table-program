# Multiplication Table Program

## Overview
This project is a simple Python program designed for beginners to practice loops, conditional statements, and error handling. The program generates the multiplication table for a user-provided number between 0 and 10.

---

## Features
- **Input Validation**: Ensures the user provides an integer between 0 and 10.
- **Dynamic Multiplication Table**: Generates and displays the table for the input number from 1 to 10.
- **Error Handling**: Handles invalid inputs such as non-numeric values or numbers outside the range.

---

## How It Works
1. The program prompts the user to enter an integer between 0 and 10.
2. If the input is valid:
   - The program displays the multiplication table for the entered number.
   - The program exits successfully.
3. If the input is invalid:
   - An error message is displayed.
   - The user is prompted to try again until a valid input is provided.

---

## Example Output
```
Enter an integer between 0 and 10: 5
Multiplication table for 5:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
```

---

## Installation and Usage

### Prerequisites
- Python 3.x installed on your machine.

### Running the Program
1. Clone the repository:
   ```bash
   git clone https://github.com/nimay-1/multiplication-table-program.git
   ```
2. Navigate to the project directory:
   ```bash
   cd multiplication-table-program
   ```
3. Run the script:
   ```bash
   python multiplication_table.py
   ```

---

## File Structure
```
multiplication-table-program/
|-- multiplication_table.py   # Main Python script
|-- README.md                 # Project documentation
```

---

## Learning Opportunities
This project helps beginners understand:
- Using `for` and `while` loops effectively.
- Validating user inputs with `try`/`except` blocks.
- Formatting and displaying dynamic outputs in Python.
