# **********************************************************************
# Exam3_Final.py
# **********************************************************************
# You must run the import statement and successfully read the CSV file
# to proceed. Examine the structure, as well as the header and tail of
# the data frame before you start with the problems. Some of the
# problems can be completed with a single statement, most will need a
# couple, with the last one needing several lines of code. While there is
# more than one way to get to an answer, and the format of the result
# may vary slightly, to get the full credit for a question, the final
# result must be correct both in terms of being reproducible by running
# the code, as well as the correct results being copy/pasted into the
# appropriate Excel answer sheet. When copy/pasting you will need to
# fiddle with the column parsing a bit to get it to split correctly.
# Pasting the result into Excel without splitting the columns will result
# in point deduction, but no additional formatting is required. Partial
# credit will be awarded based on the degree of problem completion.
# **********************************************************************
import pandas as pd

# Read from CSV file 
cars_df = pd.read_csv('Cars.csv')

# Examine data frame structure
cars_df.info()

# Examine the header and tail
cars_df.head()
cars_df.tail()

# Column list for copy/pasting: ['Model', 'Origin', 'Price', 'HP', 'MPG']
cars_df.columns.to_list()

# **********************************************************************
# 1. (3 points) Find the "cheap" cars, priced under $15,000 from US and
# South Korea. Save the result showing the Model, Origin and Price into
# df1 data frame, sorted descending on Price. You should get 7 rows as
# the result.
df1 = cars_df.loc[(cars_df['Price']<15000) & ((cars_df['Origin'] == 'South Korea') | (cars_df['Origin'] == 'United States'))]


df1.to_csv('temp.csv')
len(df1)

# ********************************************************************
# 2. (3 points) Find the US cars with HP of 500 or over, as well as
# European cars with MPG under 15. Save the result showing the Model,
# Origin, HP and MPG into df2 data frame. You should get 3 rows as
# the result.
df2 = cars_df.loc[((cars_df['Origin'] == 'United States') & (cars_df['HP']>=500)) | ((cars_df['Origin'] == 'Europe') & (cars_df['MPG'] < 15)), ['Model', 'Origin', 'HP', 'MPG']]


df2.to_csv('temp.csv')
len(df2)

# ********************************************************************
# 3. (3 points) Find all European sedans, in a sense that the Model
# contains the word 'sedan'. You must use the Series.str.contains(pat)
# function, where Series is the Model column and pat is the pattern you
# are looking for ('sedan'). The result is a boolean Series of True/False
# values, True if a Model has the word 'sedan' in it, False otherwise.
# Save the result showing the Model, MPG, HP and Price into df3 data
# frame, sorted descending on Price. You should get 7 rows in the result.
df3 = cars_df.loc[(cars_df['Model'].str.contains('sedan')) & (cars_df['Origin'] == 'Europe')].sort_values('Price', ascending=False)


df3.to_csv('temp.csv')
len(df3)

# ********************************************************************
# 4. (1 point) Find the number of models, as well as the min, max and
# average price by origin. You must use agg_dict to setup a dictionary
# with columns and aggregates, followed by the use of the agg function
# to perform the aggregations. Save the result into df4 data frame.
agg_dict = {'Model': ['count'], 'Price': ['min', 'max', 'mean']}

df4 = cars_df.groupby('Origin').agg(agg_dict)

df4.to_csv('temp.csv')

# ********************************************************************
# 5. (2 points) Add MPG_HP column to the cars_df data frame defined
# as 100*MPG/HP and rounded to 2 decimals. High MPG_HP represents
# highly efficient cars in a sense that they get higher MPG per each
# HP. Next, calculate the average MPG_HP in avg_mpg_hp variable and
# use the variable to show all the cars with MPG_HP over 3 times the
# average. Save the result showing the Model, Origin and MPG_HP into
# df5 data frame, sorted descending on MPG_HP. You should get 5 rows
# as the result.
cars_df['MPG_HP'] = round((100 * cars_df['MPG'])/cars_df['HP'], 2)
cars_df.info()
cars_df.head()

avg_mpg_hp = cars_df['MPG_HP'].mean()
avg_mpg_hp

df5 = cars_df.loc[cars_df['MPG_HP'] > 3*avg_mpg_hp]



df5.to_csv('temp.csv')
len(df5)

# ********************************************************************
# 6. (3 points) Find the number of models by Origin and Make, but only
# show the makes with more than 10 models, sorted descending on the
# number of models. You should get 8 rows in the result.
# ********************************************************************
# You must use use the following approach to this problem:
# Start by adding the two new columns to the data frame: Spc and Make.
# To create the Spc column, you must use the Series.str.find(pat)
# function, where Series is the Model column and pat is the first
# occurrence of space (' '). Then just run the provided apply function
# that will use the Spc series to extract the make out of each model,
# which will allow you to then work on the original question. The only
# reason for getting the incorrect Make column is if the Spc column was
# not setup correctly.
# ********************************************************************
cars_df['Spc'] = cars_df['Model'].str.find(' ')
cars_df['Make'] = cars_df.apply(lambda f: f.Model[:f.Spc], axis=1)
cars_df.info()
cars_df.head()

df6 = cars_df.groupby(['Origin', 'Make']).agg({'Model': ['count']}).reset_index()
df6 = df6.loc[df6['Model']['count']>10].sort_values(('Model', 'count'), ascending=False)

df6.to_csv('temp.csv')
len(df6)