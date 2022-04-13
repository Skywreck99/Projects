# *****************************************************************************
# Lect8_Loan_CSV.py
# *****************************************************************************
# Concepts covered:
# Working with CSV files:
# 1) Reading from CSV file
# 2) Understanding rows and columns
# 3) Writing to CSV file
# *****************************************************************************
# The Loans.csv file contains the following information on 25 loans:
# 1) loan_id: ID of the loan
# 2) full_name: Full name of the customer
# 3) city: The name of the city customer resides in (Santa Fe, Taos, Albuquerque)
# 4) amount: The amount borrowed
# 5) loan_type: The type of the loan (Mortg, Car, Other)
# 6) mth_pmt: Monthly payment on the loan
# *****************************************************************************
# After importing the standard csv package, we want to open the file and read
# its contents using the reader() object from the csv package. The result
# of the reader function is a list, where each element is also a list
# representing the contents of a row that is already split into individual
# elements, indexed 0, 1, ..., to number of columns, assuming the CSV file is
# a legitimate rectangular structure with the same number of columns for each
# row, and each column having a consistent meaning from row to row.
# We want to process all the loans and calculate the average monthly payment
# per dollar borrowed. The result must be written in Summary.csv file using
# the writer() object's writerow() method from the standard csv package.
# *****************************************************************************
# Test: See Summary.csv file and also repeat the exercise in Excel with
# the PivotTable tool to confirm accuracy.
# *****************************************************************************
import csv

def main():
  # Open Loans.csv for reading - creates file object
  loans_csv_file = open('Loans.csv', 'r')

  # Pass file object to reader object to efficiently read CSV file
  loan_reader = csv.reader(loans_csv_file)

  # Initialize list of customer cities and loan types
  # Both arranged alphabetically for easier comparison with Excel's PivotTable
  cust_cities = ['Albuquerque', 'Santa Fe', 'Taos']
  loan_types = ['Car', 'Mortg', 'Other']

  # Initialize a two-dimensional list where first element represents
  # a list of loan counts for for a city of Santa Fe by mortgage, car
  # and other loan types. The second element is a similar list for
  # Taos and the third a list for Albuquerque
  loan_counts = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

  # Create similar two-dimensional list to hold payment to loan ratios
  # by city and loan type
  pmt_loan_ratios = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
  
  # Loop through each row and print the row contents
  for row in loan_reader:
    # row is a list of 6 elements, indexed 0 to 5
    cust_city = row[2]
    loan_type = row[4]

    # Calculate the current payment to loan ratio
    pmt_loan_ratio = float(row[5])/float(row[3])
    
    # Count the loans by city and type and accumulate
    # payment to loan ratios
    for i in range(3):
      for j in range(3):
        if cust_city == cust_cities[i] and loan_type == loan_types[j]:
          loan_counts[i][j] += 1
          pmt_loan_ratios[i][j] += pmt_loan_ratio

  # Close input file
  loans_csv_file.close()

  # Once all the data has been processed, calculate the average
  # payment to loan ratios by dividing the accumulated payment to
  # loan ratios by the number of loans by city and loan type
  for i in range(3):
    for j in range(3):
      if loan_counts[i][j] > 0:
        pmt_loan_ratios[i][j] = 1000 * pmt_loan_ratios[i][j] / loan_counts[i][j]
        pmt_loan_ratios[i][j] = f'${pmt_loan_ratios[i][j]:,.2f}'
      else:
        pmt_loan_ratios[i][j] = 'NA'

  # Open Loans.csv for writing - creates file object
  summary_csv_file = open('Summary.csv', 'w', newline='')

  # Pass file object to writer object to efficiently write CSV file
  summary_writer = csv.writer(summary_csv_file)

  # Create column headers list and write to file
  col_headers = ['Summary'] + loan_types
  summary_writer.writerow(col_headers)

  # Write each of the city rows, one by one
  for i in range(3):
    # Make one element lists out of cust_cities[i] strings by adding [] around
    # plus concatenating with single pmt_loan_ratios[i] element, which is a list
    # So, one element list + 3 element list = 4 element list
    result_row = [cust_cities[i]] + pmt_loan_ratios[i]
    summary_writer.writerow(result_row)

  # Close the output file
  summary_csv_file.close()
  
# Call the main
main()
