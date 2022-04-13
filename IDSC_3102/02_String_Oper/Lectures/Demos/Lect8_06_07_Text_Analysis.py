# *****************************************************************************
# Lect8_06_07_Text_Analysis.py
# *****************************************************************************
# Concepts covered:
# Iterating, indexing, concatenating, testing, comparing, slicing and searching
# Testing for letters only, digits and special characters, search and replace
# Splitting and tokenizing
# *****************************************************************************
# Loosely based on problems 6 and 7 on page 463. Uses a text.txt file with
# one sentence per line for the purposes of demonstrating all the string
# manipulation concepts.
# *****************************************************************************
# Note: The program is broken into 7 exercises demonstrating major string
# manipulation concepts. Review the code for each exercise before running. 
# Test: Run the program and evaluate results against the code in each of
# the 5 exercises.
# *****************************************************************************
# Open text.txt for reading
text_file = open('text.txt', 'r')
# Read the contents into a list
contents = text_file.readlines()
# Close the file
text_file.close()

# *****************************************************************************
# *** 1. Iterating, Concatenating, Testing and Comparing
# contents[0] = 'Text File'
line = contents[0].rstrip('\n')
# Iterate over line character by character
all_lower = ''
for ch in line:
  # Test if uppercase -> convert to lowercase


print(all_lower)

# *****************************************************************************
# *** 2. Indexing, Concatenating, Testing and Slicing
# contents[1] = 'John Smith became our customer 10 years ago'
line = contents[1].rstrip('\n')
word_list = []
# Skip the first character
beg = 0
for idx in range(1, len(line)):


# Loop did not pick up the last word
word_list.append(line[beg:len(line)])
# Display result
print(word_list)

# *****************************************************************************
# *** 3. Searching and Slicing
# contents[2] = 'Extract John out of this sentence.'
line = contents[2].rstrip('\n')
# Find the position of substring John
substr = 'John'
pos = ???
print('Position:', pos)
# Slice it out of the string
slc = ???
# Display result
print('Slice:', slc)
# Bob is not part of this string
# Use find() instead of index() to avoid ValueError
pos = ???
if pos == -1:
  print('Bob was not found')
else:
  print('Position:', pos)

# *****************************************************************************
# *** 4. Simple Search and Replace
# contents[3] = 'We have John I and John II as our customers.'
line = contents[3].rstrip('\n')
# Set the search and replace strings
srch_str = 'John'
repl_str = 'Bob'
# Print line before search and replace
print('Line before:', line)
# Create a new line
new_line = ???
# Print the line after search and replace
print('Line after:', new_line)

# *****************************************************************************
# *** 5. Splitting and Tokenizing
# contents[4] = 'around and around we go'
line = contents[4].rstrip('\n')
# Split the line using space as delimiter
token_line = line.split(' ')
# Count the tokens
num_tokens = len(token_line)
# Initialize reversed line
rev_token_line = ''
for idx in range(num_tokens):
  # print(token_line[num_tokens - idx - 1])
  rev_token_line += ???
# Print result
print('Positive indexing:', rev_token_line.rstrip(' '))
# Reverse using negative indexing
reverse_line = ''
for idx in range(-1, -num_tokens - 1, -1):
  # print(token_line[idx])
  reverse_line += token_line[idx] + ' '
# Print result
print('Negative indexing:', reverse_line.rstrip(' '))
