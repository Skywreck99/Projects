# *****************************************************************************
# Lect14_01b_Regions_Divisions.py
# *****************************************************************************
# This program is very loosely based on Problem 01, page 796 in Chapter 14 of
# the 5th edition of the textbook. I expanded the database by including state
# information and added all the cities in the US with population of more than
# 100,000 people as of last 2020 census, as well as 2010 census for comparison.
# *****************************************************************************
# Complete the GUI DB program that sets up radiobuttons for four (4) regions of
# the country: Northeast, Midwest (default), South and West. When a radiobutton
# for a particular region is selected (clicked), the list of divisions must be
# automatically populated with divisions for that specific region, and the first
# division must be automatically selected. At the same time, the information on
# all the states in the selected division from the currently selected region
# must be displayed in the table. This information must include the state name,
# state population from 2020 census, number of cities in that state, total urban
# population (of all those cities), and also finally calculate the percent urban
# population defined as total urban population divided by the state population.
# *****************************************************************************
# Note: You must use the GUI design shown in the PDF using the required widgets
# and variable names as much as possible. The design and functionality of such
# an event-driven program is not a straightforward linear process, but rather
# involves quite a bit of trial and error until the program looks and works the
# way it should. You should expect to spend some time figuring this out.
# *****************************************************************************
# Test: Run the program for multiple combinations of regions and divisions
# to verify it produces the desired results.
# *****************************************************************************

import tkinter
import tkinter.messagebox
import sqlite3
from tkinter import ttk

