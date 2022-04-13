# **********************************************************************
# Data Analysis with pandas
# **********************************************************************

# OS command prompt> pip install pandas

import pandas as pd

# ********************************************************************
# Slide #4: Series Object
# ********************************************************************
rates_list = [0.07, 0.075, 0.07, 0.065, 0.077]
rates = pd.Series(rates_list)
rates
rates.values  # NumPy array
rates.values.tolist() # Original list
rates.index   # RangeIndex object
rates.index.tolist()

# ********************************************************************
# Slide #5: Index Object
# ********************************************************************
loan_type_list = ['Mortg', 'Mortg', 'Mortg', 'Car', 'Car']
loan_ids = list(range(1022, 1027))
loan_types = pd.Series(loan_type_list, index=loan_ids)
loan_types

amt_dict = {1022: 200000, 1023: 150000,
            1024: 100000, 1025: 25000, 1026: 10000}
amounts = pd.Series(amt_dict)

# ********************************************************************
# Slide #6: Vectorized Operations
# ********************************************************************
rates * amounts   # Indices not aligned
# Redefine rates with loan IDs as indices
rates = pd.Series(rates_list, index=loan_ids)
rates * amounts

# ********************************************************************
# Slide #7: DataFrame Object
# ********************************************************************
# Call the function to assemble individual series in a list
import loans
loan_series = loans.loan_series()
  
# Create data frame from the list of individual series with concat
import pandas as pd
loans_df = pd.concat(loan_series, axis=1)
loans_df

# Examine the default 0, 1, 2, 3, 4 row and column indices
loans_df.index
loans_df.index.tolist()
loans_df.columns
loans_df.columns.tolist()

# ********************************************************************
# Slide #8: DataFrame Function
# ********************************************************************
# Call the function to assemble individual series in a list
import loansdata
loan_series = loans.loan_series()

# Creating data frame from dict of individual series using DataFrame
import pandas as pd
loan_cols = ['loanID', 'intRate', 'loanType', 'amount', 'loanTerm']
loan_series_dict = dict(zip(loan_cols, loan_series))
loans_df = pd.DataFrame(loan_series_dict)

# Examine the column indices
loans_df.columns
loans_df.columns.tolist()

# Examine data frame contents
loans_df.info()

# Basic column summary stats
loans_df.describe()

# ********************************************************************
# Slide #9: Working with DataFrame Columns
# ********************************************************************
# Selecting a single column by name
loans_df['intRate']

# Selecting multiple columns using names
loans_df[['loanType', 'amount']]

# Selecting a column by number - loanTerm is the 5th column at index 4
loans_df[loans_df.columns[4]]

# Selecting multiple columns by slicing - first 3 columns at
# indices 0 (loanID), 1 (intRate), and 2 (loanType)
loans_df[loans_df.columns[:3]]

# Selecting non-adjacent columns - rate is the second (index 1), loan
# type the third (index 2) and loan term the fifth (index 4)
loans_df[loans_df.columns[[1,2,4]]]

# Finding the sum, count, mean, min and max of a column
loans_df['amount'].sum()
loans_df['loanType'].count()
loans_df['intRate'].mean()
loans_df['intRate'].max()
loans_df['loanTerm'].min()

# ********************************************************************
# Slide #10: Working with DataFrame Rows
# ********************************************************************
# Select the second row (index 1)
loans_df[1:2]

# Select the first three rows
loans_df[:3]

# Select the last two rows
loans_df[-2:]

# Select non-consecutive rows
loans_df.loc[[1,3,4]]

# Select rows based on logical (Boolean) column expressions
# Select all mortgage loans
loans_df[loans_df['loanType']=='Mortg']

# ********************************************************************
# Slide #11: Subsetting with Logical Expressions
# ********************************************************************
# Select all loans with interest rates of 7% or higher with the
# amount over 100000 - must have () around relational comparisons
loans_df[(loans_df['intRate']>=0.07) &
         (loans_df['amount']>100000)]

# Select all loans with interest rates of 7% or over who's term
# is either less than 10 or more than 20 years
loans_df[(loans_df['intRate']>=0.07) &
         ((loans_df['loanTerm']<10) |
          (loans_df['loanTerm']>20))]

# Select all mortage loans and omitting loanType column
loans_df.loc[loans_df['loanType']=='Mortg',
             loans_df.columns != 'loanType']

# ********************************************************************
# Slide #12: Reading Data from CSV and Excel Files
# ********************************************************************
import pandas as pd

# Read from CSV file 
loans_df = pd.read_csv('Loans.csv')

# Examine data frame contents - did not recognize datetime data type
loans_df.info()

# Read from Excel file -- must install xlrd library first
# OS command prompt> pip install xlrd
loans_df = pd.read_excel('Loans.xls')

# Examine data frame contents - recognized datetime data type
loans_df.info()

# Examine the header and tail
loans_df.head()
loans_df.tail()

# ********************************************************************
# Slide #13: More Subsetting Examples
# ********************************************************************
# Mortgage loans showing loanID, amount, rate, term and payment
loans_df.loc[loans_df['loanType']=='Mortg',
             ['loanID', 'amount', 'intRate', 'loanTerm', 'mthPmt']]

# Exclusion ~ operator and isin() function
# Mortgage loans excluding first and last name and loan type
loans_df.loc[loans_df['loanType']=='Mortg',
      ~loans_df.columns.isin(['firstName', 'lastName','loanType'])]

