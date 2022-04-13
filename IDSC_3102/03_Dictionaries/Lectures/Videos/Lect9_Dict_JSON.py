# **********************************************************************
# Slide #9: Dictionaries and JSON Files
# **********************************************************************
# JSON File is a dict with a single key-value pair
# {customers:[cust1, cust2, ... ]}
# Each list element like cust1 is a more complex dictionary 
# cust1 = {attr1: value1, attrib2: value2, ... }
# There are nine (9) top-level key-value pairs from user_id ... loans
# Four (4) of these top-level key-value pairs are themselves
# either a) lists or b) dicts or c) lists of dicts:
# * children is a variable length list depending on the
#   number of kids customer has.
# * address is a dict with 4 key-value pairs defining a
#   typical US address.
# * phone_numbers is a 2-element list, one for a cell phone and
#   another for a work phone. Each element is a dict with 2 key-value
#   pairs specifying the type (cell, work) and the number itself.
# * loans is a variable length list depending on the number of
#   different loans a particular customer has. Each loan is a dict
#   with 6 key-value pairs describing the basic elements of a loan.
# The objective is to extract selected information on customers and
# their loans and write it to a CSV file for further analysis.
# **********************************************************************
import json
import csv

def main():
  # Open JSON file for reading
  in_json_file = open('Loans.json', 'r')

  # Load the data from JSON file into dictionary
  loans_data = json.load(in_json_file)

  # Close the file
  in_json_file.close()

  # Use the 'customers' key to reference the value, which is
  # a list of 6 elements, each of which is a sub-dictionary
  # representing a single customer
  num_custs = len(loans_data['customers'])

  # Examine the structure first
  # check_struct(loans_data, num_custs)

  # Open Loans6.csv for writing and create csv.writer() object
  loans6_csv_file = open('Loans6.csv', 'w', newline='')
  loans6_writer = csv.writer(loans6_csv_file)

  # Create and write headers to the file
  col_headers = ['UserID', 'Customer Name', 'City', 'Phone',
                 'LoanID', 'Loan Type', 'Loan Amount', 'Monthly Payment']
  loans6_writer.writerow(col_headers)

  for i in range(num_custs):
    # Understand the reference the current customer
    cur_cust = loans_data['customers'][i]

    # Extract some data from the top-level
    usr_id = cur_cust['user_id']
    cust_name = cur_cust['first_name'] + ' ' + cur_cust['last_name']

    # Get the city by going a level further down
    cust_city = cur_cust['address']['city']

    # Get the cell phone number with correct referencing
    cust_phone = cur_cust['phone_numbers'][0]['number']

    # Let's print what we have so far
    # print(usr_id, cust_name, cust_city, cust_phone, sep=',')

    # The trickiest part is to get the loan info
    num_loans = len(cur_cust['loans'])
    for j in range(num_loans):
      loan_id = cur_cust['loans'][j]['loan_id']
      loan_type = cur_cust['loans'][j]['type']
      amount = cur_cust['loans'][j]['amount']
      mth_pmt = cur_cust['loans'][j]['mth_pmt']
      # Printing all the information for the the resulting CSV file
      print(usr_id, cust_name, cust_city, cust_phone,
            loan_id, loan_type, amount, mth_pmt, sep=',')
      # Create a resulting row list
      result_row = [usr_id, cust_name, cust_city, cust_phone,
                    loan_id, loan_type, amount, mth_pmt]
      # Write to CSV file
      loans6_writer.writerow(result_row)

  # Close the CSV file
  loans6_csv_file.close()

# *** end main()

def check_struct(loans_data, num_custs):
  # loans_data is dict of size 1, the entire file
  print(len(loans_data))

  # Print number of customers
  print(num_custs)
  print()

  # Examine the structure of the JSON file
  for i in range(num_custs):
    # Understand the reference the current customer
    cur_cust = loans_data['customers'][i]

    print('Printing keys and value types for customer', i)
    # Print the keys and values for the customers to confirm
    # the structure of the (9) top-level key-value pairs
    for key, val in cur_cust.items():
      if type(val) is int or type(val) is str:
        print(key, type(val))
      else:
        print(key, type(val), len(val))
    print()

# Call main()
main()
