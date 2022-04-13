# **********************************************************************
# Slide #8: Processing, summarizing and plotting loans
# **********************************************************************
# The program processes loan data into 2D-list loans dataset with
# rows representing individual loans and columns different loan
# characteristics as follows (indices from 0 to 7):
# 1 - loan ID
# 2 - customer name
# 3 - customer city (Albuquerque, Santa Fe, Taos)
# 4 - loan amount
# 5 - interest rate
# 6 - term of loan
# 7 - loan type (Mortg, Car, Other)
# 8 - monthly payment
# Average mortgage payment by city and total amount borrowed by
# loan type are calculated, printed and plotted as a bar and
# pie charts, respectively.
# **********************************************************************
# Assumes matplotlib library package was successfully installed
import matplotlib.pyplot as plt

# Main switchboard
def main():
  # Process the loans from Loans.txt file into tab separated
  # loans dataset and print the dataset to check
  loans = process_loans()
  for idx in range(len(loans)):
    print(loans[idx])
  print()

  # Initialize city list
  cities = ['Albuquerque', 'Santa Fe', 'Taos']
  # Calculate and print the average mortgage payment by city
  avg_pmt = avg_mortg_city(cities, loans)
  for i in range(3):
    print('Average mortgage payment in ' + cities[i] + ' is $',
      format(avg_pmt[i],',.2f'), sep='')
  print()

  # Initialize loan types
  loan_types = ['Car', 'Mortg', 'Other']
  # Calculate and print the total amount by loan type  
  total_amount = tot_amt_loan_type(loan_types, loans)
  for i in range(3):
    print('Total value of ' + loan_types[i] + ' loans is $',
          format(total_amount[i], ',.2f'))

  # Create a bar chart of average mortgage payments by city
  bar_avg_mortg_city(cities, avg_pmt)

  # Create a pie chart of total amount of loans by loan type
  pie_tot_amt_loan_type(loan_types, total_amount)

# **********************************************************************
# Function processes the Loans.txt file data and splits the
# tab separate columns into loans list dataset
def process_loans():
  # Open Loans.txt file for reading
  loans_file = open('Loans.txt', 'r')

  # Read the file contents into a list
  loans_all = loans_file.readlines()

  # Close the file
  loans_file.close()

  # Initialize the master loans list
  loans = []
  
  # Process each file line by splitting columns using \t separator
  for idx in range(len(loans_all)):
    loans_all[idx] = loans_all[idx].rstrip('\n')
    loans.append(loans_all[idx].split('\t'))

  # Return the processed loans list
  return loans

# **********************************************************************
# Function accepts the loans dataset and returns average
# mortgage payment by city
def avg_mortg_city(cities, loans):
  # Initialize counter and accumulator lists
  count_city = [0] * 3
  total_pmts = [0] * 3 

  # Count and accumulate mortgage loans by city
  for idx in range(len(loans)):
    for i in range(3):
      if loans[idx][2] == cities[i] and loans[idx][6] == 'Mortg':
        count_city[i] += 1
        total_pmts[i] += float(loans[idx][7])

  # Calculate and display average mortgage by city
  avg_pmt = [0] * 3
  for i in range(3):
    avg_pmt[i] = total_pmts[i] / count_city[i]

  # Return average mortgage payment by city list (3 elements)
  return avg_pmt

# **********************************************************************      
# Function accepts the loans dataset and returns total amount
# of all loans by loan type
def tot_amt_loan_type(loan_types, loans):
  
  # Initialize counter and accumulator lists
  total_amount = [0] * 3

  # Accumulate total amount of the loans by type
  for idx in range(len(loans)):
    for i in range(3):
      if loans[idx][6] == loan_types[i]:
        total_amount[i] += float(loans[idx][3])

  # Return total amount by loan type list (3 elements)
  return total_amount

# **********************************************************************
def bar_avg_mortg_city(cities, avg_pmt):
  # Define left edges and set bar width
  pos = [0] * 3
  for i in range(3):
    pos[i] = i * 10
  bar_width = 10

  # Create the bar chart of average mortgage payment by city
  plt.bar(pos, avg_pmt, bar_width)

  # Add formatting to the chart
  plt.title('Average Mortgage Payment by City')
  plt.xlabel('City')
  plt.ylabel('Monthly Payment')
  plt.xticks(pos, cities)
  plt.ylim(ymin=1500, ymax=2300)

  # Display the chart
  plt.show()
  
# **********************************************************************
def pie_tot_amt_loan_type(loan_types, total_amount):
  # Create the pie chart of total amounts by loan type
  plt.pie(total_amount, labels=loan_types,
          colors=('b', 'g', 'k'))

  # Add formatting to the chart
  plt.title('Total Loan Amount by Loan Type')

  # Display the chart
  plt.show()
