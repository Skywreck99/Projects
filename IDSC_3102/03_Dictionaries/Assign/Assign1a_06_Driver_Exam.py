# *****************************************************************************
# Assign1a_06_Driver_Exam.py
# *****************************************************************************
# The local driver's license office has asked you to create an application that
# grades the written portion of the driver's license exam. The exam has 20
# multiple-choice questions. The correct_answers are provided in the list at
# the top of main(). The program must read the student's answers for each
# of the 20 questions from a text file exam_answers.txt and store the answers
# in another list of student_answers.  After the student's answers have been
# read from the file, the program should display a message indicating whether
# the student passed or failed the exam. A student must correctly answer 15 of
# the 20 questions to pass the exam. The program should then display the total
# number of correctly answered questions, the total number of incorrectly 
# answered questions, and a list showing the question numbers of the incorrectly
# answered questions.
# *****************************************************************************
# Note: After reading the student_answers from the file and closing the file,
# you must strip the newline characters from each answer and find the number
# of student answers in num_answ variable. The program proceeds with the main
# task of determining pass/fail, printing the total number of correct answers
# and incorrect answers and listing the questions which were answered incorrectly.
# You must use a single function to accomplish these tasks:
# get_test_info(correct_answers, student_answers)
#   The function takes the correct and student answer lists and accumulates the
#   total score by checking the correct against student answers, and, at the
#   same time, builds the initially empty list of questions answered incorrectly.
#   The function returns two values: the total number of correct answers and the
#   list of questions answered incorrectly to the main().
# The main function receives both the total number of correct answers and the
# list of incorrectly answered questions and displays the result.
# *****************************************************************************
# Test: Your output should look like this:
# You passed the drivers exam!
# You answered 16 questions correctly and 4 incorrectly.
# You incorrectly answered these questions: [3, 4, 10, 17]
# *****************************************************************************
# Global constant
NUM_TO_PASS = 15

# Main function
def main():
  # Manually populate the list of correct answers
  correct_answers = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B',
                     'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']

  # Open exam_answers.txt for reading
  answ_file = open('exam_answers.txt', 'r')

  # Read the student answers into a list
  student_answers = answ_file.readlines()

  # Close the file
  answ_file.close()
  
  # Get the number of student answers
  num_answ = len(student_answers)

  # Iterate through the list stripping newline characters
  for idx in range(num_answ):
    student_answers[idx] = student_answers[idx].rstrip('\n')

  # Get the total number of correct answers and 
  # the list of incorrect questions
  total_correct, incorrect_questions = get_test_info(correct_answers, student_answers)

  # Check if total correct 15 or greater
  if total_correct >= NUM_TO_PASS:
    print('You passed the drivers exam!')
  else:
    print('You failed the drivers exam!')

  # Print the total number of correct and incorrect answers
  print('You answered', total_correct, 'questions correctly and ', end='')
  print(len(incorrect_questions), 'incorrectly.')

  # Display the list of incorrect questions
  print('You incorrectly answered these questions:', incorrect_questions)

def get_test_info(correct_answers, student_answers):
  # Get number of answers
  num_answ = len(student_answers)

  # Set counter to 0
  total_correct = 0

  # Initialize incorrect questions list to blank
  incorrect_questions = list()

  # Determine the total number of correct answers and build the
  # list of incorrect questions
  for idx in range(num_answ):
    # Check if the answers do not match
    if student_answers[idx] != correct_answers[idx]:
      # Add the incorrect question to the list using append()
      incorrect_questions.append(idx+1)
    else:
      # Increment the number of correct answers
      total_correct+=1

  # Return the total correct and the list of incorrect questions
  return total_correct, incorrect_questions

# Call the main
if __name__ == '__main__':
  main()
