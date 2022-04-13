# *****************************************************************************
# Lect7_Nested_Lists.py
# *****************************************************************************
# Concepts covered:
# Working with numerical nested lists
# Reading from a file into a list
# Splitting list elements into sub-lists for analysis
# *****************************************************************************
# Design a program that reads a list of quiz scores from quiz_attempts.txt
# file. Each line contains tab separated multiple attempts by the same student.
# The program should store the scores in a list, where each element represents
# all the attempts by the same student as a sub-list and then display the
# following information:
# * The highest score for each student
# * The average of scores for each student
# *****************************************************************************
# Note: You must use the built in max() functions to find the the highest
# scores, you must also use a function get_avg_score that accepts a list of
# numbers and returns the average. 
# Test: Compare with Lect7_Check_Lists.xlsx, Nested worksheet.
# *****************************************************************************

# Main function
def main():
  # Open quiz_attempts.txt for reading
  scores_file = open('quiz_attempts.txt', 'r')

  # Read the contents of the file into a list
  quiz_scores = scores_file.readlines()

  # Close the file
  scores_file.close()

  # Find and display the number of students in the file
  num_stds = len(quiz_scores)

  # Iterate over the list, splitting the attempts in sub-lists
  # and then converting strings to integers
  for std in range(num_stds):
    quiz_scores[std] = quiz_scores[std].split('\t')
    # Calculate number of attempts by student
    num_attempt = len(quiz_scores[std])
    for score in range(num_attempt):
      quiz_scores[std][score] = int(quiz_scores[std][score])

  # Check what we have so far
  # print(quiz_scores)

  # Iterate over the list of lists calculating and displaying
  # the maximum and average scores by the students
  for std in range(num_stds):
    # Calculate max and average scores for each student
    max_score = max(quiz_scores[std])
    avg_score = get_avg_score(quiz_scores[std])
    # Display the max and average scores of each student
    print(f'Max and average scores for student {std + 1:2} are: ', end='')
    print(f'{max_score} and {avg_score:.2f}')

# end main()

def get_avg_score(scores):
  # Get the number of scores
  n = len(scores)

  # Set the accumulator
  tot_score = 0

  # Loop through the list accumulating the scores
  for score in scores:
    tot_score += score

  # Calculate and return the average
  avg_score = 0
  if n > 0:
    avg_score = tot_score / n
  return avg_score

# Call the main
if __name__ == '__main__':
  main()
