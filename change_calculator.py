class ChangeCalc:
  """value settings for paper money and coins and counting marker for each"""
  def __init__(self):
    self.hundreds = 10000
    self.fifties = 5000
    self.twenties = 2000
    self.tens = 1000
    self.fives = 500
    self.ones = 100
    self.quarters = 25
    self.dimes = 1
    self.nickels = 5
    self.pennies = 1
    self.hundred_count = 0
    self.fifty_count = 0
    self.twenty_count = 0
    self.ten_count = 0
    self.five_count = 0
    self.one_count = 0
    self.quarter_count = 0
    self.dime_count = 0
    self.nickel_count = 0
    self.penny_count = 0

  
  def calc_change(self, change):
    """calculates the number of bills and coins and returns a tuple
       starting with hundreds down to pennies in descending order"""
          
    while change >= 10000:
      change -= 10000
      self.hundred_count += 1
    while change >= 5000:
      change -= 5000
      self.fifty_count += 1
    while change >= 2000:
      change -= 2000
      self.twenty_count += 1
    while change >= 1000:
      change -= 1000
      self.ten_count += 1
    while change >= 500:
      change -= 500
      self.five_count += 1
    while change >= 100:
      change -= 100
      self.one_count += 1
    while change >= 25:
      change -= 25
      self.quarter_count += 1
    while change >= 10:
      change -= 10
      self.dime_count += 1
    while change >= 5:
      change -= 5
      self.nickel_count += 1
    while change >= 1:
      change -= 1
      self.penny_count += 1
    return (self.hundred_count, self.fifty_count, 
    self.twenty_count, self.ten_count, self.five_count, 
    self.one_count, self.quarter_count, self.dime_count, 
    self.nickel_count, self.penny_count)
  
  def display_change(self, bill_count):
    """display the amount of each currency bill or
    coin to be given back to the customer"""
    print(f'{bill_count[0]} Hundreds')
    print(f'{bill_count[1]} Fifties')
    print(f'{bill_count[2]} Twenties')
    print(f'{bill_count[3]} Tens')
    print(f'{bill_count[4]} Fives')
    print(f'{bill_count[5]} Ones')
    print(f'{bill_count[6]} Quarters')
    print(f'{bill_count[7]} Dimes')
    print(f'{bill_count[8]} Nickels')
    print(f'{bill_count[9]} Pennies')
    
while True:      
  my_change = ChangeCalc()
  total_bill = float(input('Please enter the total bill.\n'))
  total_bill = int(total_bill*100)
  payment = float(input('Please enter your payment.\n'))
  payment = int(payment*100)
  print('-'*30)
  bill_count = my_change.calc_change(payment -total_bill)
  my_change.display_change(bill_count)
  quit = input("Press 'q' to quit. Press Enter to continue.\n\n")
  print('\n\n')
  if quit == "q":
    break
