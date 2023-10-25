
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

  def add_interest(self):
    self.balance * 0.00083
    print(f'Interest applied. New Account Balance: ${self.balance}')

  def print_statement(self):
    print(self.full_name)
    print(f'Account No.: {self.account_number}')
    self.get_balance()



MitchellAccount = BankAccount("Mitchell", "03141592")
MitchellAccount.deposit(400000)
MitchellAccount.print_statement()
MitchellAccount.add_interest()
MitchellAccount.print_statement()
MitchellAccount.withdraw(150)
MitchellAccount.print_statement()



#tayAccount = BankAccount("Taylor", "444")
#tayAccount.print_statement()
#tayAccount.get_balance() 
#tayAccount.deposit(11)
#tayAccount print_statement()
#tayAccount.withdrawal(9)
#tayAccount.withdraw(90) #testing else statement#
#tayAccount print_statement()
#tayAccount.print_statement()
#tayAccount.add_interest()