# *****************************************************************************
# Lect7_04_06_Test_Scores.py
# *****************************************************************************
# Concepts covered:
# Reading from a file into a numerical list
# Iterating over list elements, list indexing
# List functions: min,  max
# Passing lists to and returning lists from functions
# List modification: sorting in asc
# *****************************************************************************
# Design a program that reads a list of test scores from test_scores.txt file.
# The program should store the scores in a list and then display the following
# information:
# * Total number of test scores in the file
# * The lowest score in the list and the index at which it occurred
# * The highest score in the list and the index at which it occurred
# * The average of scores in the list
# In addition, write a function scores_above_cutoff that accepts two arguments:
# a list of scores, and a number cutoff between min and max. The function should
# return all the scores in the list that are greater than the cutoff, find and 
# display the number of and the average of those scores.
# Next, use two # different ways to create copies of the test scores, sort and
# display them in both increasing and decreasing orders.
# Lastly, use list comprehension to create a list of scores at or below cutoff.
# *****************************************************************************
# Note: You must use the built in min() and max() functions to find the lowest
# and the highest scores, as well as index() function to find at which index
# do they occur. You must also use a function get_avg_score that accepts a 
# list of numbers and returns the average. 
# Test: There are 24 scores, 45 is the lowest at index 23, 99 the highest at
# index 3 (remember indexing starts at 0 and goes to 23). Average score is 83.25.
# With 80 as the high # score cutoff, there are 17 above the cutoff
# averaging to 89.18.
# *****************************************************************************

# Main function
def main():
  # Open test_scores.txt for reading
  scores_file = open('test_scores.txt', 'r')

  # Read the contents of the file into a list
  test_scores = scores_file.readlines()

  # Close the file
  scores_file.close()

  # Find and display the number of test scores in the file
  num_scores = 
  print('Total number of scores is', num_scores)

  # Iterate over the list converting strings to numbers
  # int() conversion function will automatically strip \n
  

  # Find and display the lowest score and index at which it occurred
  min_score = 
  min_idx = 
  print('The lowest score', min_score, 'occurred at index', min_idx)
  
  # Find and display the highest score and index at which it occurred
  max_score = 
  max_idx = 
  print('The highest score', max_score, 'occurred at index', max_idx)

  # Find and display the average test score
  average_score = 
  print(f'The average test score is {average_score:.2f}')

  # Enter the score cutoff between min and max
  cutoff_msg = 'Enter score between ' + str(min_score) \
               + ' and ' + str(max_score) + ': '
  score_cutoff = int(input(cutoff_msg))
  while score_cutoff < min_score or score_cutoff > max_score:
    print('ERROR: The cutoff must be between', min_score, 'and', max_score, '!')
    score_cutoff = int(input(cutoff_msg))

  # Get the scores above the cutoff, find and display the number and the average
  # of those scores
  high_scores = 
  num_high_scores = len(high_scores)
  avg_high_score = 
  print('There were', num_high_scores, end=' ')
  print(f'averaging to {avg_high_score:.2f}')

  # Use for-loop to create a copy of the list
  sorted_scores = []


  print()
  print('Sorted scores:', sorted_scores)
  print('Original order:', test_scores)

  # Use concatenation to create a copy of the list


  print()
  print('Reversed scores:', reversed_scores)
  print('Original order:', test_scores)

  # Use list comprehension to display the scores at or below cutoff
  
  print('Low scores', low_scores)

# end main()

def get_avg_score(scores):
  # Get the number of scores
  n = 

  # Set the accumulator
  tot_score = 0

  # Loop through the list accumulating the scores


  # Calculate and return the average
  avg_score = 0
  if n > 0:
    avg_score = tot_score / n
  return avg_score

def scores_above_cutoff(scores, cutoff):
  # Create an empty list of high scores
  high_scores = []

  # Loop through scores and append high ones
  for score in scores:


  # Return the high scores
  return high_scores

# Call the main
if __name__ == '__main__':
  main()
