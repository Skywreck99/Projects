# *****************************************************************************
# Lect13_03_MPG_Calc.py
# *****************************************************************************
# Concepts Covered:
# Defining Graphical User Interface (GUI) based event driven programming.
# Describing tkinter GUI library, part of standard Python installation.
# Importing tkinter, creating root widget and naming it main_window.
# Running tkinter main loop method until the main window is closed.
# Working with tkinter widgets: Frame, Label, Entry, Button,...
# Organizing widgets with frames placed using the "grid Geometry Manager".
# Displaying labels, entry boxes and command buttons within each frame using
# the basic "pack()" method with appropriate frame and widget padding.
# Using "get()" method of entry box widget to retrieve and convert user input.
# Using "command" attribute of the command button to call the user-defined
# function designed to execute a set of actions associated with the button.
# Using "destroy" method of main_window to end the program execution.
# Using StringVar object to hold the calculated MPG output value and display it
# in a label used as an output field.
# *****************************************************************************
# Write a GUI program that calculates a car's gas milage. The program's window
# should have Entry widgets that let the user enter the number of gallons of
# gas the car holds, and the number of miles it can be driven on a full tank.
# When a Calculate MPG button is clicked, the program should display the number
# of miles that the care may be driven per gallon of gas. Use the following
# formula to calculate miles per gallon: MPG = miles / gallons.
# *****************************************************************************
# Note: All the GUI-based programs will be contained in the single class, where
# the __init__ constructor creates the main window and calls the appropriate
# functions used to defined the user interface and implement the functionality.
# *****************************************************************************
# Test: The application should be tested with reasonable input first, say 300
# miles on 13 gallons should yield 23.1 miles per gallon. You must also make
# sure the appropriate error messages are displayed, using tkinter.messagebox
# if the input is missing or is otherwise inappropriate. 
# *****************************************************************************

import tkinter
import tkinter.messagebox

