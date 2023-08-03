''' This script contains all the basic elements needed to build the yield calculator. '''
import tkinter as tk
from tkinter import messagebox

capital_initial_entry = None
apports_periodiques_entry = None
taux_rendement_annuel_entry = None
duree_investissement_entry = None

def collect_user_informations():
    print("Investment return calculator")
    print("=========================================")

    initial_capital = float(input("Enter initial amount invested : "))
    periodic_inputs = float(input("Enter the periodic inputs (0 if not) : "))
    annual_yield = float(input("Enter the annual yield (in decimal form) : "))
    investment_term = int(input("Enter the investment duration : "))

    return initial_capital, periodic_inputs, annual_yield, investment_term

def future_value_calculation():
    try:
        initial_capital = float(capital_initial_entry.get())
        periodic_inputs = float(apports_periodiques_entry.get())
        annual_yield = float(taux_rendement_annuel_entry.get())
        investment_term = int(duree_investissement_entry.get())

        future_value = initial_capital * (1 + annual_yield) ** investment_term
        if periodic_inputs > 0:
            future_value += periodic_inputs * (((1 + annual_yield) ** investment_term - 1) / annual_yield)

        print_results(future_value, future_value - initial_capital - periodic_inputs * investment_term)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid values.")

def print_results(future_value, total_return):
    print("\nResults")
    print("=========================================")
    print(f"Total amount at end of period : {future_value:.2f} €")
    print(f"Total return obtained : {total_return:.2f} €")
    messagebox.showinfo("Results",
                        f"Total amount at end of period : {future_value:.2f} €\nTotal return obtained: {total_return:.2f} €")

def create_interface():
    global capital_initial_entry, apports_periodiques_entry, taux_rendement_annuel_entry, duree_investissement_entry

    window = tk.Tk()
    window.title("Investment_Return_Calculator")

    # Initial amount
    tk.Label(window, text="Initial amount :").grid(row=0, column=0, padx=5, pady=5)
    capital_initial_entry = tk.Entry(window)
    capital_initial_entry.grid(row=0, column=1, padx=5, pady=5)

    # Periodic inputs
    tk.Label(window, text="Periodic inputs :").grid(row=1, column=0, padx=5, pady=5)
    apports_periodiques_entry = tk.Entry(window)
    apports_periodiques_entry.grid(row=1, column=1, padx=5, pady=5)

    # Annual yield
    tk.Label(window, text="Annual yield :").grid(row=2, column=0, padx=5, pady=5)
    taux_rendement_annuel_entry = tk.Entry(window)
    taux_rendement_annuel_entry.grid(row=2, column=1, padx=5, pady=5)

    # Investment term
    tk.Label(window, text="Investment term (in years) :").grid(row=3, column=0, padx=5, pady=5)
    duree_investissement_entry = tk.Entry(window)
    duree_investissement_entry.grid(row=3, column=1, padx=5, pady=5)

    calcul_button = tk.Button(window, text="Calculate", command=future_value_calculation)
    calcul_button.grid(row=5, columnspan=2, padx=5, pady=10)
    window.mainloop()

if __name__ == "__main__":
    create_interface()
