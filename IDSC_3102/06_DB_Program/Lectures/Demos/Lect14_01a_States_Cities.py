# *****************************************************************************
# Lect14_01a_States_Cities.py
# *****************************************************************************
# This program is very loosely based on Problem 01, page 796 in Chapter 14 of
# the 5th edition of the textbook. I expanded the database by including state
# information and added all the cities in the US with population of more than
# 100,000 people as of last 2020 census, as well as 2010 census for comparison.
# *****************************************************************************
# Complete the GUI DB program that loads the listbox with state names, but only
# for those states with any cities over 100,000. When a state is selected, the
# program should display in the table all the cities in that state, as well as
# 2020 and 2010 census population, and also calculate and display the percent
# change between the two census counts.
# *****************************************************************************
# Note: You must use the GUI design shown in the PDF using the required widgets
# and variable names as much as possible. The design and functionality of such
# an event-driven program is not a straightforward linear process, but rather
# involves quite a bit of trial and error until the program looks and works the
# way it should. You should expect to spend some time figuring this out.
# *****************************************************************************
# Test: Run the program for multiple states to verify it produces the desired
# results. California has a few cities with 0 (missing) for 2010 population.
# *****************************************************************************
import tkinter
import tkinter.messagebox
import sqlite3
from tkinter import ttk
class StatesCities:
  # ********************************************************************
  # Designing States-Cities DB Application
  # ********************************************************************
  def __init__(self):
    # Create the main window widget
    self.main_window = tkinter.Tk()
    # Display a title
    self.main_window.title('States and Cities')
    # Adjust size and prevent resizing
    self.main_window.geometry('650x300')
    self.main_window.resizable(False, False)
    # Design Listbox of state names
    self.list_box()
    
    # Setup tkinter Treeview table widget for displaying city info
    self.table()
    # Find the index of the currently selected state
    st_idx = self.listbox_states.curselection()
    # st_idx is a 1-element tuple, so you need st_idx[0]
    # to get the currently selected state
    st_name = self.listbox_states.get(st_idx[0])
    # Initial call to get_cities_info function to retrieve the city
    # info on the default state
    self.get_cities_info(st_name)
    
    # Bind <<ListboxSelect>> event to proc_sel_state callback function
    self.listbox_states.bind('<<ListboxSelect>>', lambda e:
                                 self.proc_sel_state(e))
    
    # Enter the tkinter main loop
    tkinter.mainloop()
  # ******************************************************************
  # Listbox of State Names
  # ******************************************************************   
  def list_box(self):
    # Display a label for state selection
    self.label_states = tkinter.Label(self.main_window,
                                    text='Select state')
    self.label_states.place(x=30, y=20)
    # Create a Listbox of state names
    self.listbox_states = tkinter.Listbox(self.main_window,
                                         selectmode=tkinter.SINGLE,
                                         height=10, width=20)
    self.listbox_states.place(x=30, y=40)
    # Connect to Cities.db and retrieve state names
    db_conn = sqlite3.connect('Cities.db')
    db_cursor = db_conn.cursor()
    db_cursor.execute('SELECT StateName FROM States')
    state_recs = db_cursor.fetchall()
    # Populate the Listbox with state names
    for idx in range(len(state_recs)):
      st_name = state_recs[idx][0]
      # Does state have any cities?
      sql_string = 'SELECT COUNT(*) AS NumCities '
      sql_string += 'FROM States INNER JOIN Cities '
      sql_string += 'ON States.StateID=Cities.StateID '
      sql_string += 'WHERE StateName="' + st_name + '"'
      db_cursor.execute(sql_string)
      num_cities = db_cursor.fetchall()
      # print(num_cities[0][0])
      if num_cities[0][0] > 0:
        self.listbox_states.insert(idx, st_name)
      
    # Select 22-nd state of Minnesota by default
    self.listbox_states.select_set(21)
    # Adjusts the position so that you can see the default state
    self.listbox_states.see(17)
    # Close DB connection
    db_conn.close()
  # ******************************************************************
  # Treeview Table of City Information
  # ******************************************************************  
  def table(self):
    # Display a label for result display
    self.label_cities = tkinter.Label(self.main_window,
                                    text='Display cities')
    self.label_cities.place(x=180, y=20)
    
    # Setup tkinter Treeview table
    column_ids = ('city','pop_2020','pop_2010','pct_chg')
    self.table_cities = ttk.Treeview(self.main_window,
                                    column=column_ids, show='headings',
                                    height=10)
    # Define headings
    self.table_cities.heading('city', anchor='w', text='City Name')
    self.table_cities.heading('pop_2020', text='Pop 2020')
    self.table_cities.heading('pop_2010', text='Pop 2010')
    self.table_cities.heading('pct_chg', text='% Change')
    # Configure column widths
    self.table_cities.column('city', width=150)
    self.table_cities.column('pop_2020', anchor='e', width=100)
    self.table_cities.column('pop_2010', anchor='e', width=100)
    self.table_cities.column('pct_chg', anchor='e', width=75)
    # Place the table to the right of the list box
    self.table_cities.place(x=180, y=40)
  # ******************************************************************
  # <<LisboxSelect>> Callback Function
  # ******************************************************************  
  def proc_sel_state(self, e):
    # Find the index of the currently selected state
    st_idx = self.listbox_states.curselection()
    # st_idx is a 1-element tuple, so you need st_idx[0]
    # to get the currently selected state    
    st_name = self.listbox_states.get(st_idx[0])
    # Subsequent calls to get_cities_info function
    self.get_cities_info(st_name)
  # ******************************************************************
  # Retrieving City Information
  # ****************************************************************** 
  def get_cities_info(self, st_name):
    # Connect to Cities.db and retrieve city information
    db_conn = sqlite3.connect('Cities.db')
    db_cursor = db_conn.cursor()
    sql_string = 'SELECT CityName, Cities.Pop2020, Pop2010 '
    sql_string += 'FROM States INNER JOIN Cities '
    sql_string += 'ON States.StateID = Cities.StateID '
    sql_string += 'WHERE StateName="' + st_name + '"'
    db_cursor.execute(sql_string)
    city_recs = db_cursor.fetchall()
    # Clear the table before inserting
    for item in self.table_cities.get_children():
      self.table_cities.delete(item)
    # Insert records for the new city
    for city_rec in city_recs:
      # Instead of printing we insert into tkinter table !!!
      # print(city_rec)
      # Calculate the percent change in population
      if city_rec[2] > 0:
        pct_chg = (city_rec[1]-city_rec[2])/city_rec[2]
      else:
        pct_chg = 0
      
      # Format the population figures and percent change
      pop_2020 = f'{city_rec[1]:,.0f}'
      pop_2010 = f'{city_rec[2]:,.0f}'
      pct_chg = f'{pct_chg:.2%}'
      
      # Create a formatted tuple for the current record
      city_rec_fmt = (city_rec[0], pop_2020, pop_2010, pct_chg)
      self.table_cities.insert('', tkinter.END, values=city_rec_fmt)
    # Close DB connection
    db_conn.close()
# Create an instance of the StatesCities class.
if __name__ == '__main__':
  states_cities = StatesCities()