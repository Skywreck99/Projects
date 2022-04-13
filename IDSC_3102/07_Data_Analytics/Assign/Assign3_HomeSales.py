# **********************************************************************
# Home Sales Data Analysis with pandas
# **********************************************************************
# You must follow the instructions provided both below and in the PDF
# associated with this assignment. The result of each problem must be
# documented in the appropriate sheet of the Assign3_pandas.xlsx Excel
# file using any method that works best for you. Providing the code for
# writing to CSV or Excel files is NOT required. See PDF for details.
# **********************************************************************
import pandas as pd

# Read from Excel file 
home_sales_df = pd.read_excel('HomeSales.xls')

# Examine data frame contents - see PDF for details on each variable.
home_sales_df.info()

# Examine the header and tail
home_sales_df.head()
home_sales_df.tail()

# **********************************************************************
# Problem 5 (1 point). List the houses that are both in the Northeast
# sector and on a corner lot. Show the selling price, size, number of
# features, offer pending and annual tax, sorted descending on the number
# of features. You should get 19 rows in the result.
df5 = 

# **********************************************************************
# Problem 6 (1 point). Find the average price, average size and average
# age of homes by Northeast sector. 
df6 = 

# **********************************************************************
# Problem 7 (1 point). Create a new column called PPSQF defined as
# Price / SquareFeet. Find the average price, average size and average
# PPSQF by Northeast sector and corner lot. Sort the resulting data frame
# by average PPSQF descending.
# Hint: Remember to reset the index of the resulting data frame before
# sorting on average PPSQF.
home_sales_df['PPSQF'] = 
home_sales_df.info()

df7 = 

# **********************************************************************
# Problem 10 (1 point). Find the number of homes, total and average size,
# as well as the min, max and average prices, and finally min, max and
# average PPSQF by Northeast sector and corner lot.
# Hint: Define the agg_dict with all the columns and aggregations and then
# use it with the agg function.
# Note: There is more than one way to get all the statistics, but in the
# end the Excel file must show the complete result.
agg_dict = 

df10 = 
