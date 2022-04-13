# **********************************************************************
# United States Energy Data Analysis with pandas
# **********************************************************************
# You must follow the instructions provided both below and in the PDF
# associated with this assignment. The result of each problem must be
# documented in the appropriate sheet of the Assign3_pandas.xlsx Excel
# file using any method that works best for you. Providing the code for
# writing to CSV or Excel files is NOT required. See PDF for details.
# **********************************************************************
import pandas as pd

# Read from CSV file 
us_energy_df = pd.read_csv('US_Energy.csv')

# Examine data frame contents - see PDF for details on each variable.
us_energy_df.info()

# Examine the header and tail
us_energy_df.head()
us_energy_df.tail()

# **********************************************************************
# Problem 1 (1 point). List states from West North Central division
# (Midwest region) showing the state name and all the numerical columns.
# You should get 7 rows in the result.
df1 = 

# **********************************************************************
# Problem 2 (1 point). List Midwest states with population over 5 million
# showing the state name, population, GDP, total consumption, total
# production and total expenditures. You should get 7 rows in the result. 
df2 =


# **********************************************************************
# Problem 3 (1 point). List the states with over 10 million people that
# either have their total consumption or total production over 4 quadrillion
# BTUs. Show the state name, region, population, total consumption and total
# production, sorted descending on population. You should get 5 rows in
# the result. Note: The consumption and production data is in billions of
# BTUs, and 1 quadrillion = 1,000 trillion = 1,000,000 billion
df3 = 

# **********************************************************************
# Problem 4 (1 point). Create a new column called NetExport defined as
# production minus consumption. The states with positive NetExport are
# "net producing", the ones with negative NetExport are "net consuming".
# List all the "net producing" states with the population over 5 million
# people. Show the state name, region, population, total production,
# total consumption, and net export, sorted descending on net export.
# You should get 4 rows in the result.  
us_energy_df['NetExport'] = 
us_energy_df.info()

df4 = 

