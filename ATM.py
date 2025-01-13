<<<<<<< HEAD
balance = 10000
pin = 2345
print("Wel Come To SBI ATM")
user_input = 1
print("Please Insert Your Card\n1.Yes\n2.No")
choice = int(input())
if choice == 1:
    print("Select Your Language")
    lan = int(input("1.English\n2.Hindi\n3.Kannada\n"))
    new_pin = int(input("Enter Your PIN\n"))
    if lan == 1:
        print("Your selecting English language")
        if new_pin == pin:
            while user_input == 1:
                print("1.Balance\n2.Withdrawal\n3.Deposit\n4.Set new PIN")
                choice = int(input())
                if choice == 1:
                    print("Balance  ₹",balance)
                elif choice == 2:
                    amount = int(input("Enter Withdrawal Amount\n"))
                    if amount % 100 == 0 and amount < balance:
                        balance -= amount
                        print("Withdrawal Amount ₹ ",amount,"\nTransaction Successfully\nVisit again Thank You!!")
                        print("Check Your Remaining Balance 'Yes' or 'No'")
                        choice = input()
                        if choice == "yes":
                            print("Remaining Balance ₹ ",balance)
                        else:
                            print("Thank You Visit again!!")
                    else:
                        print("Amount only Multiple of 100")
                elif choice == 3:
                    deposit = int(input("Enter Deposit Amount\n"))
                    if deposit % 100 == 0 and deposit < balance:
                        balance += deposit
                        print("Deposit Amount ₹",deposit)
                        print("Check Your Total Balance 'Yes' or 'No'")
                        choice = input()
                        if choice == "yes":
                            print("Total Balance ₹ ", balance)
                        else:
                            print("Thank You Visit again!!")
                    else:
                        print("Amount only Multiple of 100")
                elif choice == 4:
                    new_pin = int(input("Enter New PIN\n"))
                    print("New PIN Generate Successfully")
                else:
                    print("Invalid choice!")
                print("Do you Want Continue\n1.Yes\n2.No")
                user_input = int(input())
                if user_input == 1:
                    user_input = 1
                elif user_input == 2:
                    user_input = 2
        else:
            print("Wrong PIN!!")

    elif lan == 2:
        print("Your selecting Hindi language")
        if new_pin == pin:
            while user_input == 1:
                print("1.Balance\n2.Withdrawal\n3.Deposit\n4.Set new PIN")
                choice = int(input())
                if choice == 1:
                    print("Balance  ₹", balance)
                elif choice == 2:
                    amount = int(input("Enter Withdrawal Amount\n"))
                    if amount % 100 == 0 and amount < balance:
                        balance -= amount
                        print("Withdrawal Amount ₹ ", amount, "\nTransaction Successfully\nVisit again Thank You!!")
                        print("Check Your Remaining Balance 'Yes' or 'No'")
                        choice = input()
                        if choice == "yes":
                            print("Remaining Balance ₹ ", balance)
                        else:
                            print("Thank You Visit again!!")
                    else:
                        print("Amount only Multiple of 100")
                elif choice == 3:
                    deposit = int(input("Enter Deposit Amount\n"))
                    if deposit % 100 == 0 and deposit < balance:
                        balance += deposit
                        print("Deposit Amount ₹", deposit)
                        print("Check Your Total Balance 'Yes' or 'No'")
                        choice = input()
                        if choice == "yes":
                            print("Total Balance ₹ ", balance)
                        else:
                            print("Thank You Visit again!!")
                    else:
                        print("Amount only Multiple of 100")
                elif choice == 4:
                    new_pin = int(input("Enter New PIN\n"))
                    print("New PIN Generate Successfully")
                else:
                    print("Invalid Choice!!")
                print("Do you Want Continue\n1.Yes\n2.No")
                user_input = int(input())
                if user_input == 1:
                    user_input = 1
                elif user_input == 2:
                    user_input = 2
        else:
            print("Wrong PIN!!")

    elif lan == 3:
        print("Your selecting Kannada language")
        if new_pin == pin:
            while user_input == 1:
                print("1.Balance\n2.Withdrawal\n3.Deposit\n4.Set new PIN")
                choice = int(input())
                if choice == 1:
                    print("Balance  ₹", balance)
                elif choice == 2:
                    amount = int(input("Enter Withdrawal Amount\n"))
                    if amount % 100 == 0 and amount < balance:
                        balance -= amount
                        print("Withdrawal Amount ₹ ", amount, "\nTransaction Successfully\nVisit again Thank You!!")
                        print("Check Your Remaining Balance 'Yes' or 'No'")
                        choice = input()
                        if choice == "yes":
                            print("Remaining Balance ₹ ", balance)
                        else:
                            print("Thank You Visit again!!")
                    else:
                        print("Amount only Multiple of 100")
                elif choice == 3:
                    deposit = int(input("Enter Deposit Amount\n"))
                    if deposit % 100 == 0 and deposit < balance:
                        balance += deposit
                        print("Deposit Amount ₹", deposit)
                        print("Check Your Total Balance 'Yes' or 'No'")
                        choice = input()
                        if choice == "yes":
                            print("Total Balance ₹ ", balance)
                        else:
                            print("Thank You Visit again!!")
                    else:
                        print("Amount only Multiple of 100")
                elif choice == 4:
                    new_pin = int(input("Enter New PIN\n"))
                    print("New PIN Generate Successfully")
                else:
                    print("Invalid Choice!!")
                print("Do you Want Continue\n1.Yes\n2.No")
                user_input = int(input())
                if user_input == 1:
                    user_input = 1
                elif user_input == 2:
                    user_input = 2
        else:
            print("Wrong PIN!!")
    else:
        print("Invalid Choice!!")
