# ********************************************************************
# Slides #7-9: Database Programming
# ********************************************************************
def main():
  # Intro DB programming
  print('********************************')
  print('********** Slides 7-9 **********')
  print('********************************')
  db_prog()

  # Querying multiple tables
  print('******************************')
  print('********** Slide 15 **********')
  print('******************************')
  qry_mult_tbls()

  # Basic summary queries
  print('******************************')
  print('********** Slide 17 **********')
  print('******************************')
  summary_queries()
  print('******************************')

def db_prog():
  import sqlite3

  # Connect to the database
  db_conn = sqlite3.connect('Loans.db')

  # Get a cursor for the database
  db_cursor = db_conn.cursor()

  # Run the query against the database
  db_cursor.execute('SELECT * FROM Customer')

  # Return a list of tuples representing the resulting records
  cust_loans = db_cursor.fetchall()

  # Loop through the resulting list of tuples
  for loan in cust_loans:
    print(loan)

  # Close the connection to the DB
  db_conn.close()

  print()

# ********************************************************************
# Slide 15: Querying Multiple Tables
# ********************************************************************
def qry_mult_tbls():
  # Setup connection and cursor
  import sqlite3
  db_conn = sqlite3.connect('Loans.db')
  db_cursor = db_conn.cursor()

  # Build a more complex query string
  sql_string = 'SELECT firstName, lastName, amount, mthPmt '
  sql_string += 'FROM Customer INNER JOIN Loan '
  sql_string += 'ON Customer.custID = Loan.custID '
  sql_string += 'WHERE city = "Santa Fe" AND loanType = "Mortg"'

  # Execute query and return result in a list of tuples
  db_cursor.execute(sql_string)
  loans_mortg_sf = db_cursor.fetchall()

  # Find the number of mortgage loans in Santa Fe
  num_loans = len(loans_mortg_sf)

  # Set total amount and payment
  tot_amt = 0
  tot_pmt = 0
  
  # Loop through the resulting list of tuples
  for loan_rec in loans_mortg_sf:
    # Print the records
    print(loan_rec)
    # Update the accumulators
    tot_amt += loan_rec[2]
    tot_pmt += loan_rec[3]

  print()
  # Display total amount of mortgage loans in Santa Fe
  print(f'Total mortgage loans in Santa Fe is ${tot_amt:,.0f}')

  # Display the average mortgage monthly payment in Santa Fe
  avg_pmt = tot_pmt / num_loans
  print(f'Average mortgage monthly payment in Santa Fe is ${avg_pmt:,.2f}')

  # Close database connection
  db_conn.close()

  print()

# ********************************************************************
# Slide 17: Basic Summary Queries
# ********************************************************************
def summary_queries():
  # Setup connection and cursor
  import sqlite3
  db_conn = sqlite3.connect('Loans.db')
  db_cursor = db_conn.cursor()  

  # Find the number of loans by loan type
  sql_string = 'SELECT loanType, COUNT(*) AS NumLoans '
  sql_string += 'FROM Loan GROUP BY loanType'

  # Execute query and return result in a list of tuples
  db_cursor.execute(sql_string)
  loans_count_by_type = db_cursor.fetchall()

  # Loop through the resulting list of tuples
  for rec in loans_count_by_type:
    print(rec)

  print()

  # Calculate the average monthly payment by city
  db_sql = 'SELECT city, ROUND(AVG(mthPmt),2) AS avgMthPmt '
  db_sql += 'FROM Customer INNER JOIN Loan '
  db_sql += 'ON Customer.custID = Loan.custID '
  db_sql += 'WHERE loanType = "Mortg" GROUP BY city'

  # Execute query and return result in a list of tuples
  db_cursor.execute(db_sql)
  avg_mortg_pmt_by_city = db_cursor.fetchall()

  # Loop through the resulting list of tuples
  for rec in avg_mortg_pmt_by_city:
    print(rec)

  # Close database connection
  db_conn.close()

if __name__ == '__main__':
  main()