class RegionsDivisions:
  # ********************************************************************
  # Designing Regions-Divisions DB Application
  # ********************************************************************
  def __init__(self):
    # Create the main window widget
    self.main_window = tkinter.Tk()
    # Display a title
    self.main_window.title('Regions and Divisions')
    # Adjust size and prevent resizing
    self.main_window.geometry('850x250')
    self.main_window.resizable(False, False)

    # Design Radiobuttons for regions
    # self.radio_buttons()

    # Design Listbox of divisions
    # self.list_box()

    # Setup tkinter Treeview table widget for displaying state info
    # self.table()

    # Get the region of the currently selected radio button (Midwest)
    # ***
    
    # Bind <<ListboxSelect>> event to proc_sel_div callback function
    # self.listbox_divisions.bind('<<ListboxSelect>>', lambda e:
    #                               self.proc_sel_div(e))
    
    # Enter the tkinter main loop
    tkinter.mainloop()

  # ******************************************************************
  # Radiobutton for Regions
  # ******************************************************************   
  def radio_buttons(self):
    # Display a label for regions
    self.label_regions = tkinter.Label(self.main_window,
                                    text='Choose region')
    self.label_regions.place(x=30, y=10)

    # Build a frame that will contain regions
    self.frame_regions = tkinter.Frame(self.main_window)
    self.frame_regions.config(bd=1, relief=tkinter.SOLID)
    self.frame_regions.place(x=40, y=30)

    # Create the StringVar object to use with the radio buttons
    self.region = ???

    # Set the StringVar object to Midwest region
    # ***

    # Design 4 Radiobutton widgets for Northeast, Midwest,
    # South and West regions
    self.rb_northeast = tkinter.Radiobutton(self.frame_regions,
                                       text='Northeast',
                                       variable=self.region,
                                       value='Northeast',
                                       command=self.get_divisions)
    self.rb_northeast.pack(anchor='w')

    self.rb_midwest = tkinter.Radiobutton(self.frame_regions,
                                       text='Midwest',
                                       variable=self.region,
                                       value='Midwest',
                                       command=self.get_divisions)
    self.rb_midwest.pack(anchor='w')

    self.rb_south = tkinter.Radiobutton(self.frame_regions,
                                       text='South',
                                       variable=self.region,
                                       value='South',
                                       command=self.get_divisions)
    self.rb_south.pack(anchor='w')

    self.rb_west = tkinter.Radiobutton(self.frame_regions,
                                       text='West',
                                       variable=self.region,
                                       value='West',
                                       command=self.get_divisions)
    self.rb_west.pack(anchor='w')
    
  # ******************************************************************
  # Listbox of Divisions
  # ******************************************************************   
  def list_box(self):
    # Display a label for division selection
    self.label_divisions = tkinter.Label(self.main_window,
                                    text='Select division')
    self.label_divisions.place(x=150, y=10)

    # Create a Listbox of divisions and leave it empty
    self.listbox_divisions = tkinter.Listbox(self.main_window,
                                         selectmode=tkinter.SINGLE,
                                         height=5, width=20)
    self.listbox_divisions.place(x=150, y=30)

  # ******************************************************************
  # Treeview Table of State Information
  # ******************************************************************  
  def table(self):
    # Display a label for result display
    self.label_states = tkinter.Label(self.main_window,
                                    text='Display state and city info')
    self.label_states.place(x=300, y=10)
    
    # Setup tkinter Treeview table
    column_ids = ('state', 'pop_state','num_cities', 'pop_urban','pct_urban')
    self.table_states = ttk.Treeview(self.main_window,
                                    column=column_ids, show='headings',
                                    height=8)
    # Define headings
    self.table_states.heading('state', anchor='w', text='State Name')
    self.table_states.heading('pop_state', text='State Pop')
    self.table_states.heading('num_cities', text='Num Cities')
    self.table_states.heading('pop_urban', text='Urban Pop')
    self.table_states.heading('pct_urban', text='% Urban')

    # Configure column widths
    self.table_states.column('state', width=150)
    self.table_states.column('pop_state', anchor='e', width=100)
    self.table_states.column('num_cities', anchor='e', width=100)
    self.table_states.column('pop_urban', anchor='e', width=100)
    self.table_states.column('pct_urban', anchor='e', width=75)

    # Place the table to the right of the list box
    self.table_states.place(x=300, y=30)

  # ******************************************************************
  # Radiobuttons Callback Function
  # ******************************************************************  
  # Retrieve a list of 1-element tuples of distinct divisions for the
  # currently selected region
  def get_divisions(self):
    # Get the currently selected region
    region = ???

    # Connect to Cities.db and retrieve distinct divisions for the 
    # currently selected region into a list of 1-element tuples
    db_conn = sqlite3.connect('Cities.db')
    db_cursor = db_conn.cursor()
    sql_string = 
    sql_string += 
    db_cursor.execute(sql_string)
    division_recs = db_cursor.fetchall()
    db_conn.close()

    # Loop through division records to verify and convert to a simple
    # list of divisions
    division_list = []
    for ?? in ???:
      # print(rec)
      division_list.append(rec[0])

    # Check division_list before populating list box
    # for division in division_list:
    #  print(division)

    # Clear the Listbox first from previous region selection
    self.listbox_divisions.delete(0,'end')

    # Populate the Listbox with divisions
    for idx in range(len(division_list)):
      self.listbox_divisions.insert(idx, division_list[idx])
      
    # Select the first division in the list by default
    self.listbox_divisions.select_set(0)

    # Also need to clear Treeview table with state info
    # from previous region and division selections
    for item in self.table_states.get_children():
      self.table_states.delete(item)

    # The selected division is the first one at index 0
    div = self.listbox_divisions.get(0)
    # Get all the state info for the selected division
    self.get_states_info(div)

  # ******************************************************************
  # Retrieving State Information
  # ****************************************************************** 
  def get_states_info(self, division):
    # Connect to Cities.db and retrieve state information
    db_conn = sqlite3.connect('Cities.db')
    db_cursor = db_conn.cursor()
    sql_string = 
    sql_string += 
    sql_string += 
    sql_string += 
    sql_string += 
    sql_string += 
    sql_string += 
    sql_string += 
    db_cursor.execute(sql_string)
    state_recs = db_cursor.fetchall()

    # Clear the table before inserting
    for item in self.table_states.get_children():
      self.table_states.delete(item)

    # Insert records for the new state
    for ??? in ???:
      # Instead of printing we insert into tkinter table !!!
      # print(state_rec)     
      # Format the population figures and percent urban
      state_pop_2020 = f'{state_rec[1]:,.0f}'
      urban_pop_2020 = f'{state_rec[3]:,.0f}'
      pct_urban = f'{state_rec[4]:.2%}'
      
      # Create a formatted tuple for the current record
      state_rec_fmt = (???)
      # Insert formatted record into Treeview table
      # ***

    # Close DB connection
    db_conn.close()

  # ******************************************************************
  # <<LisboxSelect>> Callback Function
  # ******************************************************************  
  def proc_sel_div(self, e):
    # Find the index of the currently selected division
    div_idx = 
    # div_idx is a 1-element tuple, so you need div_idx[0]
    # to get the currently selected division
    div = 

    # Subsequent calls to get_states_info function
    # ***

# Create an instance of the RegionsDivisions class.
if __name__ == '__main__':
  regions_divisions = RegionsDivisions()
