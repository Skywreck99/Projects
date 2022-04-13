# **********************************************************************
# RetailItem Class
# **********************************************************************
# Concepts Covered:
# Class - a template from which objects are created
# __init__ - initializer method, aka object constructor
# attributes - properties / characteristics of objects
# methods - functions implementing actions/behavior of objects
# accessor (get) methods - read the data from object attributes
# mutator (set) methods - write the data to object attributes
# **********************************************************************

# ***

  # The __init__ method accepts arguments defining the retail item
  def __init__(self, desc, inv, prc):
    # Assigns the values of parameters to appropriate attributes
    # ***

  # The get methods read the data from object attributes
  def get_description(self):
    # ***

  def get_inventory(self):
    return self.__inventory

  def get_price(self):
    return self.__price

  # The set methods write the data to object attributes
  def set_description(self, desc):
    # ***

  def set_inventory(self, inv):
    if inv > 0 and inv <= 1000:
      self.__inventory = inv
    else:
      self.__inventory = 0

  def set_price(self, prc):
    if prc > 0 and prc <= 1000:
      self.__price = prc
    else:
      self.__price = 0

  # The calc_inventory_value function returns the current inventory
  # value for a single product item
  def calc_inventory_value(self):
    return 