class MPGCalcGUI:
  # ********************************************************************
  # Creating and Sizing the Main Window
  # ********************************************************************
  def __init__(self):
    # Create the main window widget
    self.main_window = tkinter.Tk()
    # Display a title
    self.main_window.title('MPG Calculator')
    # Adjust size and prevent resizing
    self.main_window.geometry('300x200')
    self.main_window.resizable(False, False)

    # Labels for miles, gallons and miles per gallon
    self.display_labels()

    # Input entry widgets for the miles and gallons
    self.input_entry()

    # Command buttons for making the conversion and quitting the app
    self.command_buttons()

    # Using a label to display conversion result
    self.output_labels()
    
    # Enter the tkinter main loop
    tkinter.mainloop()
  
  # ******************************************************************
  # Creating and Positioning Miles, Gallons and MPG Label Widgets
  # ******************************************************************
  def display_labels(self):
    # Create frame for miles label
    # ***
    # self.frame_label_miles.config(bd=1, relief=tkinter.SOLID)
    # Position the label in the first row, first column
    self.frame_label_miles.grid(row=0, column=0, padx=5, pady=5, sticky='w')
    # Label for miles
    # ***
    
    # Display label for miles
    self.label_miles.pack(padx=15, pady=10)
   
    # Create frame for gallons label
    self.frame_label_gallons = tkinter.Frame(self.main_window)
    self.frame_label_gallons.config(bd=1, relief=tkinter.SOLID)
    # Position the label in the second row, first column
    self.frame_label_gallons.grid(row=1, column=0, padx=5, pady=5, sticky='w')
    # Label for gallons
    self.label_gallons = tkinter.Label(self.frame_label_gallons,
                                   text='Gallons')
    # Display label for gallons
    self.label_gallons.pack(padx=15, pady=5)

    # Create frame for MPG label
    self.frame_label_mpg = tkinter.Frame(self.main_window)
    # Position the label in the third row, first column
    self.frame_label_mpg.grid(row=2, column=0, padx=5, pady=5, sticky='w')
    # Label for miles per gallon
    self.label_mpg = tkinter.Label(self.frame_label_mpg,
                                   text='MPG')
    # Display label for MPG
    self.label_mpg.pack(padx=15, pady=5)
    
  # ******************************************************************
  # Creating and Positioning Miles and Gallons Input Entry Widgets
  # ******************************************************************
  def input_entry(self):
    # Create frame for miles entry box
    self.frame_entry_miles = tkinter.Frame(self.main_window)
    # Position the entry box in the first row, second column
    self.frame_entry_miles.grid(row=0, column=1, padx=5, pady=5)
    # Entry box for miles
    # ***
    
    # Display entry box for miles
    self.entry_miles.pack(padx=5, pady=10)
    self.entry_miles.focus()

    # Create frame for gallons entry box
    self.frame_entry_gallons = tkinter.Frame(self.main_window)
    # Position the entry box in the second row, second column
    self.frame_entry_gallons.grid(row=1, column=1, padx=5, pady=5)
    # Entry box for gallons
    self.entry_gallons = tkinter.Entry(self.frame_entry_gallons,
                                       width=8)
    # Display entry box for gallons
    self.entry_gallons.pack(padx=5, pady=5)

  # ******************************************************************
  # Creating and Positioning Calculate, Clear and Quit Button Widgets
  # ******************************************************************
  def command_buttons(self):
    # Create frame for Calculate button
    self.frame_button_calc = tkinter.Frame(self.main_window)
    # Position the button in the first row, third column
    self.frame_button_calc.grid(row=0, column=2, padx=5, pady=5)
    # Command button for MPG calculation
    # ***
    
    
    # Display Calculate button
    self.button_mpg.pack(padx=5, pady=10)

    # Create frame for Clear button
    self.frame_button_clear = tkinter.Frame(self.main_window)
    # Position the button in the second row, third column
    self.frame_button_clear.grid(row=1, column=2, padx=5, pady=5)
    # Command button for MPG calculation
    self.button_clear = tkinter.Button(self.frame_button_clear,
                                      text='Clear',
                                      height=2, width=15,
                                      command=self.clear_input)
    # Display Clear button
    self.button_clear.pack(padx=5, pady=5)

    # Create frame for Quit button
    self.frame_button_quit = tkinter.Frame(self.main_window)
    # Position the button in the third row, third column
    self.frame_button_quit.grid(row=2, column=2, padx=5, pady=5)
    # Quit button to close the application
    self.button_quit = tkinter.Button(self.frame_button_quit,
                                      text='Quit',
                                      height=2, width=15,
                                      command=self.main_window.destroy)
    # Display Quit button
    self.button_quit.pack(padx=5, pady=5)

  # Creating user-defined function that calculates miles per gallon
  # using try-except to catch division by zero and invalid miles
  # and/or gallons input entries
  def calc_mpg(self):
    try:
      # Gather all the inputs
      # ***
      miles = float(miles_txt)

      gallons_txt = self.entry_gallons.get()
      gallons = float(gallons_txt)
      
      # Calculate MPG
      mpg = abs(miles) / abs(gallons)

      # Display result
      # ***
      
    except ZeroDivisionError:
      tkinter.messagebox.showinfo('ERROR!',
                                  'Number of gallons cannot be zero!')

    except ValueError:
      tkinter.messagebox.showinfo('ERROR!',
                          'You must enter valid miles and gallons!')

  # Creating user-defined function that clears miles and gallons
  # input entry widgets, output MPG label and shifts focus to
  # miles input entry widget
  def clear_input(self):
    # Clear miles entry box
    self.entry_miles.delete(0, 'end')
    # Clear gallons entry box
    self.entry_gallons.delete(0, 'end')
    # Clear MPG output label
    self.MPG.set('')
    # Refocus back to miles entry box
    self.entry_miles.focus()

  # ******************************************************************
  # Using Labels as Output Fields for MPG
  # ******************************************************************
  def output_labels(self):
    # Create a StringVar object to associate with the output label
    # ***

    # Create frame for MPG output label, this is a separate
    # label from the one actually used to label it
    self.frame_label_MPG = tkinter.Frame(self.main_window)
    # Position the label in the third row, second column
    self.frame_label_MPG.grid(row=2, column=1, padx=5, pady=5)
    # ***
    
    # Display label for miles
    self.label_MPG.pack(padx=5, pady=5)

# Create an instance of the MPGCalcGUI class.
if __name__ == '__main__':
  mpg_calc = MPGCalcGUI()
