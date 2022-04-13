# **********************************************************************
# Slide #9: Defining Loan Class
# **********************************************************************
class Loan:
  # The __init__ method hard codes mortgage attributes
  def __init__(self):
    self.int_rate = 0.045
    self.term = 30
    self.amount = 400000

  # The calc_mth_pmt function returns the monthly payment
  def calc_mth_pmt(self):
    mth_rate = self.int_rate / 12
    mth_term = 12 * self.term
    mth_pmt = (mth_rate)/(1-(1+mth_rate)**(-mth_term)) * self.amount
    return mth_pmt

def main():
  # Create an object from the Loan class
  my_mortg = Loan()

  # Extract the data from the object by directly accessing
  # public data attributes
  rate = my_mortg.int_rate
  print(f'Your mortgage has interest rate of {rate:.1%}')
  years = my_mortg.term
  amt = my_mortg.amount
  print(f'You borrowed ${amt:,.0f} for duration of {years} years.')
  
  # Calculate and display the monthly payment
  mth_pmt = my_mortg.calc_mth_pmt()
  print(f'Your current monthly payment is ${mth_pmt:,.2f}')

# **********************************************************************
# Slides #10-11: Redefining and Using Loan Class
# **********************************************************************
import loan

def main():
  # Get the interest rate, term, amount borrowed, and loan type
  rate = float(input('Enter interest rate between 0 and 1: '))
  years = int(input('Enter term of the loan in years: '))
  amt = float(input('Enter amount borrowed under 1 million: '))
  l_type = input('Enter loan type (Mortg, Car, Other): ')
  
  # Create an object from the Loan class
  my_loan = loan1.Loan(rate, years, amt, l_type)

  # Use get accessor methods to review the mortgage parameters
  l_type = my_loan.get_loan_type()
  rate = my_loan.get_int_rate()
  print(f'Your {l_type} has interest rate of {rate:.1%}')
  amt = my_loan.get_amount()
  years = my_loan.get_term()
  print(f'You borrowed ${amt:,.0f} for duration of {years} years.')

  # Calculate and display the monthly payment
  mth_pmt = my_loan.calc_mth_pmt()
  print(f'Your current monthly payment is ${mth_pmt:,.2f}')
  print()
  
  # Much later you owe 300,000 and you refinance at 4.0% for 15 years
  rate = float(input('Enter NEW interest rate between 0 and 1: '))
  years = int(input('Enter NEW term of the loan in years: '))
  amt = float(input('Enter NEW amount borrowed under 1 million: '))

  # Use the set mutator methods to change the mortgage parameters
  my_loan.set_int_rate(rate)
  my_loan.set_term(years)
  my_loan.set_amount(amt)

  # Check if there are any problems with the input
  if my_loan.get_int_rate() == 0 or \
     my_loan.get_term() == 0 or \
     my_loan.get_amount() == 0:
    print('ERROR: At least one of the 3 loan parameters is invalid!')
  else:
    # Recalculate the monthly payment
    mth_pmt = my_loan.calc_mth_pmt()
    print(f'Your NEW monthly payment is ${mth_pmt:,.2f}')

# **********************************************************************
# Slide #11: Using Enhanced Loan Class
# **********************************************************************
import loan1

def main():
  # Get the interest rate, term, amount borrowed, and loan type
  rate = float(input('Enter interest rate between 0 and 1: '))
  years = int(input('Enter term of the loan in years: '))
  amt = float(input('Enter amount borrowed under 1 million: '))
  l_type = input('Enter loan type (Mortg, Car, Other): ')
  
  # Create an object from the Loan class
  my_loan = loan2.Loan(rate, years, amt, l_type)

  # Get the current period from the user (assume correct input)
  cur_per = int(input('Input current period between 1 and tot_per: '))

  # Set the period data attribute to current period
  my_loan.set_period(cur_per)

  # Calculate the remaining balance and display it
  remain_balance = my_loan.calc_remain_balance(cur_per)
  print(f'Balance after {cur_per} periods is ${remain_balance:,.2f}')

  # Calculate the interest savings and display it
  interest_savings = my_loan.calc_interest_savings(cur_per)
  print(f'Interest saved after {cur_per} periods is ${interest_savings:,.2f}')
