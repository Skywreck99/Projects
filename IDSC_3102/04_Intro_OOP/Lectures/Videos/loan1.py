# **********************************************************************
# Slide #11: Enhancing Loan Class
# **********************************************************************
class Loan:

  # The __init__ method accepts arguments defining the loan
  def __init__(self, rate, years, amt, l_type):
    # Assigns the values of parameters to appropriate attributes
    self.__int_rate = rate
    self.__term = years
    self.__amount = amt
    self.__loan_type = l_type
    # The current period at the beginning is the 1st month
    self.__period = 1

  # The get methods read the data from object attributes
  def get_int_rate(self):
    return self.__int_rate

  def get_term(self):
    return self.__term

  def get_amount(self):
    return self.__amount

  def get_loan_type(self):
    return self.__loan_type

  def get_period(self):
    return self.__period

  # The set methods write the data to object attributes
  def set_int_rate(self, rate):
    if rate > 0 and rate <= 0.3:
      self.__int_rate = rate
    else:
      self.__int_rate = 0

  def set_term(self, years):
    if years > 0 and years <= 30:
      self.__term = years
    else:
      self.__term = 0

  def set_amount(self, amt):
    if amt > 0 and amt <= 1000000:
      self.__amount = amt
    else:
      self.__amount = 0

  def set_loan_type(self, l_type):
    self.__loan_type = l_type

  def set_period(self, per):
    tot_per = 12 * self.__term
    if per >= 1 and per <= tot_per:
      self.__period = per
    else:
      self.__period = 0

  # The calc_mth_pmt function returns the monthly payment
  def calc_mth_pmt(self):
    mth_rate = self.__int_rate / 12
    mth_term = 12 * self.__term
    mth_pmt = (mth_rate)/(1-(1+mth_rate)**(-mth_term)) * self.__amount
    return mth_pmt

  # The calc_remain_balance returns the remaining balance
  # as of the current period
  def calc_remain_balance(self, per):
    # Get the initial loan amount as the remaining balance
    rem_bal = self.__amount

    # Calculate the monthly payment
    mth_pmt = self.calc_mth_pmt()
    
    # Loop through all the periods up to the current one
    for p in range(1, per + 1):
      # Calculate the interest part of the payment
      ip = rem_bal * self.__int_rate / 12
      # Calculate the principal part of the payment
      pp = mth_pmt - ip
      # Reduce the overall balance by the principal portion
      rem_bal -= pp

    # Return the remaining balance
    return rem_bal
      
  # The calc_interest_savings returns the total interest savings
  # if the loan was to be paid off as of the current period
  def calc_interest_savings(self, per):
    # Find the remaining balance as of the current period
    rem_bal = self.calc_remain_balance(per)

    # Calculate the monthly payment
    mth_pmt = self.calc_mth_pmt()
    
    # Loop from the period after current to the end and
    # accumulate the interest that will not be paid
    intr_save = 0
    for p in range(per + 1, 12 * self.__term + 1):
      # Calculate the interest part of the payment
      ip = rem_bal * self.__int_rate / 12
      # Calculate the principal part of the payment
      pp = mth_pmt - ip
      # Reduce the overall balance by the principal portion
      rem_bal -= pp
      # Accumulate the interest savings
      intr_save += ip

    # Return the accumulated interest savings
    return intr_save
  
