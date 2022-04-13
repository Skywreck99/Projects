# **********************************************************************
# Slide #4: Creating Lists
# **********************************************************************
# List of strings
customers = ['Ryan Murphy', 'Ellen Harper', 'Bob Williams']
customers
# List of numbers
payments = [661.44, 1705.96, 1239.68, 3925.64]
print(payments)
loan_ids = list(range(1024, 1031, 3))
loan_ids
# List of items of different data types
loan = [1027, 'Ellen Harper', 1705.96]
print(loan)

# **********************************************************************
# Slide #5: Basic List Operations
# **********************************************************************
# *** Indexing *** 
nums = [1, 2] * 3
nums
nums[0]
nums[3]
size = len(nums)
nums[-2]
nums[size] # IndexError
nums[size-1]

# *** Iterating *** 
# Without an index
for num in nums:
  print(num)
# With an index
for idx in range(size):
  print(idx, nums[idx])

# **********************************************************************
# Slide #6: Basic Operations (cont.)
# **********************************************************************
# Modifying
for idx in range(2, size):
  nums[idx] = idx + 1
# Initializing and populating
rev_nums = [0] * 6
rev_nums
for idx in range(len(rev_nums)):
  rev_nums[idx] = len(rev_nums) - idx
rev_nums

# *** Concatenating *** 
# Join two lists together into a third list
all_nums = nums + rev_nums
all_nums
# Append one list to another
nums += rev_nums
nums

# **********************************************************************
# Slide #7: Basic Operations (cont.)
# **********************************************************************
# *** Slicing *** 
nums[2:4]  # Returns 3rd & 4th elements at indx 2 & 3
# Variations
first4 = nums[:4]
remain = nums[7:]
skip2 = nums[1:10:2]
last3 = nums[-3:]

# *** Searching *** 
# Use the in operator to determine if a customers is in the list
cust_srch = input('Enter customer name: ')
if cust_srch in customers:
  print(f'{cust_srch} was found in the customer list.')
else:
  print(f'{cust_srch} was NOT found in the customer list.')
# Use Ellen Harper to find her as a customer

# Use the not in operator to determine if a customers is not in the list
cust_srch = input('Enter customer name: ')
if cust_srch not in customers:
  print(f'{cust_srch} was NOT found in the customer list.')
else:
  print(f'{cust_srch} was found in the customer list.')
# Use John Smith to fail the search

# *** Copying ***
# Assigning one list variable to another will NOT make a copy
nums_copy = nums
nums_copy
nums_copy[0] = 123456
nums_copy
nums
nums[0] = 1
nums

# Omit both the start and the end slicing indices
nums_copy1 = nums[:]
nums_copy1[0] = 123456
nums_copy1
nums

# Concatenate blank list to the existing list
nums_copy2 = [] + nums
nums_copy2[0] = 123456
nums_copy2
nums

# Initialize a list and populate it with elements in a loop
nums_copy3 = [0] * len(nums)
for idx in range(len(nums)):
  nums_copy3[idx] = nums[idx]
nums_copy3[0] = 123456
nums_copy3
nums

# **********************************************************************
# Slide #8: List Methods - append, index and insert
# **********************************************************************
# Append correct loan ID of 1031 to the loans_ids list
loan_ids = list(range(1024, 1031, 3))
loan_ids
new_id = 1031
loan_ids.append(new_id)
loan_ids

# Append incorrect customer name to the customers list
customers = ['Ryan Murphy', 'Ellen Harper', 'Bob Williams']
customers
new_cust = 'Craig Holden'
customers.append(new_cust)
customers

# Get the index of the loan id and changed it
id_indx = loan_ids.index(new_id)
id_indx
loan_ids[id_indx] = 1034
loan_ids

# Attempting to index an non-existing item throws ValueError
no_indx = loan_ids.index(1031)

# Insert another loan ID and customer right before recent additions
loan_ids.insert(id_indx, 1031)
loan_ids
customers.insert(id_indx, 'Max Entermann')
customers

# **********************************************************************
# Slide #9: List Method remove and del Statement
# **********************************************************************
# Remove the last loan id of 1034
loan_ids.remove(1034)
loan_ids

# Use del statement to delete Craig Holden using his index
del_indx = customers.index('Craig Holden')
del_indx
del customers[del_indx]
customers

# **********************************************************************
# Slide #10: List Methods sort and reverse and min/max List Functions
# **********************************************************************
# Recreate the payments list
payments = [661.44, 1705.96, 1239.68, 3925.64]
# Sort the payments
payments.sort()
payments
# Reversing the sorted payments sorts them descending
payments.reverse()
payments
# Get back the original list
payments = [661.44, 1705.96, 1239.68, 3925.64]

# Find the lowest/highest payments
pmt_min = min(payments)
pmt_min
pmt_max = max(payments)
pmt_max

# Find the first and last customer (alphabetically)
cust_first = min(customers)
cust_first
cust_last = max(customers)
cust_last
