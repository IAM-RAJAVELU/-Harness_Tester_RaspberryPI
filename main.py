#   FILE NAME   :   main.py
#   AUTHOR      :   Rajavelu Balasubramanian
#   DATE        :   06-05-2024

#   DESCRIPTION :
#       This file serves as the entry point for the harness tester application. 
#
#       It imports the logic module (`logic.py`) from the Logic directory and executes
#       the main logic to check label consistency. 
#
#       The `perform_logic()` function is called within the `main()` function, 
#       which is executed when the script is run as the main program.

import sys
import os

#Gets the directory path of logic.py
Logic_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Logic'))

#Add Configuration folder to python path, after this config.py could be imported
sys.path.insert(0, Logic_dir)

from Logic.logic import *

# Main function
def main():
    # Perform logic to check label consistency
    perform_logic()

if __name__ == "__main__":
    main()

