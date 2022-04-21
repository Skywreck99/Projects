# *****************************************************************************
# Assign2_04_C-F_Convert.py
# *****************************************************************************
# Write a GUI program that converts Celsius temperatures to Fahrenheit
# temperatures or Fahrenheit to Celsius. The user should be able to enter an
# input temperature, select the type of conversion, click a button, then see
# the equivalent temperature. Use the following formulas to make the
# conversions:
#  From Fahrenheit to Celsius
#   C = (5/9)*(F - 32)
#  From Celsius to Fahrenheit
#   F = (9/5)*C + 32
# F is the Fahrenheit temperature, and C is the Celsius temperature.
# *****************************************************************************
# Note: You must use the GUI design shown in the PDF using the required widget
# and variable names provided both in the code below and the PDF. The relevant
# demo files to copy/paste/modify code appropriately are Lect13_03_MPG_Calc and
# Lect13_06_Auto_Shop.py.
# *****************************************************************************
# Test: Your output should look like this (two separate executions):
# 
# Temperature: 25.2
# Celsius to Fahrenheit option selected
# Converted temperature 77.4
# 
# Temperature: 68.7
# Fahrenheit to Celsius option selected
# Converted temperature 20.4
# *****************************************************************************

# Import both tkinter and tkinter.messagebox libraries
import tkinter
import tkinter.messagebox

