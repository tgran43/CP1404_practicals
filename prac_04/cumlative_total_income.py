"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    no_of_months = int(input("How many months? "))

    for month in range(1, no_of_months + 1):
        income = float(input("Enter income for month {}: ".format(month)))
        incomes.append(income)

    report_printing(incomes)


def report_printing(incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, len(incomes) + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()
