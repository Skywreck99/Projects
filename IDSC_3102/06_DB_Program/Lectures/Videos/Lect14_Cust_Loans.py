# **********************************************************************
# DB Programming: Customer Loans Application
# **********************************************************************

import tkinter
import tkinter.messagebox
import sqlite3
from tkinter import ttk

class CustLoans:
  # ********************************************************************
  # Slide #10: Designing Loans DB Application
  # ********************************************************************
  def __init__(self):
    # Create the main window widget
    self.main_window = tkinter.Tk()
    # Display a title
    self.main_window.title('Customer Loans')
    # Adjust size and prevent resizing
    self.main_window.geometry('550x250')
    self.main_window.resizable(False, False)

    # Design Listbox of customer names and return list of customer IDs
    cust_ids = self.list_box()
    # for idx in range(len(cust_ids)):
    #   print(idx, cust_ids[idx])
    
    # Setup tkinter Treeview table widget for displaying customer loans
    self.table()

    # Get the list index 4 of the 5-th default customer
    cust_idx = self.listbox_customers.curselection()
    # Get the custID of the default customer
    cust_id = cust_ids[cust_idx[0]]
    #[0] needed because curselection() returns a tuple (to accomodate
    # multiple item selection - not used in this example

    # Initial call to get_cust_loans function to retrieve the loans
    # of the 5-th default customer
    self.get_cust_loans(cust_id)
    
    # Bind <<ListboxSelect>> event to get_cust_id callback function
    self.listbox_customers.bind('<<ListboxSelect>>', lambda e:
                                self.get_cust_id(e, cust_ids))
    
    # Enter the tkinter main loop
    tkinter.mainloop()

  # ******************************************************************
  # Slide #11: Listbox of Customer Names
  # ******************************************************************   
  def list_box(self):
    # Display a label for customer selection
    self.label_customers = tkinter.Label(self.main_window,
                                    text='Select customer')
    self.label_customers.place(x=30, y=20)

    # Create a Listbox of customer names
    self.listbox_customers = tkinter.Listbox(self.main_window,
                                         selectmode=tkinter.SINGLE,
                                         height=10, width=20)
    self.listbox_customers.place(x=30, y=40)

    # Connect to Loans.db and retrieve customer first and last names
    db_conn = sqlite3.connect('Loans.db')
    db_cursor = db_conn.cursor()
    db_cursor.execute('SELECT custID, firstName, \
                              lastName FROM Customer')
    cust_recs = db_cursor.fetchall()

    # Close DB connection
    db_conn.close()

    # Set the list of customer IDs to blank
    cust_ids = []

    # Populate the Listbox with customer full names
    for idx in range(len(cust_recs)):
      cust_ids.append(cust_recs[idx][0])
      cust_full_name = cust_recs[idx][1] + ' ' + \
                       cust_recs[idx][2] 
      self.listbox_customers.insert(idx, cust_full_name)
      
    # Select 5-th customer by default
    self.listbox_customers.select_set(4)

    # Return the list of customer IDs
    return cust_ids

  # ******************************************************************
  # Slide #12: Treeview Table of Customer Loans
  # ******************************************************************  
  def table(self):
    # Display a label for result dispaly
    self.label_cust_loans = tkinter.Label(self.main_window,
                                    text='Customer loans')
    self.label_cust_loans.place(x=200, y=20)
    
    # Setup tkinter Treeview table
    column_ids = ('l_id','amt','l_type','pmt')
    self.table_loans = ttk.Treeview(self.main_window,
                                    column=column_ids, show='headings',
                                    height=5)
    # Define headings
    self.table_loans.heading('l_id', text='Loan ID')
    self.table_loans.heading('amt', text='Amount')
    self.table_loans.heading('l_type', text='Loan Type')
    self.table_loans.heading('pmt', text='Payment')

    # Configure column widths
    self.table_loans.column('l_id', anchor='e', width=50)
    self.table_loans.column('amt', anchor='e', width=100)
    self.table_loans.column('l_type', width=75)
    self.table_loans.column('pmt', anchor='e', width=75)

    # Place the table to the right of the list box
    self.table_loans.place(x=200, y=40)

  # ******************************************************************
  # Slide #13: <<LisboxSelect>> Callback Function
  # ******************************************************************  
  def get_cust_id(self, e, cust_ids):
    cust_idx = self.listbox_customers.curselection()
    cust_id = cust_ids[cust_idx[0]]

    # Subsequent calls to get_cust_loans function
    self.get_cust_loans(cust_id)

  # ******************************************************************
  # Slide #14: Retrieving Customer Loans
  # ****************************************************************** 
  def get_cust_loans(self, cust_id):
    # Connect to Loans.db and retrieve customer loan info based on ID
    db_conn = sqlite3.connect('Loans.db')
    db_cursor = db_conn.cursor()
    sql_string = 'SELECT loanID, amount, loanType, mthPmt \
                 FROM Loan WHERE custID=' + str(cust_id)
    db_cursor.execute(sql_string)
    loan_recs = db_cursor.fetchall()

    # Clear the table before inserting
    for item in self.table_loans.get_children():
      self.table_loans.delete(item)

    # Insert records for the new customer
    for loan_rec in loan_recs:
      # Insead of printing we insert into tkinter table !!!
      # print(loan_rec)
      # Format the amount and monthly payment as currency
      amt = f'${loan_rec[1]:,.0f}'
      pmt = f'${loan_rec[3]:,.2f}'
      # Create a formatted tuple for the current record
      loan_rec_fmt = (loan_rec[0], amt, loan_rec[2], pmt)
      self.table_loans.insert('', tkinter.END, values=loan_rec_fmt)

    # Close DB connection
    db_conn.close()

# Create an instance of the CustLoans class.
if __name__ == '__main__':
  cust_loans = CustLoans()
