# *****************************************************************************
# Assign1b_14_Gas_Prices.py
# *****************************************************************************
# The gas_prices.txt file contains the weekly average prices for a gallon of
# gas in the United States, beginning on April 5th, 1993, and ending on
# August 26th, 2013. Each line in the file contains the average price for a
# gallon of gas on a specific date. Each line is formatted in the following
# way:
#      MM-DD-YYYY:Price
# MM is the two-digit month, DD is the two-digit day, and YYYY is the
# four-digit year. Price is the average price per gallon of gas on the specific
# date.
# For this assignment, you are to write a program that reads the contents of
# the file and calculate the average price of gas per year for each year in
# the file, including the incomplete years 1993 and 2013, so the result will
# have 21 data points.
# *****************************************************************************
# Note: The tasks are significantly modified from the original textbook problem.
# After reading the file into a list named gas_prices in main(), the program
# must be modularized as follows:
# parse_data:         Takes gas_prices, returns years and prices lists
# avg_price_per_yr:   Takes years and prices, displays years and average
#                     prices for those years
# You must use the dictionary approach described as follows. Start with two
# blank dictionaries named total_prices and count_weeks. The total_prices
# dictionary is the accumulator for all the gas prices in a given year, where
# each key-value pair represents a year (key) and the sum (value) of all the
# weekly prices for that year. Similarly, the count_weeks dictionary is a counter
# of weeks in a given year, where each key-value pair represents a year (key) and
# the count (value) of the weeks for that year. You can't assume each year has 52
# weeks, both the first (1993) and the last (2013) years are incomplete, but even
# for the complete years, the count can be 53 instead of 52 weeks, or some weeks
# could be missing (although that is not the case with this data set), etc..
# *****************************************************************************
# Test: Your output should look like this (only the first few and the last year
# are displayed below to save space, the code must display all years):
# 1993 1.071
# 1994 1.078
# ...
# 2013 3.651
# *****************************************************************************
import re
# Main function
def main():
  # Open the file for reading
  price_file = open('gas_prices.txt', 'r')

  # Read the contents of the file into gas_prices list
  gas_prices = price_file.readlines()

  # Close the file
  price_file.close()

  # Parse the data into components and get years and prices
  years, prices = parse_data(gas_prices)

  # Calculate the average prices per year
  avg_price_per_yr(years, prices)
  
# *** end main()

def parse_data(gas_prices):
  # Initialize years and prices to blank lists
  years = list()
  prices = list()
  
  # Loop through the list splitting on hyphen into 3 pieces and
  # then splitting the last piece on the colon. There are other
  # of performing the split, you are encouraged to experiment, but
  # make sure you get the correct years and prices.
  for line in gas_prices:
    gas_split = re.split('[:-]', line)
    # Append appropriate values to years and prices lists. Remember
    # the prices must be added as floats, rather than strings.
    years.append(int(gas_split[2]))
    prices.append(float(gas_split[3]))

  # Return the years and prices lists
  return years, prices

def avg_price_per_yr(years, prices):
  # You can assume the years and prices lists are of the same length
  # representing the total number of weeks in the dataset
  num_weeks = len(years)

  # Initialize total_prices and count_weeks to blank dictionaries
  total_prices = dict()
  count_weeks = dict()

  # Loop through both years and prices lists accumulating the prices into
  # the total_prices dictionary, and counting the weeks for a given year in
  # the count_weeks dictionary. The year acts a key for both dictionaries.
  for idx in range(num_weeks):
    # Get the current year as the key
    key = years[idx]

    # Check if the year (key) is NOT in the total_prices dictionary
    if key not in total_prices.keys():
      # Add the year (key) with the corresponding price as the initial value
      total_prices[key] = prices[idx]
    # Otherwise the year (key) is already in dictionary
    else:
      # Increment/accumulate the value for the existing key (year)
      # by adding the corresponding price
      total_prices[key] += prices[idx]

    # Similar logic applies for the week counts, but we want to reverse
    # the if-else for practice (i.e., just to do it differently).
    # Check if the year (key) IS in the count_weeks dictionary.
    if key in count_weeks.keys():
      # Increment the value representing the week count by 1
      count_weeks[key] += 1
    # Otherwise the year (key) is not in the count_weeks dictionary
    else:
      # Add the year (key) with the value of 1, the first week of the year
      count_weeks[key] = 1

  # Print the result by looping through one of the two dictionaries,
  # and calculating the avg_price using values from both dictionaries
  #print(count_weeks.items())
  for key in total_prices.keys():
    avg_price = total_prices[key] / count_weeks[key]
    print(key, f'{avg_price:.3f}')

# Call the main
if __name__ == '__main__':
  main()
