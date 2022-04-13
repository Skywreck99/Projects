# **********************************************************************
# CashRegister Class
# **********************************************************************
# Concepts Covered:
# Object of one class as attribute of another class - object hierarchy
# List of objects as an attribute of a class
# **********************************************************************

import # ***

class CashRegister:

  # The __init__ method accepts arguments defining a cash register
  def __init__(self):
    # Assigns the values of parameters to appropriate attributes
    # ***

  # The add_item adds an object of RetailItem class to the list
  def add_item(self, item):
    # ***
    print('The item was added to the order.')
  
  # The calc_ord_total calculates the total for the order, displays
  # the confirmation number and the total itself
  def calc_total(self):
    tot = 0.0
    # ***
    
    print('The order total is: $', format(tot, ',.2f'), sep='')

  # The display_items() method shows the list of items processed
  # by the cash register
  def display_items(self):
    print('The items in the cash register are:')
    print('-----------------------------------------------')
    for item in self.__items:
      print(item.get_description())
    print('-----------------------------------------------')
