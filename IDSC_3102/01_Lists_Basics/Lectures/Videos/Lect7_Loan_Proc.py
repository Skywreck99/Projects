# **********************************************************************
# Slide #3: Processing Lists
# **********************************************************************
# Processing numerical list
def main():
  # List of mortgage payments
  payments = [661.44, 1705.96, 1239.68, 3925.64]

  # Get number of list elements and set accumulator
  num_pmts = len(payments)
  tot_pmts = 0.0

  # Loop through the list accumulating payments
  for pmt in payments:
    tot_pmts += pmt

  # Calculate and display the average payment of $1,883.18
  avg_pmt = tot_pmts / num_pmts
  print(f'Average mortgage payment is ${avg_pmt:,.2f}')

# Processing list of strings
def main():
  # List of customer cities
  cust_cities = ['Santa Fe', 'Santa Fe', 'Santa Fe', 'Taos', 'Albuquerque',
               'Albuquerque', 'Santa Fe', 'Santa Fe', 'Albuquerque',
               'Santa Fe', 'Albuquerque', 'Taos', 'Taos', 'Albuquerque',
               'Taos', 'Taos']

  # Set list of city counters, 0=Santa Fe, 1=Taos, 2=Albuquerque
  city_count = [0] * 3

  # Loop through the list appropriately incrementing city counters
  for city in cust_cities:
    if city == 'Santa Fe':
      city_count[0] += 1
    elif city == 'Taos':
      city_count[1] += 1
    else:
      city_count[2] += 1

  # Display the customer city counts
  print('Number of Santa Fe customers is', city_count[0])
  print('Number of Taos customers is', city_count[1])
  print('Number of Albuquerque customers is', city_count[2])

# **********************************************************************
# Slide #4: Lists and Functions
# **********************************************************************
# Passing list to a function
def main():
  # List of mortgage payments
  payments = [661.44, 1705.96, 1239.68, 3925.64]

  # Display the average payment of $1,883.18
  print(f'The average monthly payment is ${calc_avg(payments):,.2f}')
  
def calc_avg(num_list):
  # Calculate list size and set accumulator
  size = len(num_list)
  total = 0.0
  
  # Loop through the list accumulating values
  for num in num_list:
    total += num

  # Check if the size is not zero
  if size != 0:
    average = total / size
  else:
    average = 0.0

  # Return the average
  return average

# Returning list from a function
# Nothing goes in -> list comes out
def main():
  # Get the list of payments from a function
  payments = get_nums()

  # Display the payments
  print('The mortgage payment list')
  print(payments)

def get_nums():
  # Pretend the user entered these values
  nums = [661.44, 1705.96, 1239.68, 3925.64]

  # Return the list
  return nums

# Returning list from a function
# List goes in -> list comes out
def main():
  # List of customer cities
  cust_cities = ['Santa Fe', 'Santa Fe', 'Santa Fe', 'Taos', 'Albuquerque',
               'Albuquerque', 'Santa Fe', 'Santa Fe', 'Albuquerque',
               'Santa Fe', 'Albuquerque', 'Taos', 'Taos', 'Albuquerque',
               'Taos', 'Taos']

  # The function relies on sorted list
  cust_cities.sort()

  # Print the city frequency counts
  print('City frequency counts')
  print(freq_counts(cust_cities))

def freq_counts(str_list):
  # Set item counter
  item = 0
  freqs = [1]

  # Loop through the sorted list using index
  for indx in range(1, len(str_list)):
    if str_list[indx] == str_list[indx - 1]:
      freqs[item] += 1
    else:
      item += 1
      freqs.append(1)

  return freqs

