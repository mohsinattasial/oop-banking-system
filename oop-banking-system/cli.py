from src.bank import Bank
from src.account import SavingsAccount, CurrentAccount

bank = Bank()

while True:

    print("\n1 Open Savings Account")
    print("2 Open Current Account")
    print("3 Deposit")
    print("4 Withdraw")
    print("5 Transfer")
    print("6 Show Balance")
    print("7 Exit")

    choice = input("Choose: ")

    if choice == "1":

        acc_id = input("Account ID: ")
        owner = input("Owner Name: ")

        acc = SavingsAccount(acc_id, owner)
        bank.open_account(acc)

        print("Savings account created")

    elif choice == "2":

        acc_id = input("Account ID: ")
        owner = input("Owner Name: ")

        acc = CurrentAccount(acc_id, owner)
        bank.open_account(acc)

        print("Current account created")

    elif choice == "3":

        acc_id = input("Account ID: ")
        amount = float(input("Amount: "))

        acc = bank.get_account(acc_id)
        acc.deposit(amount)

        print("Deposit successful")

    elif choice == "4":

        acc_id = input("Account ID: ")
        amount = float(input("Amount: "))

        acc = bank.get_account(acc_id)
        acc.withdraw(amount)

        print("Withdraw successful")

    elif choice == "5":

        from_id = input("From Account: ")
        to_id = input("To Account: ")
        amount = float(input("Amount: "))

        bank.transfer(from_id, to_id, amount)

        print("Transfer successful")

    elif choice == "6":

        acc_id = input("Account ID: ")
        acc = bank.get_account(acc_id)

        print("Balance:", acc.get_balance())

    elif choice == "7":
        break