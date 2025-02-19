"""Utilities 5%
Rent/Housing 15%
Transportation 30%
Healthcare 3%
Groceries 10%
Communication 2%"""

"""The application must determine:
Monthly income tax, and gross income after tax (using the tax table information below)
The amount payable for each expense category, and the total expenses
The net income (after tax and expenses)"""

class BudgetCalculator:
    def __init__(self):
        self.user_code = None
        self.gross_salary = 0
        self.tax = 0
        self.expenses = {
            "Utilities": 0.05,
            "Rent/Housing": 0.15,
            "Transportation": 0.30,
            "Healthcare": 0.03,
            "Groceries": 0.10,
            "Communication": 0.02
        }
        self.net_salary = 0
        

    def add_entry(self,user_code, gross_salary):
        self.user_code = user_code
        self.gross_salary = gross_salary
        self.calculate_tax()
        # self.calculate_expenses()
        # self.net_salary = self.gross_salary - self.tax - self.expenses
    
    def calculate_tax(self):
        taxable_income = self.gross_salary * 12
        if taxable_income <= 237100:
            self.tax = 0.18 * taxable_income
        elif taxable_income >= 237101 and taxable_income <= 370500:
            taxable_income = taxable_income - 237100
            self.tax = (0.26 * taxable_income) + 42678
        elif taxable_income >= 370501 and taxable_income <= 512800:
            taxable_income = taxable_income - 370500
            self.tax = (0.31 * taxable_income) + 77362
        elif taxable_income >= 512801 and taxable_income <= 673000:
            taxable_income = taxable_income - 512800
            self.tax = (0.36 * taxable_income) + 121475
        elif taxable_income >= 673001 and taxable_income <= 857900:
            self.tax = (0.39 * taxable_income) + 179147
        elif taxable_income >= 857901 and taxable_income <= 1817000:
            self.tax = (0.41 * taxable_income) + 251258
        elif taxable_income >= 1817001:
            self.tax = (0.45 * taxable_income) + 644489
    
    def calculate_expenses(self):    
        pass        
    
    def display_budget(self):
            print("Monthly Budget")
            print("________________________________________\n")
            print("Income")
            print("________________________________________\n")
            print(f"Gross Monthly Income (Before Tax): R{self.gross_salary}")
            print("Gross Monthly Income (After Tax): R")
            print("________________________________________\n")
            print("Expenses")
            print("________________________________________\n")
            

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
            # netSalary = grossSalary - budget.calculate_tax()
            budget.add_entry(user_code, gross_salary)
            budget.calculate_tax()
            print(f"\nMonthly Tax Payable: R{budget.tax/12}\n")
            budget.display_budget()
            
            
        elif choice == 0:
            print("Cheers!")
            break
        else:
            print("Please select a valid option.")
            
if __name__ == "__main__":
    main()