else:
    print("Please Insert Your Card!!")
print("Thank You Visit Again!!")
=======
balance = 10000
pin = 2345
print("Wel Come To SBI ATM")
user_input = 1
print("Please Insert Your Card\n1.Yes\n2.No")
choice = int(input())
if choice == 1:
    print("Select Your Language")
    lan = int(input("1.English\n2.Hindi\n3.Kannada\n"))
    new_pin = int(input("Enter Your PIN\n"))
    if lan == 1:
        print("Your selecting English language")
        if new_pin == pin:
            while user_input == 1:
                print("1.Balance\n2.Withdrawal\n3.Deposit\n4.Set new PIN")
                choice = int(input())
                if choice == 1:
                    print("Balance  ₹",balance)
                elif choice == 2:
                    amount = int(input("Enter Withdrawal Amount\n"))
                    if amount % 100 == 0 and amount < balance:
                        balance -= amount
                        print("Withdrawal Amount ₹ ",amount,"\nTransaction Successfully\nVisit again Thank You!!")
                        print("Check Your Remaining Balance 'Yes' or 'No'")
                        choice = input()
                        if choice == "yes":
                            print("Remaining Balance ₹ ",balance)
                        else:
                            print("Thank You Visit again!!")
                    else:
                        print("Amount only Multiple of 100")
                elif choice == 3:
                    deposit = int(input("Enter Deposit Amount\n"))
                    if deposit % 100 == 0 and deposit < balance:
                        balance += deposit
                        print("Deposit Amount ₹",deposit)
                        print("Check Your Total Balance 'Yes' or 'No'")
                        choice = input()
                        if choice == "yes":
                            print("Total Balance ₹ ", balance)
                        else:
                            print("Thank You Visit again!!")
                    else:
                        print("Amount only Multiple of 100")
                elif choice == 4:
                    new_pin = int(input("Enter New PIN\n"))
                    print("New PIN Generate Successfully")
                else:
                    print("Invalid choice!")
                print("Do you Want Continue\n1.Yes\n2.No")
                user_input = int(input())
                if user_input == 1:
                    user_input = 1
                elif user_input == 2:
                    user_input = 2
        else:
            print("Wrong PIN!!")

    elif lan == 2:
        print("Your selecting Hindi language")
        if new_pin == pin:
            while user_input == 1:
                print("1.Balance\n2.Withdrawal\n3.Deposit\n4.Set new PIN")
                choice = int(input())
                if choice == 1:
                    print("Balance  ₹", balance)
                elif choice == 2:
                    amount = int(input("Enter Withdrawal Amount\n"))
                    if amount % 100 == 0 and amount < balance:
                        balance -= amount
                        print("Withdrawal Amount ₹ ", amount, "\nTransaction Successfully\nVisit again Thank You!!")
                        print("Check Your Remaining Balance 'Yes' or 'No'")
                        choice = input()
                        if choice == "yes":
                            print("Remaining Balance ₹ ", balance)
                        else:
                            print("Thank You Visit again!!")
                    else:
                        print("Amount only Multiple of 100")
                elif choice == 3:
                    deposit = int(input("Enter Deposit Amount\n"))
                    if deposit % 100 == 0 and deposit < balance:
                        balance += deposit
                        print("Deposit Amount ₹", deposit)
                        print("Check Your Total Balance 'Yes' or 'No'")
                        choice = input()
                        if choice == "yes":
                            print("Total Balance ₹ ", balance)
                        else:
                            print("Thank You Visit again!!")
                    else:
                        print("Amount only Multiple of 100")
                elif choice == 4:
                    new_pin = int(input("Enter New PIN\n"))
                    print("New PIN Generate Successfully")
                else:
                    print("Invalid Choice!!")
                print("Do you Want Continue\n1.Yes\n2.No")
                user_input = int(input())
                if user_input == 1:
                    user_input = 1
                elif user_input == 2:
                    user_input = 2
        else:
            print("Wrong PIN!!")

    elif lan == 3:
        print("Your selecting Kannada language")
        if new_pin == pin:
            while user_input == 1:
                print("1.Balance\n2.Withdrawal\n3.Deposit\n4.Set new PIN")
                choice = int(input())
                if choice == 1:
                    print("Balance  ₹", balance)
                elif choice == 2:
                    amount = int(input("Enter Withdrawal Amount\n"))
                    if amount % 100 == 0 and amount < balance:
                        balance -= amount
                        print("Withdrawal Amount ₹ ", amount, "\nTransaction Successfully\nVisit again Thank You!!")
                        print("Check Your Remaining Balance 'Yes' or 'No'")
                        choice = input()
                        if choice == "yes":
                            print("Remaining Balance ₹ ", balance)
                        else:
                            print("Thank You Visit again!!")
                    else:
                        print("Amount only Multiple of 100")
                elif choice == 3:
                    deposit = int(input("Enter Deposit Amount\n"))
                    if deposit % 100 == 0 and deposit < balance:
                        balance += deposit
                        print("Deposit Amount ₹", deposit)
                        print("Check Your Total Balance 'Yes' or 'No'")
                        choice = input()
                        if choice == "yes":
                            print("Total Balance ₹ ", balance)
                        else:
                            print("Thank You Visit again!!")
                    else:
                        print("Amount only Multiple of 100")
                elif choice == 4:
                    new_pin = int(input("Enter New PIN\n"))
                    print("New PIN Generate Successfully")
                else:
                    print("Invalid Choice!!")
                print("Do you Want Continue\n1.Yes\n2.No")
                user_input = int(input())
                if user_input == 1:
                    user_input = 1
                elif user_input == 2:
                    user_input = 2
        else:
            print("Wrong PIN!!")
    else:
        print("Invalid Choice!!")
else:
    print("Please Insert Your Card!!")
print("Thank You Visit Again!!")
>>>>>>> fa9be5743cc4a04f7b15e533cdf7a533c32b9c66
