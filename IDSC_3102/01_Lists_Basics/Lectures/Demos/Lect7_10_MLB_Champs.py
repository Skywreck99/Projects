# *****************************************************************************
# Lect7_10_MLB_Champs.py
# *****************************************************************************
# Concepts covered:
# Reading from a file into a string list
# Iterating over list elements, list indexing, comparing strings
# Passing lists to and returning value from functions
# List modification: inserting, appending, sorting
# *****************************************************************************
# The world_series_winners.txt file contains a chronological list of the World
# Series winning teams from 1903 through 2020, with 1904 and 1994 being the 
# only 2 years without the World Series. Write the program that performs the
# following tasks:
# * Searches through the list and counts the number of times Minnesota Twins 
#   won the World Series.
# * Inserts 'NA' at position 1 for 1904 and position 91 for 1994.
# * Sorts the list into a new list variable to preserve the original.
# * Use the sorted list to find the all time second best team (New York 
#   Yankees of course being the all time first).
# * Finds the years the second best team of all times won the World Series.
# *****************************************************************************
# Note: You must use the find_second_best() function for finding the second
# best team of all times by passing the sorted teams and returning the name
# of the team. 
# Test: Use the Excel file Lect7_Check_Lists.xlsx to validate the results.
# *****************************************************************************

# Main function
def main():
  # Open world_series_winners.txt for reading
  mlb_file = open('world_series_winners.txt', 'r')

  # Read the contents of the file into a list
  mlb_champs = mlb_file.readlines()

  # Close the file
  mlb_file.close()

  # Strip the \n from each team name



  # Confirm Minnesota Twins won World Series at least once
  search_team = 'Minnesota Twins'
  if 
    print(f'{search_team} won at least one World Series!')
    count_wins = 0
    # Then find out how many times


    print(search_team, 'won World Series', count_wins, 'times.')
  else:
    print(f'{search_team} never won a World Series!')
  print('******************************************************************')

  # Use the insert() method to add NA for years 1904 and 1994
  # Since 1904 is the 2nd year in this dataset the index is 1
  mlb_champs.insert(1, 'NA')
  # The index for 1994 should 1994 - 1903 = 91
  # Verify in Lect7_Check_Lists.xlsx
  mlb_champs.insert(91, 'NA')
  # So now adding 1903 to the index gives us the year
  
  # Make a copy of the list and sort it


  
  # Call the function to determine the all time second best
  second_best_team = 
  print(second_best_team, 'is the second best team of all times!')

  # Set the blank list for years won
  years_won = []

  # Find the years the second best team won
  for idx in range(len(mlb_champs)):
    if mlb_champs[idx] == second_best_team:
      

  # Print the years the second best team won
  print(years_won)

# end main()

def find_second_best(winners):
  # Set the counters
  second_max = 0
  count_wins = 1

  # Find the size of the list
  num_wins = len(winners)

  # Loop through the sorted list comparing adjacent teams
  for idx in range(1, num_wins):
    # If the two consecutive elements are the same, the
    # same team won, so we increase the counter
 
 
    # Otherwise compare to previous max and update
    # team and counter skipping Yankees
    else:
      if count_wins > second_max and winners[idx - 1] != 'New York Yankees':
        second_max = count_wins
        second_best_team = winners[idx - 1]
      count_wins = 1

  # Return the second best team
  # print(second_max)
  return second_best_team


# Call the main
if __name__ == '__main__':
  main()
