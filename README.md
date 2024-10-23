# Error Calculator Web Application

This project is a web-based error calculator built using Python's Streamlit library. It allows users to compute the absolute and relative errors of two expressions: an actual value and an approximated value. The application supports basic mathematical operations, parenthesis grouping, and some predefined constants (like `pi`, `e`, and `sqrt`). The results include both rounded and chopped outputs.

## Features

- **Evaluate mathematical expressions:** Supports addition, subtraction, multiplication, division, and exponentiation.
- **Error Calculation:** Computes both absolute and relative errors between an actual value and an approximated value.
- **Rounded and Chopped Outputs:** Displays the approximated value and errors in both rounded and chopped formats.
- **Support for constants and square root function:** Recognizes constants like `pi`, `e`, and evaluates square root expressions.
- **Customizable Decimal Precision:** Users can specify the number of decimal places for the results.

## Prerequisites

Ensure you have the following installed on your system:
- Python 3.x
- Streamlit library

You can install Streamlit using pip:
```bash
pip install streamlit
```

## How to Run

1. **Clone the repository** or copy the code into a Python script.
2. **Navigate** to the directory containing the script.
3. **Run the Streamlit app** by executing the following command:
   ```bash
   streamlit run your_script_name.py
   ```
   Replace `your_script_name.py` with the name of the file containing the code.

4. **Open your web browser**, and Streamlit will automatically open the application interface at `http://localhost:8501`.

## Application Interface

### Calculator Tab
- **Actual Value Expression:** Enter the mathematical expression representing the actual value.
- **Approximated Value Expression:** Enter the mathematical expression representing the approximated value.
- **Number of Decimal Places:** Specify the number of decimal places for rounding or chopping the output.
- **Calculate Button:** Click to compute and display the results, including rounded and chopped approximated values, absolute errors, and relative errors.

### Guide Tab
The guide provides information on:
- The format for inputting expressions.
- Supported operators.
- Predefined constants (`pi`, `e`) and functions like `sqrt` (square root).

### Example Input
- **Actual Value Expression:** `(pi + 2) * sqrt(5) / 3`
- **Approximated Value Expression:** `3.14159 + 2`

### Operators
Supported operators include:
- `+` for addition
- `-` for subtraction
- `*` for multiplication
- `/` for division
- `**` for exponentiation (e.g., 2 ** 3 equals 8)

## Error Calculation Logic

- **Absolute Error:** `|actual_value - approximated_value|`
- **Relative Error:** `|actual_value - approximated_value| / actual_value`

## License
This project is provided as-is, without any warranty. You are free to modify and distribute the code as needed.

---

Enjoy using the error calculator!# MachineProb1
