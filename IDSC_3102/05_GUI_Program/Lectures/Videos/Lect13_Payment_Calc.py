# **********************************************************************
# GUI Programming: Payment Calculator Application
# **********************************************************************

import tkinter
import tkinter.messagebox

class PmtCalcGUI:
  # ********************************************************************
  # Slide #06: Creating and Sizing the Main Window
  # ********************************************************************
  def __init__(self):
    # Create the main window widget
    self.main_window = tkinter.Tk()
    # Display a title
    self.main_window.title('Payment Calculator')
    # Adjust size to 600 x 800 and prevent resizing
    self.main_window.geometry('350x250')
    self.main_window.resizable(False, False)

    # Display labels for amount borrowed and montly payment
    self.display_labels()

    # Input entry widget for amount borrowed
    self.input_entry()

    # Loan term radio buttons within frames
    self.radio_buttons()

    # List box of interest rates
    self.list_box()

    # Command buttons for calculating monthly payment
    # and quitting the application
    self.command_buttons()

    # Using a label to display resulting monthly payment
    self.output_labels()
    
    # Enter the tkinter main loop
    tkinter.mainloop()

  # ******************************************************************
  # Slide #07: Displaying and Positioning Label Widgets
  # ******************************************************************
  def display_labels(self):
    # Display a label for the amount borrowed
    self.label_amt = tkinter.Label(self.main_window,
                                   text='Amount')
    # Positioned towards the top-left corner
    self.label_amt.place(x=30, y=20)
    
    # Display a label for the monthly payment
    self.label_pmt = tkinter.Label(self.main_window,
                                   text='Monthly Payment:')
    # Positioned towards the bottom-left corner
    self.label_pmt.place(x=30, y=200)

  # ******************************************************************
  # Slide #08: Input Entry Widgets and Handling User Input
  # ******************************************************************
  def input_entry(self):
    # Input entry box for user to enter amount borrowed
    self.entry_amt = tkinter.Entry(self.main_window,
                                   width=12)
    self.entry_amt.place(x=100, y=20)
    self.entry_amt.focus()

  # ******************************************************************
  # Slide #09: Radiobutton Widgets within Frames
  # ******************************************************************
  def radio_buttons(self):
    # Display a label for terms
    self.label_term = tkinter.Label(self.main_window,
                                    text='Term')
    self.label_term.place(x=30, y=50)

    # Build a frame that will contain loan terms
    self.frame_term = tkinter.Frame(self.main_window)
    self.frame_term.config(bd=1, relief=tkinter.SOLID)
    self.frame_term.place(x=30, y=70)

    # Create the IntVar object to use with the radio buttons
    self.loan_term = tkinter.IntVar()

    # Set the IntVar object to 4 years
    self.loan_term.set(4)

    # Design 3 Radiobutton widgets for loan terms of 4, 5 or 6 years
    self.rb_4yrs = tkinter.Radiobutton(self.frame_term,
                                       text='4 years',
                                       variable=self.loan_term,
                                       value=4)
    self.rb_4yrs.pack()

    self.rb_5yrs = tkinter.Radiobutton(self.frame_term,
                                       text='5 years',
                                       variable=self.loan_term,
                                       value=5)
    self.rb_5yrs.pack()

    self.rb_6yrs = tkinter.Radiobutton(self.frame_term,
                                       text='6 years',
                                       variable=self.loan_term,
                                       value=6)
    self.rb_6yrs.pack()

  # ******************************************************************
  # Slide #10: Listbox of Interest Rates
  # ******************************************************************   
  def list_box(self):
    # Display a label for interest rates
    self.label_rates = tkinter.Label(self.main_window,
                                    text='Rates (%)')
    self.label_rates.place(x=120, y=50)

    # Create a Listbox of interest rates
    self.listbox_rates = tkinter.Listbox(self.main_window,
                                         selectmode=tkinter.SINGLE,
                                         height=7, width=7)
    self.listbox_rates.place(x=120, y=70)

    # Populate the Listbox with interest rates
    rate = 3.5
    for i in range(41):
      self.listbox_rates.insert(i, format(rate,'.1f'))
      rate += 0.1

    # Select 6-th item by default
    self.listbox_rates.select_set(5)


  # ******************************************************************
  # Slide #11: Creating Button Widgets and Using Info Dialog Boxes
  # ******************************************************************
  def command_buttons(self):
    # Command button for monthly payment calculation
    self.button_calc = tkinter.Button(self.main_window,
                                      text='Calculate',
                                      height=2, width=15,
                                      command=self.calc_mth_pmt)
    # Position Calculate button towards the top-right corner
    self.button_calc.place(x=200, y=20)

    # Quit button to close the application
    self.button_quit = tkinter.Button(self.main_window,
                                      text='Quit',
                                      height=2, width=15,
                                      command=self.main_window.destroy)
    # Position Quit button right below Calculate button
    self.button_quit.place(x=200, y=70)
    

  def calc_mth_pmt(self):
    # Gather all the inputs
    try:
      amt_txt = self.entry_amt.get()
      amount = float(amt_txt)
      term = self.loan_term.get()
      idx = self.listbox_rates.curselection()
      rate = float(self.listbox_rates.get(idx))

      # Calculate the monthly payment
      mth_pmt = (rate/1200)/(1-(1+rate/1200)**(-12*term))*amount

      # Display the result
      #tkinter.messagebox.showinfo('Payment',
                                  #f'Monthly Payment ${mth_pmt:,.2f}')
      self.mth_pmt.set(f'${mth_pmt:,.2f}')

    except ValueError:
      tkinter.messagebox.showinfo('ERROR!',
                                  'You must enter a valid amount!')

 
  # ******************************************************************
  # Slide #12: Using Labels as Output Fields
  # ******************************************************************
  def output_labels(self):
    # Create a StringVar object to associate with output label
    self.mth_pmt = tkinter.StringVar()

    # Create a label for monthly payment output
    self.label_pmt = tkinter.Label(self.main_window,
                                   textvariable=self.mth_pmt)
    self.label_pmt.place(x=140, y=200)
    # self.label_pmt.config(bd=1, relief=tkinter.SOLID)

# Create an instance of the MyGUI class.
if __name__ == '__main__':
  pmt_calc = PmtCalcGUI()