# **********************************************************************
# Slide #5: Lists and Files
# **********************************************************************
# Writing lists to files
def main():
  # List of mortgage payments
  payments = [661.44, 1705.96, 1239.68, 3925.64]
  # List of customer cities
  cust_cities = ['Santa Fe', 'Santa Fe', 'Santa Fe', 'Taos', 'Albuquerque',
               'Albuquerque', 'Santa Fe', 'Santa Fe', 'Albuquerque',
               'Santa Fe', 'Albuquerque', 'Taos', 'Taos', 'Albuquerque',
               'Taos', 'Taos']

  # Open files for writing
  pmts_file = open('Payments.txt', 'w')
  cities_file = open('Cities.txt', 'w')

  # Write payments to the Payments.txt file
  for pmt in payments:
    pmts_file.write(str(pmt) + '\n')

  # Write cities to the Cities.txt file
  for city in cust_cities:
    cities_file.write(city + '\n')

  # Close the files
  pmts_file.close()
  cities_file.close()

# Reading lists from files
def main():
  # Open files for reading
  pmts_file = open('Payments.txt', 'r')
  cities_file = open('Cities.txt', 'r')

  # Read file contents into lists
  payments = pmts_file.readlines()
  cust_cities = cities_file.readlines()

  # Close both files
  pmts_file.close()
  cities_file.close()

  # Payments must be converted to float one by one (float strips \n)
  for indx in range(len(payments)):
    payments[indx] = float(payments[indx])

  # Customer cities must be stripped of newline character \n
  for indx in range(len(cust_cities)):
    cust_cities[indx] = cust_cities[indx].rstrip('\n')

  # This will allow us to print clean lists
  print('List of payments as floats')
  print(payments)
  print('List of cities without blank lines')
  print(cust_cities)

# **********************************************************************
# Slide #6: List Comprehension and Tuples
# **********************************************************************
# List of customer cities
cust_cities = ['Santa Fe', 'Santa Fe', 'Santa Fe', 'Taos', 'Albuquerque',
             'Albuquerque', 'Santa Fe', 'Santa Fe', 'Albuquerque',
             'Santa Fe', 'Albuquerque', 'Taos', 'Taos', 'Albuquerque',
             'Taos', 'Taos']

# Use list comprehension to find city lengths
city_lengths = [len(c) for c in cust_cities]
city_lengths

# List of mortgage payments
payments = [661.44, 1705.96, 1239.68, 3925.64]

# Use list comprehension to filter the payments under $1,500
low_pmts = [p for p in payments if p < 1500]
low_pmts

# Convert payments list into a tuple
pmts_tuple = tuple(payments)
pmts_tuple
# Display the first element and try modifying it
pmts_tuple[0]
pmts_tuple[0] = 999.99

# **********************************************************************
# Slide #7: Two-Dimensional Lists
# **********************************************************************
# *** Listing customer cities and counts of customers in those cities
def main():
  # List of customer cities
  cust_cities = ['Santa Fe', 'Santa Fe', 'Santa Fe', 'Taos', 'Albuquerque',
               'Albuquerque', 'Santa Fe', 'Santa Fe', 'Albuquerque',
               'Santa Fe', 'Albuquerque', 'Taos', 'Taos', 'Albuquerque',
               'Taos', 'Taos']

  # The function relies on sorted list
  cust_cities.sort()

  # Print the cities and customer counts
  print('Cities and their frequency counts')
  print(item_freq_counts(cust_cities))
  
# Function receives a list and returns a
# 2-dim list of items and frequencies
def item_freq_counts(str_list):
  # Initialize item counter
  item = 0
  # Initialize a 2-dimensional list
  items_freqs = []
  # Set the first list element ['Albuquerque', 1]
  item_freq = [str_list[0], 1]
  # Add it to the currently blank 2D list
  items_freqs.append(item_freq)

  # Loop through the sorted list of customer cities using index
  for indx in range(1, len(str_list)):
    # If the element is the same as the previous one,
    # increment the (same) city count by 1
    if str_list[indx] == str_list[indx - 1]:
      items_freqs[item][1] += 1   # References 2nd column in the table
    # Otherwise, increment the (overall) count of cities
    # Set the (same) city count to 1, e.g. ['Taos', 1] and
    # add it to the 2D list
    else:
      item += 1
      item_freq = [str_list[indx], 1]
      items_freqs.append(item_freq)

  return items_freqs
