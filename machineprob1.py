import streamlit as st
import math
from fractions import Fraction

#   Function for the basic math operations
def calculate_result(num1, operator, num2):
    result = None

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    elif operator == '**':
        result = num1 ** num2

    return result

#   Function for the absolute error
def calculate_absolute_error(actual_value, approximated_value):
    absolute_error = abs(actual_value - approximated_value)
    return absolute_error

#   Function for the relative  error
def calculate_relative_error(actual_value, approximated_value):
    relative_error = abs((actual_value - approximated_value) / actual_value)
    return relative_error

#   Converts the user input(pi,euler,sqrt)
def replace_constants(expression):
    constants = {
        'pi': str(math.pi),
        'e': str(math.e),
    }

    for constant, value in constants.items():
        expression = expression.replace(constant, value)

    while 'sqrt(' in expression:
        start = expression.find('sqrt(')
        end = expression.find(')', start)
        sub_expression = expression[start+5:end]
        evaluated = math.sqrt(float(sub_expression))
        expression = expression[:start] + str(evaluated) + expression[end+1:]

    return expression

#   Function for evaluating the expression, if the user input has parenthesis and replacing constants into the converted constants
def evaluate_expression(expression):
    try:
        expression = replace_constants(expression)
        return eval(expression)
    except (ValueError, ZeroDivisionError, SyntaxError, NameError):
        return None
        
#   To handle errors
def evaluate_sub_expression(expression):
    try:
        return eval(expression)

    except (ValueError, ZeroDivisionError, SyntaxError, NameError):
        return None

#   Main function
def main():
    tab1, tab2 = st.tabs(["Calculator", "Guide"])
    with tab1:
        st.title("Error Calculator")
        st.write("Enter the expressions for the actual value and the approximated value.")

        actual_expression = st.text_input("Actual Value Expression")
        approx_expression = st.text_input("Approximated Value Expression")

        decimal_places = st.number_input("Number of Decimal Places", min_value=0, max_value=15, value=0)

        actual_value = evaluate_expression(actual_expression)
        approximated_value = evaluate_expression(approx_expression)

        if actual_value is not None:
            st.write("Actual Value:", actual_value)

        if approximated_value is not None:
            st.write("Approximated Value:", approximated_value)

        if st.button("Calculate") and actual_value is not None and approximated_value is not None:

            st.markdown("## Rounded Output")
            rounded_output = round(approximated_value, decimal_places)

            absolute_error_rounded = calculate_absolute_error(actual_value, rounded_output)
            relative_error_rounded = calculate_relative_error(actual_value, rounded_output)
            
            st.write("Rounded Approximated Value:", rounded_output)
            st.write("Rounded Absolute Error:", absolute_error_rounded)
            st.write("Rounded Relative Error:", f"{relative_error_rounded * 100}%")

            st.markdown("## Chopped Output")
            
            chopped_output = math.trunc(approximated_value * (10 ** decimal_places)) / (10 ** decimal_places)

            absolute_error_chopped = calculate_absolute_error(actual_value, chopped_output)
            relative_error_chopped = calculate_relative_error(actual_value, chopped_output)

            st.write("Chopped Approximated Value:", chopped_output)
            st.write("Chopped Absolute Error:", absolute_error_chopped)
            st.write("Chopped Relative Error:", f"{relative_error_chopped * 100}%")
    with tab2:
        st.header("Guide")
        st.subheader("Input Format")
        st.write("Use the format 'expression operator expression' for the actual value and the approximated value.")
        st.write("You can use parentheses to group sub-expressions.")
        st.write("Available commands: pi, e, sqrt")
        st.write("Example: (pi + 2) * sqrt(5) / 3")
        st.write("Max value for decimal places is 15.")

        st.subheader("Operators")
        st.write("Supported operators:")
        st.write("- Addition: `+`")
        st.write("- Subtraction: `-`")
        st.write("- Multiplication: `*`")
        st.write("- Division: `/`")
        st.write("- Power: `**`")

if __name__ == "__main__":
    main()
