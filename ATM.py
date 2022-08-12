# Create Class of ATM
class atm:
    def __init__(self):
        self.current_balance = 5000  # Current balance

    def deposit(self):  # create deposit method
        deposit_amt = int(input("Enter Deposit Amount "))
        print("You have deposited ", deposit_amt, "amount")
        deposit_bal = deposit_amt + self.current_balance  # this deposited amount will add in current balance
        print("You have deposit :", deposit_amt, " &  balance is ", deposit_bal)

    def withdraw(self):
        withdraw_amt = int(input("Enter Withdraw Amount "))
        if withdraw_amt <= self.current_balance:  # condition if withdraw is less than current balance
            print("You have withdraw your amount ", withdraw_amt)
            withdraw_bal = self.current_balance - withdraw_amt
        else:
            print("You don't have enough balance")


# make function
def atm_machine():
    while True:
        # MAKE options to get vales from Users
        print(' 1. Deposit ,2. Withdraw, 3. Check Balance, 4. Exit ')
        ch = int(input("Enter Choice "))
        if ch == 3:
            print("Yours Current balance is ", obj.current_balance)
            d = input("Do You want to another Transaction ? Press 'Y' or press Enter to exit ")
            if d != 'y':
                break
        elif ch == 1:
            obj.deposit()
            d = input("Do You want to another Transaction ? Press 'Y' or press Enter to exit ")
            if d != 'y':
                break
        if ch == 2:
            obj.withdraw()
            d = input("Do You want to another Transaction ? Press 'Y' or press Enter to exit ")
            if d != 'y':
                break

        elif ch == 4:
            print("Thanks , BYE")
            exit()
            break


obj = atm()
atm_machine()
