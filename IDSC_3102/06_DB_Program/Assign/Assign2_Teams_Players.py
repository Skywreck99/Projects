# *****************************************************************************
# Assign2_Teams_Players.py
# *****************************************************************************
# This program is very loosely based on the material in Chapter 14 of the 5th
# edition of the textbook, but it does not specifically refer to any of the
# end-of-the chapter problems.
# *****************************************************************************
# Complete the GUI DB program that loads the listbox with MLB teams based on
# the selected league (American or Nation) radiobutton. When a team is selected,
# the program should display in the table all the players on that team,
# calculate and display the players batting average as hits divided by at bats,
# and sort the players descending on their batting average.
# *****************************************************************************
# Note: You must use the GUI design shown in the PDF using the required widgets
# and variable names. The design and functionality of an event-driven program
# is not a straightforward linear process, but rather involves quite a bit of
# trial and error until the program looks and works the way it should. You
# should expect to spend some time figuring this out.
# *****************************************************************************
# Test: Your output should look like it is shown in the PDF, but all the other
# combinations of input selection must produce correct results as well.
# *****************************************************************************

from lib2to3.pgen2.token import LEFTSHIFT
import tkinter
import tkinter.messagebox
import sqlite3
from tkinter import CENTER, RIGHT, ttk

class BaseballDB:
  # ********************************************************************
  # Designing Baseball DB Application
  # ********************************************************************
  def __init__(self):
    # Create the main window widget
    self.main_window = tkinter.Tk()
    # Display a title
    self.main_window.title('Player Stats')
    # Adjust size and prevent resizing
    self.main_window.geometry('450x300')
    self.main_window.resizable(False, False)

    # Radiobuttons widgets for the American and National leagues
    self.radio_buttons()
    
    # Listbox of team names from which to select a single team 
    self.list_box()
    
    # tkinter Treeview table widget for displaying player info
    # for the currently selected team
    self.table()

    # Populate the initial list with teams from the American league
    self.get_teams()

    # The selected team is the first one at index 0 (Angels)
    team = self.listbox_teams.get(self.listbox_teams.curselection()[0])

    # Initial call to get_player_info function to retrieve the player
    # stats on the default team (Angels)
    self.get_players_info(team)
    
    # Bind <<ListboxSelect>> event to proc_sel_team callback function
    # This will trigger an event when a team selection is changed
    self.listbox_teams.bind('<<ListboxSelect>>', lambda e:
                            self.proc_sel_team(e))
    
    # Enter the tkinter main loop
    tkinter.mainloop()

  # ******************************************************************
  # Radiobuttons for Leagues
  # ******************************************************************   
  def radio_buttons(self):
    # Displays a label for leagues
    self.label_leagues = tkinter.Label(self.main_window,
                                    text='Choose league')
    self.label_leagues.place(x=30, y=20)

    # Builds a frame that will contain American and National leagues
    self.frame_leagues = tkinter.Frame(self.main_window)
    self.frame_leagues.config(bd=1, relief=tkinter.SOLID)
    self.frame_leagues.place(x=30, y=40)

    # Create a StringVar object to use with the radio buttons
    self.league = tkinter.StringVar()

    # Set the StringVar object to the 'American' league
    self.league.set('American')

    # Designs 2 Radiobutton widgets for American and National leagues.
    self.rb_american = tkinter.Radiobutton(self.frame_leagues,
                                       text='American',
                                       variable=self.league,
                                       value='American',
                                       command=self.get_teams)
    self.rb_american.pack(anchor='w')

    self.rb_national = tkinter.Radiobutton(self.frame_leagues,
                                       text='National',
                                       variable=self.league,
                                       value='National',
                                       command=self.get_teams)
    self.rb_national.pack(anchor='w')

  # ******************************************************************
  # Listbox of Team Names
  # ******************************************************************   
  def list_box(self):
    # Displays a label for team selection
    self.label_teams = tkinter.Label(self.main_window,
                                    text='Select team')
    self.label_teams.place(x=30, y=100)

    # Create a Listbox of team names with the SINGLE list item
    # selection mode, height of 8 teams and witdth of 20.
    self.listbox_teams = tkinter.Listbox(self.main_window,
                                         selectmode=tkinter.SINGLE,
                                         height=8, width=20)
    # Position the Listbox at (30, 120)
    self.listbox_teams.place(x=30, y=120)

  # ******************************************************************
  # Treeview Table of Player Information
  # ******************************************************************  
  def table(self):
    # Displays a label for result display
    self.label_players = tkinter.Label(self.main_window,
                                    text='Display players')
    self.label_players.place(x=180, y=20)
    
    # Setup tkinter Treeview table with 'player' and 'bat_avg'
    # for the column IDs with the height of 10 players
    column_ids = ('player', 'bat_avg')
    self.table_players = ttk.Treeview(self.main_window,
                                      column=column_ids,
                                      show='headings',
                                      height=10)
    
    # Define headings (see PDF for the text and alignment)
    self.table_players.heading('player', text='Player Name', anchor='w')
    self.table_players.heading('bat_avg', text='Batting Avg', anchor='e')

    # Configure column widths to 150 for player and 75 for bat_avg
    self.table_players.column('player', width=150)
    self.table_players.column('bat_avg', width=75)

    # Place the table to the right of the radiobuttons and the list
    # box at (180,40)
    self.table_players.place(x=180, y=40)

  # ******************************************************************
  # Radiobuttons Callback Function
  # ******************************************************************  
  # Retrieve a list of 1-element tuples (because of the SINGLE list
  # item selection model) of individual teams from the currently
  # selected league.
  def get_teams(self):
    # Get the selected league from the self.league StringVar
    league = self.league.get()
    
    # Connect to Baseball.db and retrieve team names for the currently
    # selected league. See bottom of the PDF file.
    db_conn = sqlite3.connect('Baseball.db')
    # Get the cursor
    db_cursor = db_conn.cursor()
    sql_string = 'SELECT TeamName '
    sql_string += 'FROM Team WHERE League = "' + league + '" '
    # Execute query
    db_cursor.execute(sql_string)
    # Fetch the results
    team_recs = db_cursor.fetchall()
    # Close the connection
    db_conn.close()

    # Clear the Listbox from previous league selection
    self.listbox_teams.delete(0,'end')

    # Clear the Treeview table with player info from previous
    # league and/or team selections
    for item in self.table_players.get_children():
      self.table_players.delete(item)

    # Populate the Listbox with team names
    for idx in range(len(team_recs)):
      team = team_recs[idx][0]
      # Insert team at idx position in the listbox
      self.listbox_teams.insert(idx, team)
      
    # Select the first team by default
    self.listbox_teams.select_set(0)

    # Get the first selected team at index 0 
    team = self.listbox_teams.select_set(0)

    # Get all the player info for the selected team
    return team

  # ******************************************************************
  # Retrieving Player Stats
  # ****************************************************************** 
  def get_players_info(self, team):
    # Connect to Baseball.db and retrieve player stats, which includes
    # his name and batting average defined as hits divided by at bats,  
    # for the currently selected team, sorted descending on the batting 
    # average. See bottom of the PDF file.
    db_conn = sqlite3.connect('Baseball.db')
    db_cursor = db_conn.cursor()
    sql_string = 'SELECT PlayerName, Hits/AtBats AS BatAvg '
    sql_string += 'FROM Team INNER JOIN Player '
    sql_string += 'ON Team.TeamID = Player.TeamID '
    sql_string += 'WHERE TeamName="' + team + '" '
    sql_string += 'ORDER BY BatAvg DESC'
    db_cursor.execute(sql_string)
    player_recs = db_cursor.fetchall()
    db_conn.close()

    # Clear the Treeview table before inserting
    for item in self.table_players.get_children():
      self.table_players.delete(item)

    # Insert player records into the Treeview table
    for player_rec in player_recs:
      # Format the batting average to 3 decimals
      bat_avg = f'{player_rec[1]:,.3f}'
      # Create a formatted tuple for the current record
      player_rec_fmt = (player_rec[0], bat_avg)
      # Insert the formatted tuple into the Treeview table
      self.table_players.insert('', tkinter.END, value=player_rec_fmt)

  # ******************************************************************
  # <<LisboxSelect>> Callback Function
  # ******************************************************************  
  def proc_sel_team(self, e):
    # Find the index of the currently selected team
    team_idx = self.listbox_teams.curselection()
    # team_idx is a 1-element tuple, so you need team_idx[0]
    # to get the currently selected team    
    team = self.listbox_teams.get(team_idx[0])

    # Subsequent calls to get_players_info function
    self.get_players_info(team)

# Creates an instance of the BaseballDB class.
if __name__ == '__main__':
  baseball = BaseballDB()




