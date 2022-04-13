# **********************************************************************
# DB Programming: Loans by Type Summary
# **********************************************************************

import tkinter
import tkinter.messagebox
import sqlite3
from tkinter import ttk

class LoansTypeSum:
  # ********************************************************************
  # Slide #18: Summarizing Loans by Type Grouped by City
  # ********************************************************************
  def __init__(self):
    # Create the main window widget
    self.main_window = tkinter.Tk()
    # Display a title
    self.main_window.title('Loans by Type Summary')
    # Adjust size and prevent resizing
    self.main_window.geometry('575x150')
    self.main_window.resizable(False, False)

    # Design Radiobuttons for loan types
    self.radio_buttons()
    
    # Setup tkinter Treeview table widget for displaying loan summary
    self.table()

    # Make the initial call to Radiobuttons callback function
    self.get_loans_type_sum()
    
    # Enter the tkinter main loop
    tkinter.mainloop()

  # ******************************************************************
  # Define Radiobutton Widgets for Loan Type
  # ******************************************************************   
  def radio_buttons(self):
      # *******************************************************************
      # Create Radiobuttons for loan types
      # *******************************************************************
      # Display a label for loan types
      self.label_loan_type = tkinter.Label(self.main_window,
                                      text='Choose loan type')
      self.label_loan_type.place(x=30, y=10)

      # Build a frame that will contain loan types
      self.frame_loan_type = tkinter.Frame(self.main_window)
      self.frame_loan_type.config(bd=1, relief=tkinter.SOLID)
      self.frame_loan_type.place(x=40, y=30)

      # Create the StringVar object to use with the radio buttons
      self.loan_type = tkinter.StringVar()

      # Set the StringVar object to Mortgage loan type
      self.loan_type.set('Mortg')

      # Design 3 Radiobutton widgets for Mortgage, Car and Other loan types
      self.rb_mortg = tkinter.Radiobutton(self.frame_loan_type,
                                         text='Mortgage',
                                         variable=self.loan_type,
                                         value='Mortg',
                                         command=self.get_loans_type_sum)
      self.rb_mortg.pack(anchor='w')

      self.rb_car = tkinter.Radiobutton(self.frame_loan_type,
                                         text='Car',
                                         variable=self.loan_type,
                                         value='Car',
                                         command=self.get_loans_type_sum)
      self.rb_car.pack(anchor='w')

      self.rb_other = tkinter.Radiobutton(self.frame_loan_type,
                                         text='Other',
                                         variable=self.loan_type,
                                         value='Other',
                                         command=self.get_loans_type_sum)
      self.rb_other.pack(anchor='w')

  # ******************************************************************
  # Treeview Table of Customer Loans for Selected Loan Type
  # ******************************************************************  
  def table(self):
    # Display a label for result dispaly
    self.label_cust_loans = tkinter.Label(self.main_window,
                                    text='Loans Summary')
    self.label_cust_loans.place(x=150, y=10)
    
    # Setup tkinter Treeview table
    column_ids = ('cty','l_num','tot_amt','avg_pmt')
    self.table_loans = ttk.Treeview(self.main_window,
                                    column=column_ids, show='headings',
                                    height=3)
    # Define headings
    self.table_loans.heading('cty', anchor='w', text='City')
    self.table_loans.heading('l_num', text='Num Loans')
    self.table_loans.heading('tot_amt', text='Total Amount')
    self.table_loans.heading('avg_pmt', text='Average Payment')

    # Configure column widths
    self.table_loans.column('cty', width=100)
    self.table_loans.column('l_num',anchor='e', width=75)
    self.table_loans.column('tot_amt', anchor='e', width=100)
    self.table_loans.column('avg_pmt', anchor='e', width=100)

    # Place the table to the right of the list box
    self.table_loans.place(x=150, y=30)

  # ******************************************************************
  # Summarizing Customer Loans by Loan Type Grouped by City
  # ****************************************************************** 
  # Radiobutton's callback function
  def get_loans_type_sum(self):
    # Get the values of loan type radio buttons
    ltp = self.loan_type.get()

    # Connect to Loan.db and summarize loans by type grouped by city
    db_conn = sqlite3.connect('Loans.db')
    db_cursor = db_conn.cursor()
    sql_string = 'SELECT city, COUNT(*) AS numLoans, '
    sql_string += 'SUM(amount) AS totAmount, '
    sql_string += 'ROUND(AVG(mthPmt), 2) AS avgMthPmt '
    sql_string += 'FROM Customer INNER JOIN Loan '
    sql_string += 'ON Customer.custID = Loan.custID '
    sql_string += 'WHERE loanType="' + ltp + '" '
    sql_string += 'GROUP BY city'
    db_cursor.execute(sql_string)
    loan_recs = db_cursor.fetchall()

    # Clear the Treeview table before inserting
    for item in self.table_loans.get_children():
      self.table_loans.delete(item)

    # Insert records into Treeview table
    for loan_rec in loan_recs:
      # Insead of printing we insert into tkinter table !!!
      # print(loan_rec)
      # Format the total amount and average monthly payment as currency
      tot_amt = f'${loan_rec[2]:,.0f}'
      avg_pmt = f'${loan_rec[3]:,.2f}'
      # Create a formatted tuple for the current record
      loan_rec_fmt = (loan_rec[0],  loan_rec[1], tot_amt, avg_pmt)
      self.table_loans.insert('', tkinter.END, values=loan_rec_fmt)

    # Close DB connection
    db_conn.close()

# Create an instance of the LoansTypeSum class.
if __name__ == '__main__':
  loans_type_sum = LoansTypeSum()
