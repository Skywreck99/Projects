# *****************************************************************************
# Lect9_07_MLB_Winners.py
# *****************************************************************************
# Concepts covered:
# Creating dictionary element by element from an empty dictionary
# Adding elements to a dictionary
# Accessing keys and values in a dictionary
# Testing if a key is in a dictionary
# Using for loop to iterate over a dictionary
# *****************************************************************************
# The world_series_winners.txt file contains a chronological list of the World
# Series winning teams from 1903 through 2020, with 1904 and 1994 being the 
# only 2 years without the World Series. Write the program that reads the file
# and creates a dictionary in which the keys are the names of the teams and
# each key's associate value is the number of time team has won the World
# Series. The program should also create a dictionary in which the keys are
# the years and each key's associated value is the name of the team that won
# that year. The program should prompt the user for a year in the range of
# 1903 through 2020. It should then display the name of the team that won the
# World series that year and the number of times that team has won the World
# Series.
# *****************************************************************************
# Note: You should use the code from Lect7_10_MLB_Champs.py to insert 'NA' for
# the 2 missing years 1904 and 1994.
# Test: Use the Excel file Lect7_Check_Lists.xlsx to validate the results.
# *****************************************************************************

# Main function
def main():
  # Open world_series_winners.txt for reading
  mlb_file = open('world_series_winners.txt', 'r')

  # Read the contents of the file into a list
  mlb_winners = mlb_file.readlines()

  # Close the file
  mlb_file.close()

  # Strip the \n from each team name
  for idx in range(len(mlb_winners)):
    
    
  # Set 2 empty dictionaries, one for team wins and
  # another for years won
  team_wins = 
  for idx in range(len(mlb_winners)):
    # Each list element is a team key
    team_key = 
    # If the team key already in dictionary, increment value by 1
    if :
      
    # Team not in dictionary, add it with the first World Series win
    else:
      

  # Print directory of teams wins


# end main()

# Call the main
if __name__ == '__main__':
  main()
