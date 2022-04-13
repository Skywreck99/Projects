# **********************************************************************
# DB Programming: Loans by Type and City
# **********************************************************************

import tkinter
import tkinter.messagebox
import sqlite3
from tkinter import ttk

class LoansTypeCity:
  # ********************************************************************
  # Slide #16: Loans by Type and City
  # ********************************************************************
  def __init__(self):
    # Create the main window widget
    self.main_window = tkinter.Tk()
    # Display a title
    self.main_window.title('Loans by Type and City')
    # Adjust size and prevent resizing
    self.main_window.geometry('400x300')
    self.main_window.resizable(False, False)

    # Design Radiobuttons for loan types and cities
    self.radio_buttons()
    
    # Setup tkinter Treeview table widget for displaying customer loans
    self.table()

    # Make the initial call to Radiobuttons callback function
    self.get_loans_type_city()
    
    # Enter the tkinter main loop
    tkinter.mainloop()

  # ******************************************************************
  # Define Radiobutton Widgets for Loan Type and City
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
                                         command=self.get_loans_type_city)
      self.rb_mortg.pack(anchor='w')

      self.rb_car = tkinter.Radiobutton(self.frame_loan_type,
                                         text='Car',
                                         variable=self.loan_type,
                                         value='Car',
                                         command=self.get_loans_type_city)
      self.rb_car.pack(anchor='w')

      self.rb_other = tkinter.Radiobutton(self.frame_loan_type,
                                         text='Other',
                                         variable=self.loan_type,
                                         value='Other',
                                         command=self.get_loans_type_city)
      self.rb_other.pack(anchor='w')

      # *******************************************************************
      # Create Radiobuttons for cities
      # *******************************************************************
      # Display a label for cities
      self.label_city = tkinter.Label(self.main_window,
                                      text='Choose city')
      self.label_city.place(x=200, y=10)

      # Build a frame that will contain cities
      self.frame_city = tkinter.Frame(self.main_window)
      self.frame_city.config(bd=1, relief=tkinter.SOLID)
      self.frame_city.place(x=200, y=30)

      # Create the StringVar object to use with the radio buttons
      self.city = tkinter.StringVar()

      # Set the StringVar object to the city of Albuquerque
      self.city.set('Albuquerque')

      # Design 3 Radiobutton widgets for Albuquerque, Santa Fe and Taos
      self.rb_albq = tkinter.Radiobutton(self.frame_city,
                                         text='Albuquerque',
                                         variable=self.city,
                                         value='Albuquerque',
                                         command=self.get_loans_type_city)
      self.rb_albq.pack(anchor='w')

      self.rb_stfe = tkinter.Radiobutton(self.frame_city,
                                         text='Santa Fe',
                                         variable=self.city,
                                         value='Santa Fe',
                                         command=self.get_loans_type_city)
      self.rb_stfe.pack(anchor='w')

      self.rb_taos = tkinter.Radiobutton(self.frame_city,
                                         text='Taos',
                                         variable=self.city,
                                         value='Taos',
                                         command=self.get_loans_type_city)
      self.rb_taos.pack(anchor='w')

  # ******************************************************************
  # Treeview Table of Customer Loans for Selected Loan Type and City
  # ******************************************************************  
  def table(self):
    # Display a label for result dispaly
    self.label_cust_loans = tkinter.Label(self.main_window,
                                    text='Customer loans')
    self.label_cust_loans.place(x=30, y=130)
    
    # Setup tkinter Treeview table
    column_ids = ('f_name','l_name','amt','pmt')
    self.table_loans = ttk.Treeview(self.main_window,
                                    column=column_ids, show='headings',
                                    height=5)
    # Define headings
    self.table_loans.heading('f_name', anchor='w', text='First Name')
    self.table_loans.heading('l_name', anchor='w', text='Last Name')
    self.table_loans.heading('amt', text='Amount')
    self.table_loans.heading('pmt', text='Payment')

    # Configure column widths
    self.table_loans.column('f_name', width=80)
    self.table_loans.column('l_name', width=100)
    self.table_loans.column('amt', anchor='e', width=75)
    self.table_loans.column('pmt', anchor='e', width=75)

    # Place the table to the right of the list box
    self.table_loans.place(x=30, y=150)

  # ******************************************************************
  # Retrieving Customer Loans by Loan Type and City
  # ****************************************************************** 
  # Radiobutton's callback function
  def get_loans_type_city(self):
    # Get the values of loan type and city radio buttons
    ltp = self.loan_type.get()
    cty = self.city.get()

    # Connect to Loans.db and retrieve loans by type and city
    db_conn = sqlite3.connect('Loans.db')
    db_cursor = db_conn.cursor()
    sql_string = 'SELECT firstName, lastName, amount, mthPmt '
    sql_string += 'FROM Customer INNER JOIN Loan '
    sql_string += 'ON Customer.custID = Loan.custID '
    sql_string += 'WHERE city="' + cty + '" AND loanType="' + ltp + '"'
    db_cursor.execute(sql_string)
    loan_recs = db_cursor.fetchall()

    # Clear the table before inserting
    for item in self.table_loans.get_children():
      self.table_loans.delete(item)

    # Insert records into Treeview table
    for loan_rec in loan_recs:
      # Insead of printing we insert into tkinter table !!!
      # print(loan_rec)
      # Format the amount and monthly payment as currency
      amt = f'${loan_rec[2]:,.0f}'
      pmt = f'${loan_rec[3]:,.2f}'
      # Create a formatted tuple for the current record
      loan_rec_fmt = (loan_rec[0],  loan_rec[1], amt, pmt)
      self.table_loans.insert('', tkinter.END, values=loan_rec_fmt)

    # Close DB connection
    db_conn.close()

# Create an instance of the LoansTypeCity class.
if __name__ == '__main__':
  loans_type_city = LoansTypeCity()
