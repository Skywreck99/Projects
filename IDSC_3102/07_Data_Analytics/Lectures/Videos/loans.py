# *** loans.py
def loan_series():
  import pandas as pd
  
  # Redefine all the Series with default indices
  # Loan ID's will become the first column in a data frame
  loan_ids = pd.Series(range(1022, 1027))

  # Rates series is defined from a list
  rates_list = [0.07, 0.075, 0.07, 0.065, 0.077]
  rates = pd.Series(rates_list)

  # Loan Types series is defined from a list
  loan_type_list = ['Mortg', 'Mortg', 'Mortg', 'Car', 'Car']
  loan_types = pd.Series(loan_type_list)

  # Amount series is defined from a dictionary
  amt_dict = {1022: 200000, 1023: 150000,
            1024: 100000, 1025: 25000, 1026: 10000}
  amounts = pd.Series(amt_dict)
  amounts = pd.Series(amounts.values)

  # New Loan Terms series is defined from a list
  term_list = [15, 15, 30, 3, 5]
  loan_terms = pd.Series(term_list)

  # Creating a list of individual series
  series_list = [loan_ids, rates, loan_types, amounts, loan_terms]

  # Return the list of individual series
  return series_list
