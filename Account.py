 num_accounts = 0
  def __init__(self, account_number, balance, owner):
    # Instance variables
    self.account_number = account_number
    self.balance = balance
    self.owner = owner
    # Increment the number of accounts
    Account.num_accounts += 1
  def deposit(self, amount):
    self.balance += amount
  def withdraw(self, amount):
    if amount <= self.balance:
      self.balance -= amount
    else:
      print("Insufficient funds.")
  def get_account_number(self):
    return self.account_number
  def get_balance(self):
    return self.balance
  def get_owner(self):
    return self.get_owner


    Add attributes deposits and withdrawals in the init method which are empty lists
 by default and another attribute loan_balance which is zero by default.
 Class Account:
 def__init__(self):
    self.deposits=[]
    self.withdrawals=[]
    self.loan_balance=0

Add a method check_balance which returns the account’s balance



def__init__(self,deposit=None,withdrawals,loan_balance=0):
    self.deposits=deposit[]
    self.withdrawals=withdrawals[]
    self.loan_balance=0
    
def chack_balance(self):
    return self.loan_balance


Update the deposit method to append each withdrawal transaction to the deposits list.
 Each transaction should be in form of a dictionary like this  
{
   "amount": amount,
   "narration": “deposit”
}
def deposit(self,amount):
    transaction={"amount":amount,"naration":"deposit"}
    self.deposits.append(transaction)
    self.loan_balance +=amount



Update the withdrawal method to append each withdrawal transaction to the withdrawals list. 
Each transaction should be in form of a dictionary like like this 
{
   "amount": amount,
   "narration": “withdrawal”
}
def withdrawals(self,amount):
    if self.loan_balance>=amount
    transaction={"amount":amount,"naration":"withdrawal"}
   self.withdrawals.append(transaction)
   self.loan_balance -=amount
   else:
    print(Insufficient funds)
 

Add a new method  print_statement which combines both deposits and withdrawals into one list and, 
using a for loop, prints each transaction in a new line like this
deposit - 1000
withdrawal - 500

def print_statement(self):
    transactions=self.deposits + self.withdrawals
    sorted_transactions = sorted(transactions,key=lambda key: k['date'])
    

    for transactions in sorted_transactions:
        print(f"{transaction['naration']} -{transaction['amount']}")


Add a borrow_loan method which allows a customer to borrow if they meet these conditions:
Account has no outstanding loan
Loan amount requested is more than 100
Customer has made at least 10 deposits.
Amount requested is less than or equal to 1/3 of their total sum of all deposits.
A successful loan increases the loan_balance by requested amount

def borrow_loan(self,loan_amount):
    if self_loan_balance==0 and loan_amount >100 and len (self.deposits) >=10:
        total_deposits = sum([transaction['amount'] for transaction in self.deposits])

        if loan_amount <= total_deposits/3:
            transaction = {"amount":loan_amount,"naration":"loan"}
            self.withdrawals.append(transaction)
            self.loan_balance +=loan_amount

            else:
                print("loan amount exceeds 1/3 of total deposits")

            else:
                print("Cannot borrow a loan.")    



Add a repay_loan method with this functionality
A customer can repay a loan to reduce the current loan_balance
Overpayment of a loan increases the accounts current balance

def repay_loan(self,repayment_amount):
    if self.loan_balance >0:
        if repayment_amount <=




Add a transfer method which accepts two attributes (amount and instance of another account).
 If the amount is less than the current instances balance, the method transfers the requested amount 
 from the current account to the passed account. The transfer is accomplished by reducing the current 
 account balance and depositing the requested amount to the passed account.

    def repay_loan(self_amount):
        if self.loan_balance >= amount:
            self.loan_balance -= amount
            self.transactions.append({"type":"repayment","amount": amount})
            
            else:
                self.balance +=(amount - self_loan_balance)
                self.transactions.append({"type": "overpayment", "amount": amount, 
                "overpaid_amount": (amount - self.balance.balance)})
                self.loan_balance = 0

    
    
    