# Show all the loans for customers that are not from Taos. Keep the
# loanID, city, and amount through monthly payment. Save the result
# in loans_no_Taos_df data frame.
loans_no_Taos_df = loans_df.loc[loans_df['city']!='Taos',
  ['loanID', 'city',  'amount', 'intRate', 'loanTerm',
   'loanType','mthPmt']]

# ********************************************************************
# Slide #14: More Subsetting Examples (cont.)
# ********************************************************************
# Show all Taos mortgage loans. Keep the loanID, amount, interest rate,
# loan term and monthly payment. Save the result in loans_Taos_Mortg_df
loans_Taos_Mortg_df = loans_df.loc[(loans_df['city']=='Taos') &
  (loans_df['loanType']=='Mortg'), ['loanID','amount', 'intRate',
  'loanTerm', 'mthPmt']]

# Show mortgage loans that are either over half a million or under
# 200K. Keep the loanID, amount, interest rate, loan term, and
# monthly payment. Save the result in loans_mortg_high_low_df.
loans_mortg_high_low_df = loans_df.loc[(loans_df['loanType']=='Mortg') &
  ((loans_df['amount']>500000) | (loans_df['amount']<200000)), ['loanID',
  'amount', 'intRate', 'loanTerm', 'mthPmt']]

# Show all January 2030 loans. Keep the loanID, loan date, as well as
# amount through monthly payment. Save the result in loans_jan_df.
import datetime
beg_jan = datetime.date(2030, 1, 1)
end_jan = datetime.date(2030, 1, 31)
loans_jan_df = loans_df.loc[(loans_df['loanDate']>=beg_jan) &
  (loans_df['loanDate']<=end_jan), ['loanID', 'loanDate',
  'amount', 'intRate', 'loanTerm', 'loanType','mthPmt']]

# ********************************************************************
# Slide #15: Sorting and Adding Columns
# ********************************************************************
# Select the loanID, loan type, city, amount, interest rate and
# monthly payment into loans_sub_df, and then sort the resulting
# data frame descending on monthly payment into a new data frame
# named loans_sort1_df.
loans_sub_df = loans_df[['loanID', 'loanType', 'city', 'amount',
                        'intRate','mthPmt']]

loans_sort1_df = loans_sub_df.sort_values('mthPmt', ascending=False)

# Sort the selected columns (loans_sub_df) by loan type and within
# each type by amount descending. Save the result into loans_sort2_df.
loans_sort2_df = loans_sub_df.sort_values(['loanType', 'amount'],
                                          ascending=(True, False))

# Sort the selected columns (loans_sub_df) by loan type and city and
# then within each type-city combination by amount descending. Save
# the result into loans_sort3_df.
loans_sort3_df = loans_sub_df.sort_values(['loanType', 'city', 'amount'],
                                          ascending=(True, True, False))

# Create a new column totPmt = mthPmt * loanTerm * 12
loans_df['totPmt'] = loans_df['mthPmt'] * loans_df['loanTerm'] * 12

# Find the average of total payments
avg_tot_pmt = loans_df['totPmt'].mean()

# Use it to subset the loans with total payment > average. Keep the
# loanID, amount, interest rate, loan term, monthly payment and total
# payment. Save the result in loans_above_avg_tot_pmt_df.
loans_above_avg_tot_pmt_df = loans_df.loc[loans_df['totPmt']>avg_tot_pmt,
    ['loanID', 'amount', 'intRate', 'loanTerm', 'mthPmt', 'totPmt']]

# ********************************************************************
# Slide #16: Group By (Splitting) and Aggregating
# ********************************************************************
# Find average monthly payment by the type of loan. Save the groups
# into loan_type_grp, the means of all columns into loan_type_avg_df,
# and just the means of monthly payments into loan_type_avg_pmt_df.

# Split the data frame into 3 groups using loanType - Mortg, Car, Other
loan_type_grp = loans_df.groupby('loanType')

# Calculate means of all numerical columns (returns a data frame)
# Apply (aggregate) step of the split-apply-combine process
# Combine the averages over three groups into a resulting data frame
loan_type_avg_df = loan_type_grp.mean()
type(loan_type_avg_df)
loan_type_avg_df.info()

# Subset just the mthPmt column as the final result
loan_type_avg_pmt = loan_type_avg_df['mthPmt']

# Direct way of finding the average monthly payment by loan type.
loan_type_avg_pmt = loans_df.groupby('loanType').mean()['mthPmt']

# Find the total of all amounts borrowed by loan type.
loan_type_tot_amt = loans_df.groupby('loanType').sum()['amount']

# Find the number of loans by loan type. You can use any column
# instead of loanID except the loanType.
loan_type_count = loans_df.groupby('loanType').count()['loanID']

# ********************************************************************
# Slide #17: Grouping By Multiple Columns
# ********************************************************************
# Find the average monthly payment by loan type and city.
loan_type_city_avg_pmt = \
  loans_df.groupby(['loanType','city']).mean()['mthPmt']

# Find the minimum, maximum and average monthly payment by loan type.
loan_type_pmt_stats = \
  loans_df.groupby('loanType').agg({'mthPmt': ['min', 'max', 'mean']})

# Find the number of loans, total and average amount borrowed, as well
# as the minimum, maximum and average monthly payment by loan type and
# city. Create a dictionary with all the columns (keys) and aggregations
# (values) in agg_dict first. 
agg_dict = {'loanID': ['count'],'amount': ['sum', 'mean'],
            'mthPmt': ['min', 'max', 'mean']}

loan_type_city_summ = \
  loans_df.groupby(['loanType','city']).agg(agg_dict)



