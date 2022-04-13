# **********************************************************************
# Slides #10-11: Redefining Loan Class
# **********************************************************************
class Loan:

  # The __init__ method accepts arguments defining the loan
  def __init__(self, rate, years, amt, l_type):
    # Assigns the values of parameters to appropriate attributes
    self.__int_rate = rate
    self.__term = years
    self.__amount = amt
    self.__loan_type = l_type

  # The get methods read the data from object attributes
  def get_int_rate(self):
    return self.__int_rate

  def get_term(self):
    return self.__term

  def get_amount(self):
    return self.__amount

  def get_loan_type(self):
    return self.__loan_type

  # The set methods write the data to object attributes
  def set_int_rate(self, rate):
    if rate > 0 and rate <= 0.3:
      self.__int_rate = rate
    else:
      self.__int_rate = 0

  def set_term(self, tot_per):
    if tot_per > 0 and tot_per <= 30:
      self.__term = tot_per
    else:
      self.__term = 0

  def set_amount(self, amt):
    if amt > 0 and amt <= 1000000:
      self.__amount = amt
    else:
      self.__amount = 0

  def set_loan_type(self, l_type):
    self.__loan_type = l_type

  # The calc_mth_pmt function returns the monthly payment
  def calc_mth_pmt(self):
    mth_rate = self.__int_rate / 12
    mth_term = 12 * self.__term
    mth_pmt = (mth_rate)/(1-(1+mth_rate)**(-mth_term)) * self.__amount
    return mth_pmt
  