class TempConvert:
  # ********************************************************************
  # Creating and Sizing the Main Window
  # ********************************************************************
  def __init__(self):
    # Create the main window widget
    self.main_window = tkinter.Tk()
    # Display the title 'Temperature Converter'
    self.main_window.title("Temperature Converter")
    # Adjust size to 350 x 200 and prevent resizing
    self.main_window.geometry("350x200")
    self.main_window.resizable(False, False)

    # Create labels for temperature, conversion type and the result
    self.display_labels()

    # Create command buttons for making the conversion and quitting
    # the application
    self.command_buttons()

    # Create an input entry widget for the temperature
    self.input_entry()

    # Create conversion type radio buttons within a frame
    self.radio_buttons()

    # Use a label to display conversion result
    self.convert_temp()
    
    # Enter the tkinter main loop
    tkinter.mainloop()

  # ******************************************************************
  # Displaying and Positioning input temperature, conversion type and
  # output temperature Label Widgets
  # ******************************************************************
  def display_labels(self):
    # Create/display a label for temperature in the main window
    # with the text 'Temperature'
    self.label_temp = tkinter.Label(self.main_window, text="Temperature: ")
    
    # Position the label in the top-left corner at (30, 20)
    self.label_temp.place(x=30, y=20)
    
    # Create/display a label for conversion type in the main window
    # with the text 'Conversion Type'
    self.label_convert_type = tkinter.Label(self.main_window, text="Conversion Type")
    
    # Position the label below the temperature label at (30, 60)
    self.label_convert_type.place(x=30, y=60)

    # Display label associated for the result in the main window
    # with the text 'Converted temperature'
    self.label_result = tkinter.Label(self.main_window, text="Converted Temperature")
    
    # Position the label towards the bottom at (30, 150)
    self.label_result.place(x=30, y=150)

  # ******************************************************************
  # Temperature Input Entry Widget
  # ******************************************************************
  def input_entry(self):
    # Create an input entry box in the main window for a user to enter
    # the temperature. The width should be 8.
    self.entry_temp = tkinter.Entry(self.main_window, width=8)
    
    # Position the input entry widget at (120, 20)
    self.entry_temp.place(x=120, y=20)
    # Use the focus() method to set the focus to the input entry box.
    self.entry_temp.focus()

  # ******************************************************************
  # Conversion Type Radiobutton Widgets within a Frame
  # ******************************************************************
  def radio_buttons(self):
    # Build a frame in the main window that will contain conversion
    # type choices. Configure the frame with bd=1 and SOLID relief.
    self.frame_convert_type = tkinter.Frame(self.main_window)
    self.frame_convert_type.config(bd=1, relief=tkinter.SOLID)
    # Position the frame at (30, 80)
    self.frame_convert_type.place(x=30, y=80)

    # Create the IntVar object to use with the radio buttons
    self.convert_type = tkinter.IntVar()

    # Set the IntVar object to 1 representing Fahrenheit to Celsius
    # conversion. 2 will represent Celsius to Fahrenheit conversion.
    self.convert_type.set(1)

    # Design 2 Radiobutton widgets for the 2 conversion types. The
    # text for the first button should be 'Fahrenheit to Celsius',
    # 'Celsius to Fahrenheit' for the second. The variable is 
    # self.convert_type and the values 1 and 2, respectively, 
    # as described above.
    # Create/display the first button
    self.rb_FC = tkinter.Radiobutton(self.frame_convert_type,
                                    text = "Fahrenheit to Celsius",
                                    variable = self.convert_type,
                                    value=1)
    
    # Pack the first button into the frame
    self.rb_FC.pack()

    # Create/display the second button
    self.rb_CF = tkinter.Radiobutton(self.frame_convert_type,
                                    text = "Celsius to Fahrenheit",
                                    variable = self.convert_type,
                                    value=2)
    
    # Pack the second button into the frame
    self.rb_CF.pack()

  # ******************************************************************
  # Creating Convert and Quit Button Widgets
  # ******************************************************************
  def command_buttons(self):
    # Create/display the command button for temperature conversions
    # in the main window. The text is 'Convert', with height of 2 and
    # width of 15. The command parameter is set to self.convert_temp
    # callback function
    self.button_convert = tkinter.Button(self.main_window,
                                        text="Convert",
                                        height=2,
                                        width=15,
                                        command=self.convert_temp)
    
    # Position the button towards the top-right corner at (200,20)
    self.button_convert.place(x=200,y=20)

    # Create/display the Quit button to close the application. The
    # button should have the same height and width as the one above,
    # calling the main_window.destroy method when clicked on.
    self.button_quit = tkinter.Button(self.main_window,
                                        text="Quit",
                                        height=2,
                                        width=15,
                                        command=self.main_window.destroy)
    
    # Position Quit button right below the Calculate button at (200,70)
    self.button_quit.place(x=200,y=70)

  # ******************************************************************
  # Using Labels as Output Fields for Converted Temperature
  # ******************************************************************
  def output_labels(self):
    # Create a StringVar object to associate with the output label
    self.convert_temp = tkinter.StringVar()

    # Create a label for the converted temperature output in the main
    # window. The textvariable parameter must be set to self.convert_temp
    self.label_convert_temp = tkinter.Label(self.main_window,
                                            textvariable=self.convert_temp)
    
    # Position the label at (160,150)
    self.label_convert_temp.place(x=160,y=150)

  # ******************************************************************
  # Callback Function for Convert Command Button
  # ******************************************************************     
  def convert_temp(self):
    # Gather all the inputs to calculate the temperature conversion
    try:
      # Get the user-entered temperature from the input entry box
      temp_txt = self.entry_temp.get()
      if temp_txt:
        
          # Convert it to a float
          temperature = float(temp_txt)

          # Get the appropriate conversion type
          convert_type = self.convert_type.get()
          # If the conversion type is 1, you have Fahrenheit to Celsius conversion
          if convert_type == 1:
            # Calculate celsius based on temperature (which is in Fahrenheit)
            celsius = (5/9)*(temperature - 32)
            # Display the result in the self.convert_temp label formated to 1 digit
            self.label_result.config(text = "Converted Temperature " + str(format(celsius, ".1f"))) # (use celsius somewhere)
            #self.convert_temp.set(f'{celsius:,.1f}')
          # Otherwise it must be Celsius to Fahrenheit conversion
          else:
            # Calculate fahrenheit based on temperature (which is in Celsius)
            fahrenheit = (9/5)*temperature + 32
            # Display the result in the self.convert_temp label formated to 1 digit
            self.label_result.config(text = "Converted Temperature " + str(format(fahrenheit, ".1f")))
            #self.convert_temp.set(f'{fahrenheit:,.1f}')

    except ValueError:
      # Display error message: 'You must enter a valid temperature!'
      tkinter.messagebox.showinfo('ERROR!',
                                  'You must enter a valid temperature!')

# Create an instance of the TempConvert class.
if __name__ == '__main__':
  temp_convert = TempConvert()