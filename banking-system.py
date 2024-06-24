
def show_balance(balance):
  print('***********************')
  print(f"Your balance is ${balance:.2f}")
  print('***********************')

def deposit():
  amount = float(input("Enter an amount to be deposited: "))
  
  if amount < 0:
    print("That's not a valid amount!")
    return 0
  else:
    return amount


def withdraw(balance):
  amount = float(input("Enter an amount to be withdrawn: "))
  
  if amount < 0:
    print("That's not a valid amount!")
    return 0
  elif amount > balance:
    print("Insufficient funds")
    return 0
  else:
    return amount
  
def main():
  balance = 0
  is_running = True

  while is_running:
    print('************************************')
    print('Your Bank Account System Is Running!')
    print('************************************')

    print('Banking Program')
    print('1.Balance')
    print('2.Deposit')
    print('3.Withdraw')
    print('4.Exit')
    print('***********************')

    choice = input("Enter Your Choice (1-4): ")

    if choice == '1':
      show_balance(balance)
    elif choice == '2':
      balance += deposit()
    elif choice == '3':
      balance -= withdraw(balance)
    elif choice == '4':
      is_running = False
    else:
      print("That is not a valid choice: ")

  print("Thank you!")
  print("Have a nice day!")

main()
