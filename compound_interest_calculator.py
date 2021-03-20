"""Author: Simon Zhang

   Date: Dec 14, 2020

   Description: This program calculates the future amount of an investment with
   compound interest.
"""

def main():
    """This function defines the mainline logic of the program and takes the values for the
    principal, interest rate, compounding period, and years invested from the user."""

    print("""
Given the principal, interest rate, number of years and number of compounding periods,
this program will determine the future value of the investment.
""")

    principal = float(input("Enter the principal amount in dollars: "))

    # divide the interest rate by 100 to convert to decimal
    interest_rate = float(input("Enter the interest rate as a percentage: "))/100

    # prints a list of options for compounding periods
    print("""
    1. Annually (1 time/year)
    2. Semi-annually (2 times/year)
    3. Quarterly (4 times/year)
    4. Monthly (12 times/year)
    5. Bi-Weekly (26 times/year)
    6. Weekly (52 times/year)
    7. Daily (365 times/year)
    """)

    # prompts the user for a number corresponding to the compounding period on the list above
    compounding_period_choice = int(input("Enter the number corresponding to the compounding periods: "))

    # list containing the number of times a year each compounding period respresents
    times_per_year = [1, 2, 4, 12, 26, 52, 365]

    # converts number the user chose from the compounding choices to the number of times a year
    compounding_period = times_per_year[compounding_period_choice - 1]

    years = int(input("Enter the number of years the principal is being invested: "))

    future_amount = calculate_future_amount(principal, interest_rate, compounding_period, years)

    display_result(future_amount)

def calculate_future_amount(principal, interest_rate, compounding_period, years):
    """This function takes the values for the principal, interest rate,
    number of times interest applied per time period, and number of years and returns
    the future amount of the investment."""

    # Formula for future value compound interest: A = P(1+r/n)^(nt)
    future_amount = round((principal * (1 + interest_rate/compounding_period) ** (compounding_period * years)), 2)

    return future_amount

def display_result(future_amount):
    """This function takes the value of future amount of the investment and prints it
    as a message."""

    print("The future value of the investment is: $" + str(future_amount))

main()