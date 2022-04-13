# **********************************************************************
# Slide #3: String Indexing
# **********************************************************************
# Once defined, the string cannot be changed
full_name = 'Smith, John'

# Iterate over string, character by character
for ch in full_name:
  print(ch)

# String indexing
full_name[5]     # Displays the comma enclosed in single quotes
full_name[-5]    # Displays the space enclosed in single quotes
len(full_name)   # Returns 11 as the length of the string

# Strings are immutable, once defined they cannot be changed
# Assume we want the first name to read Joey
full_name[9] = 'e'    # Neither of these assignments will work
full_name[10] = 'y'   # Throws TypeError exception

# Attempting to access element beyond the end of the string
# will result in a run-time IndexError exception
full_name[11]

# **********************************************************************
# Slide #4: String Concatenating & Slicing
# **********************************************************************
# *** Concatenation
# Appears to modify strings, but in fact does not
emp_name = 'Smith'
print(emp_name)
# Every time we concatenate, a new string variable is created
emp_name += ', '
print(emp_name)
# The fact that the variable name is the same does not matter
emp_name += 'John'
print(emp_name)

# Iterate over string until you hit the comma
full_name = 'Smith, John'
last = ''
idx = 0
while full_name[idx] != ',':
  last += full_name[idx]
  idx += 1
print(last)

# *** Slicing
full_name = 'Smith, John'
idx = 0
lgth = len(full_name)
for idx in range(-1, -lgth - 1, -1):
  print(idx, full_name[idx])
  if full_name[idx] == ' ':
    spc_idx = idx
    break
print(spc_idx)
first = full_name[spc_idx + 1:]
print(first)

# **********************************************************************
# Slide #5: String Methods - Modifying & Testing
# **********************************************************************
full_name = 'Smith, John'
full_name.upper()

last = 'Smith'
first = 'John'
dig = '123'

# Constructing user name
user_name = first[0] + last + dig
print(user_name)
user_name = user_name.lower()
print(user_name)

# Constructing password
user_pass = first[0] + last[0] + 'pass' + dig + '!'
print(user_pass)
# Testing password
counts = [0, 0, 0, 0, 0]
for ch in user_pass:
  # Count all characters
  counts[0] += 1
  # Count uppercase letters
  if ch.isalpha() and ch == ch.upper():
    counts[1] += 1
  # Count number of digits
  elif ch.isdigit():
    counts[2] += 1
  # Count non-alphanumerical characters
  elif not ch.isalnum():
    counts[3] += 1
  elif ch.isspace():
    counts[4] += 1
print('Password has', counts[0], 'characters.')
print('Password has', counts[1], 'uppercase letters.')
print('Password has', counts[2], 'digits.')
print('Password has', counts[3], 'special characters.')
print('Password has', counts[4], 'spaces.')

# **********************************************************************
# Slide #6: String Methods - Searching
# **********************************************************************
full_name = 'Smith, John'
# Using find() method
comma_indx = full_name.find(',')
comma_indx
last = full_name[:comma_indx]
print(last)

# Using index() method
spc_indx = full_name.index(' ')
spc_indx
first = full_name[spc_indx + 1:]
print(first)

# Using replace() method
new_name = full_name.replace('John', 'Joey')
print(new_name)

# Using startswith(), endswith() methods
last = 'Smith'
first = 'John'
if full_name.startswith(last) and full_name.endswith(first):
  print('The name is:', first, last)

# **********************************************************************
# Slide #7: String Methods - Splitting
# **********************************************************************
full_name = 'Smith, John'
delimiter = ', '
tokens = full_name.split(delimiter)
print('First name is:', tokens[1])
print('Last name is:', tokens[0])

# Reading simple and clean CSV files
def main():
  # Open CSV file for reading
  loans_csv_file = open('Loans.csv', 'r')

  # Read CSV file into a list
  loans = loans_csv_file.readlines()

  # Close CSV file
  loans_csv_file.close()

  # Process the loans
  for line in loans:
    # Get the current loan info by tokenizing line string
    loan = line.split(',')

    # Calculate and display payment to loan ratio
    pmt = float(loan[5])
    amt = float(loan[3])
    pmt_loan_ratio = 1000 * pmt / amt
    print(f'Payment to loan ratio is ${pmt_loan_ratio:,.2f}')
