
class BankAccount():
  def __init__(self, full_name, account_number, balance=0):
    self.full_name = full_name
    self.account_number = account_number
    self.balance = balance

  def deposit(self, amount):
    self.balance += amount 
    print(f'Amount deposited: ${amount}')
    print(f'New Account Balance: ${self.balance}\n')

  #def withdrawal(self, amount): IF STATEMENT

  def get_balance(self):
    print(f'Account Balance: ${self.balance}')
    return self.balance

  def print_details(self):
    print(self.full_name)
    print(f'Account No.: {self.account_number}')
    self.get_balance()

#tayAccount = BankAccount("Taylor", "444")
#tayAccount.print_details()
#tayAccount.get_balance() still returnign zero, need to add deposit/withdrawl
#tayAccount.deposit(11)
#tayAccount.print_details()