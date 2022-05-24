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
df5 = home_sales_df[(home_sales_df['NESector'] == 'Yes') & (home_sales_df['CornerLot'] == 'Yes')]
df5 = df5.drop(['Age', 'NESector', 'CornerLot'], axis=1).sort_values('Features', axis=0, ascending=False)
df5.head(20)

# **********************************************************************
# Problem 6 (1 point). Find the average price, average size and average
# age of homes by Northeast sector. 
df6 = home_sales_df.drop(['Features','CornerLot','OfferPending','AnnualTax'], axis=1).groupby('NESector').mean()
df6.head()

# **********************************************************************
# Problem 7 (1 point). Create a new column called PPSQF defined as
# Price / SquareFeet. Find the average price, average size and average
# PPSQF by Northeast sector and corner lot. Sort the resulting data frame
# by average PPSQF descending.
# Hint: Remember to reset the index of the resulting data frame before
# sorting on average PPSQF.
home_sales_df['PPSQF'] = home_sales_df['Price'] / home_sales_df['SquareFeet']
home_sales_df.info()

df7 = home_sales_df.drop(['Features','Age','OfferPending','AnnualTax'], axis=1).groupby(['NESector','CornerLot']).mean().reset_index(drop=False, inplace=False).sort_values('PPSQF', axis=0, ascending=False)
df7.head()