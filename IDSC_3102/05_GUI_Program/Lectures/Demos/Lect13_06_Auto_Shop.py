# *****************************************************************************
# Lect13_06_Auto_Shop.py
# *****************************************************************************
# Concepts Covered:
# Working with additional tkinter widgets: Checkbutton and Radiobutton
# Organizing widgets with the exact placement with "place Geometry Manager" 
# *****************************************************************************
# Joe's Automotive performs the following routine maintenance services:
# * Oil change - $30.00
# * Lube job - $20.00
# * Radiator flush - $40.00
# * Transmission flush - $100.00
# * Inspection - $35.00
# * Muffler replacement - $200.00
# * Tire rotation - $20.00
# Write a GUI program with check buttons that allow the user to select any or
# all of these services, select one of the three options for how fast the 
# customer needs their vehicle back and the estimated part's cost. "Two days"
# turnaround adds $100.00 to the job, $50.00 for "2-5 business days", and $0.00
# for "Within week". When the user clicks a button, the total estimated
# charges should be displayed.
# *****************************************************************************
# Note: All the GUI-based programs will be contained in the single class, where
# the __init__ constructor creates the main window and calls the appropriate
# functions used to defined the user interface and implement the functionality.
# *****************************************************************************
# Test: The application should be tested various combination of inputs,
# verifying the additions are preformed correctly.
# *****************************************************************************

import tkinter
import tkinter.messagebox

