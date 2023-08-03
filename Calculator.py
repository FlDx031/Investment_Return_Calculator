''' This script contains all the basic elements needed to build the yield calculator. '''
import math

def collect_user_informations():
    print("Investement return calculator")
    print("=========================================")

    initial_capital = float(input("Enter initial amount invested : "))
    periodic_inputs = float(input("Enter the periodic inputs (0 if not) : "))
    annual_yield = float(input("Enter the annual yield (in decimal form) : "))
    investment_term = int(input("Enter the investment duration : "))

    return initial_capital, periodic_inputs, annual_yield, investment_term
def future_value_calculation(initial_capital, periodic_inputs, annual_yield, investment_term):
    future_value = initial_capital * (1 + annual_yield) ** investment_term
    if periodic_inputs > 0:
        future_value += periodic_inputs * (((1 + annual_yield) ** investment_term - 1) / annual_yield)
    return future_value

def print_results(future_value, total_return):
    print("\nResults")
    print("=========================================")
    print(f"Total amount at end of period : {future_value:.2f} €")
    print(f"Total return obtained : {total_return:.2f} €")

if __name__ == "__main__":
    initial_capital, periodic_inputs, annual_yield, investment_term = collect_user_informations()
    future_value = future_value_calculation(initial_capital, periodic_inputs, annual_yield, investment_term)
    total_return = future_value - initial_capital - periodic_inputs * investment_term
    print_results(future_value, total_return)

