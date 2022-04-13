# *****************************************************************************
# Lect10_05_Retail_Items_Inventory.py
# *****************************************************************************
# Concepts Covered:
# Creating an instance of an object
# Using accessor (get) methods to read the data out of the object's attributes
# Using "regular" methods to perform operations on object's attributes
# Using mutator (set) methods to write new data into the object's attributes
# *****************************************************************************
# This problem is loosely based on Problem 5, page 580 in Ch. 10.
# Complete a class named RetailItem in retailitem.py file that holds data about
# an item available for sale. The class stores the following data in attributes:
# description, inventory and price. Complete all the accessor and mutator  
# methods next, followed by calc_inventory_value method that multiplies the
# number of units on hand (inventory) with the item's price.
# Once you have finished the class, complete the main program below that
# creates a single retail item object, stores the given data, displays it
# back, calculates and displays the current inventory value, updates the
# inventory and recalculates and displays the updated (new) inventory value.
# *****************************************************************************
# Note: The class must be completed in retailitem.py Python file, imported and 
# used in the main below. You must use the retail_item as the name of the object
# created from the RetailItem class. The rest of the variable names are up to
# you, I suggest short names for various attributes (desc, cur_inv, prc)
# and calculated inventory values (cur_inv_val), etc..
# *****************************************************************************
# Test: Your input should use following data on a single product: description
# ('Shirt'), inventory on hand (20) and price (24.95). In addition, assume 2
# units of the product were purchased.
# Your output should look like this:
# Our Shirt item retails for $24.95
# There are 20 Shirt items currently on inventory!
# The current inventory value for Shirt item is $499.00
# The updated inventory for Shirt item is 18 units!
# The updated inventory value for Shirt item is $449.10
# *****************************************************************************

import # ***

# Main function
def main():
  # Create an object of the RetailItem class named retail_item
  # and populate it with test data
  # ***

  # Use the get accessor methods to display the data
  desc = 
  cur_inv = retail_item.get_inventory()
  prc = retail_item.get_price()
  print('Our', desc, 'item retails for', f'${prc:,.2f}')
  print('There are', cur_inv, desc, 'items currently on inventory!')

  # Use the calc_inventory_value method to obtain and display the
  # current inventory value of the product
  cur_inv_val = 
  print('The current inventory value for', desc,
        'item is', f'${cur_inv_val:,.2f}')
  
  # Adjust the inventory using the appropriate mutator method
  new_inv = retail_item.get_inventory() - 2
  # ***
  upd_inv = retail_item.get_inventory()
  print('The updated inventory for', desc, 'item is', upd_inv, 'units!')

  # Use the calc_inventory_value method to obtain and display the
  # updated / new inventory value of the product
  new_inv_val = retail_item.calc_inventory_value()
  print('The updated inventory value for', desc,
        'item is', f'${new_inv_val:,.2f}')

# Call the main
if __name__ == '__main__':
  main()
