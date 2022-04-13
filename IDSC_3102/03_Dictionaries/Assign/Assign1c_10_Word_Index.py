# *****************************************************************************
# Assign1c_10_Word_Index.py
# *****************************************************************************
# Write a program that reads the contents of kennedy.txt file. The program
# should create a dictionary in which the key-value pairs are described as
# follows:
# * Key: the keys are the individual words found in the file.
# * Values: each value is a list that contains the line numbers in the file
#   where the word (the key) is found.
# Once the dictionary was built, the program should create another text file, 
# known as a word index, listing the contents of the dictionary. The index.txt
# file should contain an alphabetical listing of the words that are stored as
# keys in the dictionary, along with the line numbers where the words appear
# in the original text file. 
# *****************************************************************************
# Note: You must start with the empty word_dict dictionary, loop through the
# file lines, line by line, and split each line into a list called words. Then
# you must loop through the words list checking if a particular word is in the
# word_dict or not. If yes, you append the line number to the already existing
# list, if not, you must start the list with the current line number. Finally,
# use the items() method to get the sorted dictionary shown below.
# *****************************************************************************
# Test: Your output should look like this:
# We [1]
# observe [1]
# today [1]
# not [1]
# a [1, 2, 4]
# victory [1]
# of [2, 3]
# party [2]
# but [2]
# celebration [2]
# freedom [3]
# symbolizing [3]
# an [3]
# end [3]
# as [4, 5, 6]
# well [4, 5]
# beginning [4]
# signifying [5]
# renewal [5]
# change [6]
# *****************************************************************************

# Main function
def main():
  # Open the file for reading
  text_file = open('kennedy.txt', 'r')

  # Read the contents of the file into lines list
  lines = text_file.readlines()

  # Close the file
  text_file.close()

  # Initialize the word dictionary
  word_dict = {}

  # Loop through the lines, stripping the newline character
  # splitting a line in a list of words
  for idx in range(len(lines)):
    lines[idx] = lines[idx].rstrip('\n')
    words = lines[idx].split(' ')
    # Loop through the words
    for w in words:
      # Check if the word is already in the dictionary
      if w in word_dict.keys():
        #If yes, append the line number to the values, unless already there
        if idx+1 not in word_dict[w]:
          word_dict[w] += [idx+1]
      # Word not yet in the dict, add it with add it with line number as value
      else:
        word_dict[w] = [idx+1]

  # Using items() should show the sorted dictionary
  for key, value in word_dict.items():
    print(key, value)

# Call the main
if __name__ == '__main__':
  main()
