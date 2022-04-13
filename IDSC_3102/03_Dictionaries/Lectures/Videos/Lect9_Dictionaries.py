# **********************************************************************
# Slide #4: Basic Dictionary Operations
# **********************************************************************
# *** Creating a customer dictionary with name:city key:value pairs
cust_cities = {
  'Ryan': 'Santa Fe',
  'Ellen': 'Albuquerque',
  'Bob': 'Albuquerque'
  }
cust_cities

# *** Retrieving value from dictionary based on its key
# Lookup Bob's city - displays Albuquerque
cust_cities['Bob']
# Look up where John lives - generates KeyError exception
cust_cities['John']

# Testing whether the key exists before using it
if 'Bob' in cust_cities:
  print(cust_cities['Bob'])
if 'John' not in cust_cities:
  print('John is not our customer!')

# *** Modifying dictionary by adding new key-value pairs
# Adding customer to dictionary
cust_cities['Ted'] = 'Santa Fe'
# Display total number of elements in the dictionary
num_cust = len(cust_cities) # Returns 4

# Careful about adding another Ted from Taos
cust_cities['Ted'] = 'Taos'
# Recalculate number of elements
num_cust = len(cust_cities) # Still returns 4
# This is because dictionary cannot have duplicate keys
# The existing Tod's city was changed from Santa Fe to Taos

# *** Iterating over the dictionary
for key in cust_cities:
  print(key, cust_cities[key])

# Delete Ted after checking he exists
if 'Ted' in cust_cities:
  del cust_cities['Ted']

num_cust = len(cust_cities) # Back to original 3
for key in cust_cities:
  print(key, cust_cities[key])
  type(key)
  
# **********************************************************************
# Slide #5: Dictionary Methods
# **********************************************************************
# The get() method allows you to provide default value
# if key is not found
cust_cities.get('Ted', 'Ted was just deleted')
cust_cities.get('Bob', 'Bob is no longer with us')

# The keys(), values() and items() methods return immutable tuples
# which are more secure and faster to process

# The keys() method is used to return keys as a dict_keys tuple
cc_keys = cust_cities.keys()
cc_keys
type(cc_keys)
for key in cc_keys:
  print(key)

# The values() method is used to return values as a dict_values tuple
cc_vals = cust_cities.values()
cc_vals
type(cc_vals)
for val in cc_vals:
  print(val)

# The items() method returns the key-value pairs as dict_items tuples
cc_items = cust_cities.items()
cc_items
type(cc_items)
for item in cc_items:
  print(item)

# Both pop() and popitem() methods remove key-value pairs if the
# key exists, or display the provided default if not
# pop() returns the value of an item about to be removed
val = cust_cities.pop('Bob')
print(val, 'was removed from dict')
cust_cities

# popitem() returns the key-value pair the last item to be removed
key, val = cust_cities.popitem()
print(key,'from',val,'was removed from dict')
cust_cities

# The clear() method is used to clear all the key-value pairs
# from the dict and leave an empty dictionary
cust_cities.clear()
cust_cities

# **********************************************************************
# Slide #6: Duplicate Key Challenge
# **********************************************************************
# Challenge of maintaining unique or non-duplicated keys
# Adding a Bob from Taos (a different customer) will not work
cust_cities = {
  'Ryan': 'Santa Fe',
  'Ellen': 'Albuquerque',
  'Bob': 'Albuquerque'
  }
cust_cities['Bob'] = 'Taos'  # Taos will replace Albuquerque
cust_cities

# Creative, but a bit too complicated solution could be
cust_cities = {
  (1, 'Ryan'): 'Santa Fe',
  (2, 'Ellen'): 'Albuquerque',
  (3, 'Bob'): 'Albuquerque',
  (4, 'Bob'): 'Taos'
  }

# It does show the flexibility of different approaches
for key in cust_cities.keys():
  if key[1] == 'Bob':
    print(cust_cities[key])

# Better to use unique key such as user_id
cust_info = {
  'rmurphy1234': 'Santa Fe',
  'eharper3210': 'Albuquerque',
  'bwilliams99': 'Albuquerque'
  }
cust_info

# So a different Bob (Collins) from Taos would simply have a 
# different user_id and would not be confused with Bob from Albuquerque
cust_info['bcollins976'] = 'Taos'
for info in cust_info.items():
  print(info)

# **********************************************************************
# Slide #7: More Complex Dictionaries
# **********************************************************************
# What if we want to maintain first name information in addition
# to the city? One solution is that the value associated with a key is
# a list or another dict, or a combination of both list and dict (later).
cust_info = {
  'rmurphy1234': ['Ryan','Santa Fe'],
  'eharper3210': ['Ellen','Albuquerque'],
  'bwilliams99': ['Bob','Albuquerque']
  }
for key in cust_info.keys():
  print(key)
for val in cust_info.values():
  print(val)

# Now it gets a bit more complicated because we want to add the
# basic loan info to the current data structure. So, in addition to
# the first_name and city, the 3rd list element is loan_info, which
# itself is a list with variable number of dicts whose key:value
# pairs represent loan_type:mth_pmt.
cust_info = {
  'rmurphy1234': ['Ryan','Santa Fe',[{'Mortg': 661.44},{'Car': 762.1}]],
  'eharper3210': ['Ellen','Albuquerque',[{'Mortg': 1705.96},{'Other': 457.26},{'Car': 603.5}]],
  'bwilliams99': ['Bob','Albuquerque',[{'Mortg': 3925.64}]]
  }

# While you can still see the overall structure, Ryan with 2 loans
# (mortgage and car), Ellen with 3 (mortgage, car and other) and Bob
# with one mortgage loan, the brackets and braces and the different
# data structures are a bit more difficult to disentangle.
for cust_val in cust_info.values():
  for loan_dict in cust_val[2]:
    for loan_key in loan_dict:
      print(cust_val[0], cust_val[1], loan_key, loan_dict[loan_key], sep=',')

# Shows how to convert a relatively complex data structure into
# row and column CSV format

# **********************************************************************
# Slide #8: Dictionaries and JSON Files
# **********************************************************************
# See Lect9_Dict_JSON.py
