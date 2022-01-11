import os
import sys


class Budget(object):
    def __init__(self):
        os.system('cls')
        self.budget = float(input("What is your budget?\n"))
        #50-30-20 rule where 20 is savings
        self.spending = self.budget * 0.5
        self.returnBudget()

    def returnBudget(self):
        os.system('cls')
        print("Your total budget is:\n$", '{:.2f}'.format(self.budget))
        print("======================")
        print("Pick an option below")
        print("======================")
        main_options = int(input("1: View Overall Budget\n2: View Spending Budget\n"))

        if main_options == 1:
            self.overallBudget()
        elif main_options == 2:
            # spending budget is 50%
            self.spendingBudget()
        else: 
            quit

    def overallBudget(self):
        os.system('cls')
        options = int(input("How much would you like to save?\n1: 20%\n2: 30%\n"))
        if options == 1:
            self.savingPercentage = 0.2
        elif options == 2:
            self.savingPercentage = 0.3
        else: 
            print("Select one of the options provided")

        self.finalSavings = self.budget * self.savingPercentage
        self.Remaining = self.budget - self.finalSavings - self.spending
        print("\nSpending: %s\nSaving: %s\nRemaining: %s\n" % (self.spending, self.finalSavings, self.Remaining))
        os.system('pause')
        self.returnBudget()

    def spendingBudget(self):
        os.system('cls')
        print("Spending Budget: %s" % (self.spending))
        rent = float(input("What is your monthly rent?\n"))
        bills = float(input("What are your monthly bills?\n"))
        groceryMoney = self.spending - rent - bills
        print("Your current Expenses are:\nRent: %s\nBills: %s\nGroceries: %s" % (rent, bills, groceryMoney))
        os.system('pause')
        self.returnBudget()


Budget()