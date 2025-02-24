class BudgetCalculator:
    def __init__(self):
        self.user_code = None
        self.gross_salary = 0
        self.tax = 0
        self.expense_percentages = {
            "Utilities": 0.05,
            "Rent/Housing": 0.15,
            "Transportation": 0.30,
            "Healthcare": 0.03,
            "Groceries": 0.10,
            "Communication": 0.02
        }
        self.expense_amounts = {}
        self.net_salary = 0

    def add_entry(self, user_code, gross_salary):
        self.user_code = user_code
        self.gross_salary = gross_salary
        self.calculate_tax()
        self.calculate_expenses()
        self.net_salary = self.gross_salary - (self.tax / 12) - sum(self.expense_amounts.values())

    def calculate_tax(self):
        taxable_income = self.gross_salary * 12
        if taxable_income <= 237100:
            self.tax = 0.18 * taxable_income
        elif 237101 <= taxable_income <= 370500:
            taxable_income = taxable_income - 237100
            self.tax = (0.26 * taxable_income) + 42678
        elif 370501 <= taxable_income <= 512800:
            taxable_income = taxable_income - 370500
            self.tax = (0.31 * taxable_income) + 77362
        elif 512801 <= taxable_income <= 673000:
            taxable_income = taxable_income - 512800
            self.tax = (0.36 * taxable_income) + 121475
        elif 673001 <= taxable_income <= 857900:
            taxable_income = taxable_income - 673000
            self.tax = (0.39 * taxable_income) + 179147
        elif 857901 <= taxable_income <= 1817000:
            taxable_income = taxable_income - 857900
            self.tax = (0.41 * taxable_income) + 251258
        elif taxable_income >= 1817001:
            taxable_income = taxable_income - 1817000
            self.tax = (0.45 * taxable_income) + 644489

    def calculate_expenses(self):
        gross_after_tax = self.gross_salary - (self.tax / 12)
        for category, percentage in self.expense_percentages.items():
            self.expense_amounts[category] = gross_after_tax * percentage

    def display_budget(self):
        print("\nMONTHLY BUDGET")
        print("________________________________________\n")
        print("INCOME\n")
        print(f"Gross Monthly Income (Before Tax): R{self.gross_salary:.2f}")
        print(f"Gross Monthly Income (After Tax): R{self.gross_salary - (self.tax / 12):.2f}")
        print("________________________________________\n")
        print("TAX PAYABLE")
        print(f"\nMonthly Tax Payable: R{self.tax / 12:.2f}")
        print("________________________________________\n")
        print("EXPENSES\n")
        total_expenses = 0
        for category, amount in self.expense_amounts.items():
            print(f"{category}: R{amount:.2f}")
            total_expenses += amount
        print(f"Total Expenses: R{total_expenses:.2f}")
        print("________________________________________\n")
        print("NET INCOME\n")
        print(f"Net Income after expenses & tax: R{self.net_salary:.2f}")
        print("________________________________________\n")
        print("*********END*********")

def main():
    budget = BudgetCalculator()

    while True:
        print("\nWelcome to BE.2022.V6T6C1's budget calculator!")
        print("________________________________________")
        print("\n1. Create New Entry")
        print("0. Exit\n")

        choice = int(input("Select an option: "))

        if choice == 1:
            print("\nLet's create a new entry!")
            user_code = input("Enter your code: ")
            gross_salary = float(input("Enter your gross salary: "))
            budget.add_entry(user_code, gross_salary)
            budget.display_budget()
        elif choice == 0:
            print("Cheers!")
            break
        else:
            print("Please select a valid option.")

if __name__ == "__main__":
    main()