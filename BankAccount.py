
class BankAccount():
  def __init__(self, full_name, account_number, balance=0):
    self.full_name = full_name
    self.account_number = account_number
    self.balance = balance

  def deposit(self, amount):
    self.balance += amount 
    print(f'Amount deposited: ${amount}')
    print(f'New Account Balance: ${self.balance}\n')

  def withdraw(self, amount): #IF STATEMENT
    if self.balance > amount:
      self.balance -= amount
      print(f'Amount Withdrawn: ${amount}')
      print(f'New Account Balance: ${self.balance}\n')
    else:
      print('Cannot complete transaction: INSUFFICIENT FUNDS')
      print('A $10 overdraft fee has been applied to your account.\n')
      print(f'Current Account Balance: ${self.balance - 10}')

  def get_balance(self):
    print(f'Account Balance: ${self.balance}')
    return self.balance

  def print_details(self):
    print(self.full_name)
    print(f'Account No.: {self.account_number}')
    self.get_balance()

tayAccount = BankAccount("Taylor", "444")
#tayAccount.print_details()
tayAccount.get_balance() 
tayAccount.deposit(11)
#tayAccount.print_details()
#tayAccount.withdrawal(9)
tayAccount.withdraw(90) #testing else statement#
#tayAccount.print_details()