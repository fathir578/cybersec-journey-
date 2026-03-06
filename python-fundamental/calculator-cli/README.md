# Calculator CLI Project

A simple command-line interface (CLI) calculator application built with Python. This tool allows users to perform basic arithmetic operations interactively.

## Features

- **User Personalization**: Greets the user with a styled banner using their name.
- **Arithmetic Operations**: Supports Addition (`+`), Subtraction (`-`), Multiplication (`*`), and Division (`/`).
- **Error Handling**: 
  - Validates numerical inputs.
  - Handles division by zero gracefully.
  - Validates supported operators.
- **Interactive Loop**: Allows multiple calculations in a single session without restarting the script.
- **Graceful Exit**: Includes a countdown sequence when exiting the program.

## Project Structure

```text
calculator-cli/
└── calculator.py      # Main script containing all logic
```

## Prerequisites

- Python 3.x (No external libraries required)

## How to Run

Execute the script from the `calculator-cli` directory:

```bash
python calculator.py
```

## Future Improvements

- Add support for more advanced operations (power, square root).
- Implement a graphical user interface (GUI).
- Improve input validation for non-integer numbers (floats).
