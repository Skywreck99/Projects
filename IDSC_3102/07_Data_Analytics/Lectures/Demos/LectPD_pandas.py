# **********************************************************************
# Data Analysis with pandas
# **********************************************************************

# OS command prompt> pip install pandas
import pandas as pd

# ********************************************************************
# Series and Index Objects
# ********************************************************************
std_names_list =['John', 'Steve', 'Mary', 'Joe']

std_names = ???
std_names                     # Series object
std_names.values              # NumPy array
std_names.values.tolist()     # List object
std_names.index               # RangeIndex object
std_names.index.tolist()      # List object

# ********************************************************************
# DataFrame Object
# ********************************************************************
std_major_list = ['IS', 'FIN', 'ACCT', 'IS']
std_gpa_list = [3.6, 3.2, 3.8, 3.5]

std_data_dict = {'name': std_names_list, 'major': std_major_list,
  'gpa': std_gpa_list}

students_df = ???
students_df

# Examine the column names (indexes)
students_df.columns           # Index object
students_df.columns.tolist()  # List object

# Examine data frame structure (meta-data)
students_df.info()

# ********************************************************************
# Working with DataFrame Columns
# ********************************************************************
# Selecting a single column by name
students_df[???]

# Selecting multiple columns using names
students_df[???]

# Selecting a column by number - major is the second column at index 1
students_df[students_df.columns[1]]

# Selecting multiple columns by slicing - first 2 columns
students_df[students_df.columns[:2]]

# Selecting non-adjacent columns - name and gpa
students_df[students_df.columns[[0,2]]]

# Finding the basic stats of a column
students_df['name'].???
students_df['gpa'].???
students_df['gpa'].max()
students_df['major'].min()

# ********************************************************************
# Working with DataFrame Rows
# ********************************************************************
# Select the second row (index 1)
students_df[1:2]

# Select the first three rows
students_df[:3]

# Select the last two rows
students_df[-2:]

# Select non-consecutive rows using loc property
students_df.loc[[0,2,3]]

# Select rows based on logical (Boolean) column expressions. Select all
# IS students by creating a logical/Boolean (True, False) series.
bool_series = ???
type(bool_series)
students_df[bool_series]

# The most widely used way of subsetting data frame rows, typically
# with direct nesting of a Boolean series within the data frame.
students_df[???]

# ********************************************************************
# Subsetting with Logical Expressions
# ********************************************************************
# Select all non-IS students with GPA of 3.5 or higher
# Must have () around relational comparisons
students_df[???]

# Select all loans with gpa of 3.5 or lower who are either finance of
# information systems majors.
students_df[???]

# Select all IS majors omitting the major column
students_df.loc[students_df['major']=='IS', ???]

# Same as including name and gpa columns, which is what we will use the most
students_df.loc[students_df['major']=='IS', ???]
