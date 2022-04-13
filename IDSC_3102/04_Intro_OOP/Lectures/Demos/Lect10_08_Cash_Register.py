# *****************************************************************************
# Lect10_08_Cash_Register.py
# *****************************************************************************
# Concepts Covered:
# Working with objects that contain other objects as attributes
# Working with lists of objects
# *****************************************************************************
# This problem is loosely based on Problem 8, page 581 in Ch. 10.
# This exercise assumes you completed the RetailItem class in retailitem.py
# file. Next complete the CashRegister class that can be used with the
# RetailItem class in the cashregister.py file. The CashRegister class is
# designed to be able to internally keep a list of RetailItem objects, add new
# RetailItem objects, calculate and display the total for the order, and show
# the list of items in the "cash register".
# Once you have finished the CashRegister class, complete the main program below
# that creates two RetailItem objects, stores the given data, creates an object
# of CashRegister class, adds the first retail item to the order, calculates and
# displays the order total, and displays the current content of the cash register.
# Next, the second retail item is added to the same order, the total is
# recalculated and redisplayed at the end.
# *****************************************************************************
# Note: The CashRegister class is to be completed in cashregister.py Python
# file. You must use the retail_item as the name of the object created from the
# the RetailItem class and my_order for the object of the CashRegister class.
# The rest of the variable names are up to you.
# *****************************************************************************
# Test: Your input should use following data on two retail items: 
# 1) description ('Jacket'), inventory on hand (12) and price (59.95)
# 2) description ('Shirt'), inventory on hand (20) and price(24.95)
# Your output should look like this:
# The item was added to the order.
# The items in your order are:
# -----------------------------------------------
# Description: Jacket
# -----------------------------------------------
# The order total is: $59.95
# 
# Creating another order item for the same order!
# The item was added to the order.
# The items in your order are:
# -----------------------------------------------
# Description: Jacket
# Description: Shirt
# -----------------------------------------------
# The order total is: $84.90
# *****************************************************************************

# Import RetailItem and CashRegister classes
import retailitem
import # ***

# Main function
def main():
  # Create objects of RetailItem class named retail_item (Jacket)
  retail_item = retailitem.RetailItem('Jacket', 12, 59.95)

  # Create an object of CashRegister class named my_order
  my_order = 
  # Add the retail item created above (a Jacket) to the order
  # ***

  # Show what is in the order, i.e., the content of the "cash register"
  # ***
  
  # Use the calc_total method to calculate and display the current order total
  # ***
  print()

  print('Creating another order item for the same order!')
  # Create another object of RetailItem class named retail_item (Shirt)
  retail_item = retailitem.RetailItem('Shirt', 20, 24.95)
  # Add the Shirt to the same order
  my_order.add_item(retail_item)

  # Show again what is in the order, i.e., the content of the "cash register"
  my_order.display_items()

  # Recalculate the total and redisplay the confirmation number with the
  # new (and final) order total
  my_order.calc_total() 
  
# Call the main
if __name__ == '__main__':
  main()
