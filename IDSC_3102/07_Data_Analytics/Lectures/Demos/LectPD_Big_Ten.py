# ********************************************************************
# Reading Data from CSV Files
# ********************************************************************
import pandas as pd

# Read from CSV file 
big_ten_df = ???

# Examine data frame contents
big_ten_df.info()

# Examine the header and tail
big_ten_df.head()
big_ten_df.tail()

# ********************************************************************
# Practicing Subsetting with BigTen Examples
# ********************************************************************
big_ten_column_list = big_ten_df.columns.tolist()
# Use the list as much as possible to copy/paste column selections
big_ten_column_list

# ********************************************************************
# 1. List moderately ranked schools showing school name, graduation rate,
# ACT scores and acceptance rates. Save the result in mod_df data
# frame and manually copy/paste from the console into LectPD_Big_Ten.xlsx
# Excel file, sheet 1. Must get skilled with Data -> Text to Columns!
mod_df = big_ten_df.loc[???]
mod_df

# ********************************************************************
# 2. List Midwest schools excluding abbreviation, region and enrollment
# using the exclusion ~ (tilda) operator and isin() function.
# Save the result in midwest_df data frame and write it into temp.csv
# file. Then copy/paste from temp.csv into LectPD_Big_Ten.xlsx Excel
# file, sheet 2.
midwest_df = big_ten_df.loc[???]
midwest_df

# Easy writing of a data frame to a CSV file (must be closed!)
midwest_df.???

# ********************************************************************
# 3. Show all the schools that are neither Low nor in Top10. Keep the
# school, WN_Rank, graduation and acceptance rates. Save the result
# in middle_df data frame and write it into temp.csv which must be
# closed from the previous question. Then copy/paste from temp.csv file
# into LectPD_Big_Ten.xlsx Excel file, sheet 3.
middle_df = big_ten_df.loc[???,
                           ['School', 'WN_Rank','Grad_Rate', 'Accept']]
middle_df

# Make sure temp.csv is closed from previous question!
middle_df.to_csv('temp.csv')

# ********************************************************************
# 4. Show the moderately ranked schools in Midwest with ACT over 27. 
# Keep the school name, ACT score, acceptance rate, and high school
# GPA. Save the result in mod_mdw_act_df data frame, and copy/paste 
# into sheet 4 of the LectPD_Big_Ten.xlsx Excel file.
mod_mdw_act_df = big_ten_df.loc[???,
  ['School','ACT', 'Accept', 'HS_GPA']]
mod_mdw_act_df

# ********************************************************************
# 5. Show Midwest schools with enrollment either over 40000 or under 30000.
# Keep the school name, World News rank, graduation rate, and enrollment.
# Save the result in mdw_enroll_high_low_df and copy/paste into sheet 5 of
# the Excel file.
mdw_enroll_high_low_df = big_ten_df.loc[???,
  ['School', 'WN_Rank', 'Grad_Rate', 'Enroll']]
mdw_enroll_high_low_df

# ********************************************************************
# 6. Select the school name, region, World News rank, graduation rate
# and enrollment into big_ten_sub_df. Then sort the new data frame on
# enrollment descending into big_ten_sort1_df. Manually copy/paste
# into sheet 6 of the Excel file.
big_ten_sub_df = big_ten_df[['School', 'Region', 'WN_Rank',
                             'Grad_Rate', 'Enroll']]

big_ten_sort1_df = big_ten_sub_df.???
big_ten_sort1_df

# Sort the big_ten_sub_df by region and within each region by graduation
# rate descending into big_ten_sort2_df. Manually copy/paste into
# sheet 6 of the Excel file.
big_ten_sort2_df = big_ten_sub_df.???

big_ten_sort2_df

# ********************************************************************
# 7. Create a new column with average composite ACT and SAT score defined
# as: Score = (ACT/36 + SAT/1600)/2 and rounded to 2 decimals
big_ten_df[???] = round((big_ten_df['ACT']/36 + big_ten_df['SAT']/1600)/2, 2)
big_ten_df

# Find the average of the composite score
avg_score = ???
avg_score