class AutoShopGUI:
  # ********************************************************************
  # Creating and Sizing the Main Window
  # ********************************************************************
  def __init__(self):
    # Create the main window widget
    self.main_window = tkinter.Tk()
    # Display a title
    self.main_window.title('Auto Shop Calculator')
    # Adjust size and prevent resizing
    self.main_window.geometry('550x250')
    self.main_window.resizable(False, False)

    # Labels for parts cost, services, turnaround, and total cost
    self.display_labels()

    # Command buttons for calculating total estimated charges
    # and quitting the application
    self.command_buttons()

    # Input entry widget for parts cost
    self.input_entry()

    # Check buttons for all the services
    self.check_buttons()

    # Turnaround radio buttons within a frame
    self.radio_buttons()

    # Using a label to display the resulting total charges
    self.output_labels()
    
    # Enter the tkinter main loop
    tkinter.mainloop()

  # ******************************************************************
  # Creating and Positioning Label Widgets
  # ******************************************************************
  def display_labels(self):
    # Display a label for the cost of parts
    self.label_parts_cost = tkinter.Label(self.main_window,
                                   text='Parts cost')
    # Position the label in the top-left corner
    # ***

    # Display a label for the list of services
    self.label_services = tkinter.Label(self.main_window,
                                   text='Services')
    # Position the label right below the parts cost
    self.label_services.place(x=30, y=40)

    # Display a label for the service turnaround
    self.label_turnaround = tkinter.Label(self.main_window,
                                   text='Turnaround')
    # Position the label towards the top middle
    self.label_turnaround.place(x=250, y=40)

    # Display a label for the total charges
    self.label_total_charges = tkinter.Label(self.main_window,
                                   text='Total charges')
    # Position the label towards the bottom middle
    self.label_total_charges.place(x=350, y=200)

  # ******************************************************************
  # Creating Button Widgets and Using Info Dialog Boxes
  # ******************************************************************
  def command_buttons(self):
    # Command button for total estimated charge calculation
    self.button_calc = tkinter.Button(self.main_window,
                                      text='Calculate',
                                      height=2, width=10,
                                      command=self.calc_tot_cost)
    # Position Calculate button towards the top-right corner
    self.button_calc.place(x=450, y=20)

    # Quit button to close the application
    self.button_quit = tkinter.Button(self.main_window,
                                      text='Quit',
                                      height=2, width=10,
                                      command=self.main_window.destroy)
    # Position Quit button right below Calculate button
    self.button_quit.place(x=450, y=70)
    
  def calc_tot_cost(self):
    # Accumulate total cost
    total_cost = 0.0
    try:
      # Get the parts cost
      parts_txt = self.entry_parts_cost.get()
      parts_cost = float(parts_txt)
      total_cost += parts_cost

      # Add the cost of selected services
      # ***
      
      if self.cb_lube_var.get() == 1:
        total_cost += 20.00
      if self.cb_radiator_var.get() == 1:
        total_cost += 40.00
      if self.cb_transmission_var.get() == 1:
        total_cost += 100.00
      if self.cb_inspection_var.get() == 1:
        total_cost += 35.00
      if self.cb_muffler_var.get() == 1:
        total_cost += 200.00
      if self.cb_tire_var.get() == 1:
        total_cost += 20.00

      # Add the cost of faster turnaround
      # ***
      if turnaround == 1:
        total_cost += 100.00
      elif turnaround == 2:
        total_cost += 50.00
      else:
        total_cost += 0.0

      # Display the result
      self.total_cost.set(f'${total_cost:,.2f}')

    except ValueError:
      tkinter.messagebox.showinfo('ERROR!',
                                  'You must enter valid parts cost!')

  # ******************************************************************
  # Input Entry Widgets and Handling User Input
  # ******************************************************************
  def input_entry(self):
    # Input entry box for user to enter parts cost
    self.entry_parts_cost = tkinter.Entry(self.main_window,
                                   width=12)
    # Place it towards the top middle
    self.entry_parts_cost.place(x=100, y=15)
    self.entry_parts_cost.focus()

  # ******************************************************************
  # Checkbuttons for Services
  # ******************************************************************   
  def check_buttons(self):
    # Create a frame to hold all service check buttons
    self.frame_services = tkinter.Frame(self.main_window)
    self.frame_services.config(bd=1, relief=tkinter.SOLID)
    self.frame_services.place(x=30, y=60)

    # Create seven IntVar objects to use with the Checkbuttons
    # ***
    self.cb_lube_var = tkinter.IntVar()
    self.cb_radiator_var = tkinter.IntVar()
    self.cb_transmission_var = tkinter.IntVar()
    self.cb_inspection_var = tkinter.IntVar()
    self.cb_muffler_var = tkinter.IntVar()
    self.cb_tire_var = tkinter.IntVar()

    # Set all the IntVar objects to 0 indicating none are selected
    # ***
    self.cb_lube_var.set(0)
    self.cb_radiator_var.set(0)
    self.cb_transmission_var.set(0)
    self.cb_inspection_var.set(0)
    self.cb_muffler_var.set(0)
    self.cb_tire_var.set(0)

    # Create the Checkbutton widgets in the frame
    # ***
    
    
    self.cb_lube_job = tkinter.Checkbutton(self.frame_services,
                                      text='Lube job - $20.00',
                                      variable=self.cb_lube_var)
    self.cb_radiator_flush = tkinter.Checkbutton(self.frame_services,
                                      text='Radiator flush - $40.00',
                                      variable=self.cb_radiator_var)
    self.cb_transmission_flush = tkinter.Checkbutton(self.frame_services,
                                      text='Transmission flush - $100.00',
                                      variable=self.cb_transmission_var)
    self.cb_inspection = tkinter.Checkbutton(self.frame_services,
                                      text='Inspection - $35.00',
                                      variable=self.cb_inspection_var)
    self.cb_muffler_replacement = tkinter.Checkbutton(self.frame_services,
                                      text='Muffler replacement - $200.00',
                                      variable=self.cb_muffler_var)    
    self.cb_tire_rotation = tkinter.Checkbutton(self.frame_services,
                                      text='Tire rotation - $20.00',
                                      variable=self.cb_tire_var)

    # Pack the Checkbuttons into the frame
    # ***
    self.cb_lube_job.pack(anchor='w')
    self.cb_radiator_flush.pack(anchor='w')
    self.cb_transmission_flush.pack(anchor='w')
    self.cb_inspection.pack(anchor='w')
    self.cb_muffler_replacement.pack(anchor='w')
    self.cb_tire_rotation.pack(anchor='w')

  # ******************************************************************
  # Turnaround Radiobutton Widgets within a Frame
  # ******************************************************************
  def radio_buttons(self):
    # Build a frame that will contain turnaround options
    self.frame_turnaround = tkinter.Frame(self.main_window)
    self.frame_turnaround.config(bd=1, relief=tkinter.SOLID)
    self.frame_turnaround.place(x=250, y=60)

    # Create the IntVar object to use with the radio buttons
    # ***

    # Set the IntVar object to option 2: 2-5 business days
    # ***

    # Design 3 Radiobutton widgets for 3 turnaround options
    # ***
    
    

    self.rb_2_5days = tkinter.Radiobutton(self.frame_turnaround,
                                       text='2-5 business days - $50.00',
                                       variable=self.turnaround,
                                       value=2)
    self.rb_2_5days.pack(anchor='w')

    self.rb_week = tkinter.Radiobutton(self.frame_turnaround,
                                       text='Within week - $0.00',
                                       variable=self.turnaround,
                                       value=3)
    self.rb_week.pack(anchor='w')

    
  # ******************************************************************
  # Using Labels as Output Fields
  # ******************************************************************
  def output_labels(self):
    # Create a StringVar object to associate with output label
    self.total_cost = tkinter.StringVar()

    # Create a label for total cost output
    self.label_total_cost = tkinter.Label(self.main_window,
                                   textvariable=self.total_cost)
    self.label_total_cost.place(x=450, y=200)

# Create an instance of the AutoShopGUI class.
if __name__ == '__main__':
  auto_shop = AutoShopGUI()
