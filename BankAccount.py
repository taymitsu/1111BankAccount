
class BankAccount(self, full_name, account_number, balance=0):
  self.full_name = full_name
  self.account_number = account_number
  self.balance = balance

  def get_balance(self):
    print(f'Account Balance: {self.balance}')
    return self.balance

  def print_details(self):
    print(self.full_name)
    print(f'Account No.: {self.account_number}')
    self.get_balance()