# Use it to subset the schools with total composite score > average. Keep
# the school name, World News rank, SAT, ACT and composite score. Save the 
# result in above_avg_score_df, copy/paste into sheet 7 of the Excel file. 
above_avg_score_df = big_ten_df.loc[???,
    ['School', 'WN_Rank', 'SAT', 'ACT', 'Score']]
above_avg_score_df

# ********************************************************************
# 8. Find the average acceptance rate, total enrollment and number
# of schools by World News ranking. Create appropriate data frames,
# extract the columns needed, sort as appropriate, and manually
# copy/paste the results into sheet 8 of the Excel file.

# Group by WN_Rank and calculating the average of all numerical columns.
WN_rank_mean_df = ???
WN_rank_mean_df

# Note that the result is a new data frame with WN_Rank as row indexes and
# names of numerical columns as column indexes.
type(WN_rank_mean_df)
WN_rank_mean_df.index
WN_rank_mean_df.columns

# Sort the data frame ascending on Accept and then select the column.
WN_rank_mean_df.???
WN_rank_mean_df.???

# Find the total enrollment by World News ranking and sort descending
# on total enrollment. Adding up any column other than Enroll does not
# make logical sense. This shows it can be done as a single long expression,
# which is prone to errors and should be typically broken into multiple steps.
big_ten_df.???

# Find the number of schools by World News ranking. The column can be 
# any one from the data frame, except WN_Rank. All the counts will
# produce the exact same result.
WN_rank_count_df = ???
WN_rank_count_df

# Sort descending
WN_rank_count_df.???

# ********************************************************************
# 9. Find the average graduation rate, ACT and SAT scores, acceptance rate
# and high school GPA by Region and World News ranking. Create the appropriate
# data frame, learn about multi-level indexes, re-index the data frame,
# and manually copy/paste the result into sheet 9 of the Excel file.
region_wn_rank_mean_df = ???
region_wn_rank_mean_df

# Note that the result is a new data frame with multi-level Region-WN_Rank
# as row indexes (tuples) and names of numerical columns as column indexes. 
type(region_wn_rank_mean_df)
region_wn_rank_mean_df.index
region_wn_rank_mean_df.columns

# Googling the issue results in application of reset_index() to create
# two columns Region and WN_Rank out of the indexes
region_wn_rank_mean_df = ???
region_wn_rank_mean_df

# Then all we have to do is remove the Enrollment column to get our result.
# Googling how to use slicing with Boolean array
region_wn_rank_mean_df.loc[:, region_wn_rank_mean_df.columns != 'Enroll']

# We could just use the inclusion of all the other columns.
region_wn_rank_mean_df[['Region','WN_Rank','Grad_Rate','SAT','ACT','Accept','HS_GPA']]

# ********************************************************************
# 10. Find the min, max and average high school GPA by World News ranking.
# Use groupby on WN_Rank together with the agg function, which needs a
# single-element dictionary, where the key is HS_GPA and the value is a
# list of aggregate functions we need. This will create a data frame, call
# it wn_rank_hs_gpa_stats_df, that needs to be manually copy/pasted into
# sheet 10 of the Excel file.

# Single grouping, single column, and multiple aggregates
wn_rank_hs_gpa_stats_df = big_ten_df.???
type(wn_rank_hs_gpa_stats_df)
wn_rank_hs_gpa_stats_df

# Find the number of schools, total and average enrollment, as well
# as min, max and average graduation rate by region and World News rank.
# Save it into region_wn_rank_summ_df. Create a dictionary with all 
# columns (keys) and aggregates (values) in agg_dict first. Manually
# copy/paste the result into sheet 10 of the Excel file.
agg_dict = {'School': ['count'], 'Enroll': ['sum', 'mean'],
            'Grad_Rate': ['min', 'max', 'mean']}

# Multi-level groupings, multiple columns, and multiple aggregates
region_wn_rank_summ_df = ???
region_wn_rank_summ_df

# Reset the index for potential further use
region_wn_rank_summ_df = region_wn_rank_summ_df.reset_index()
region_wn_rank_summ_df
