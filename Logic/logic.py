#   FILE NAME   :   logic.py
#   AUTHOR      :   Rajavelu Balasubramanian
#   DATE        :   06-05-2024

#   DESCRIPTION :
#           This file contains the core logic implementation for the harness tester application. 
#           It includes functions to initialize GPIO pins, perform logic checks on label consistency
#           across connectors, and send the status to the `report.py` module.
#           
#          The script dynamically adds the `Configuration` and `Reports` directories to the Python path 
#          to import the `config.py` and `report.py` modules. It also checks the platform to determine whether 
#          it's running on a Raspberry Pi and imports the `RPi.GPIO` module accordingly. 
# 
#          If `RPi.GPIO` is not available (e.g., running on a different platform), 
#           it uses a mock implementation provided by the `unittest.mock` module.

#   TODOs       :
#  - Implement mocking of GPIO functionality for non-Raspberry Pi platforms.
#  - Enhance error handling and logging within the logic functions particularly with same label not available and GND pins
import sys
import os

#Gets the directory path of config.py
Configuration_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Configuration'))
#Gets the directory path of report.py
Reports_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Reports'))


#Add Configuration folder to python path, after this config.py could be imported
sys.path.insert(0, Configuration_dir)
#Add Configuration folder to python path, after this config.py could be imported
sys.path.insert(0, Reports_dir)

import config
import report
# Import RPi.GPIO only if the script is running on a Raspberry Pi
import platform
if platform.machine().startswith('arm') or platform.machine().startswith('aarch64'):
    import RPi.GPIO as GPIO
else:
    # Mocking RPi.GPIO if it's not available
    try:
        import RPi.GPIO as GPIO
    except ImportError:
        from unittest.mock import MagicMock
        GPIO = MagicMock() 



#TODO: Mock the gpios
# Function to initialize GPIO pins
def initialize_gpio():
    GPIO.setmode(GPIO.BCM)
    for connector_pins in [config.PIN_MAPPING_CONNECTOR_1, config.PIN_MAPPING_CONNECTOR_2, config.PIN_MAPPING_CONNECTOR_3]:
        for label, pin in connector_pins.items():
            # Skip ground pins
            if "GND" in label:
                continue
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.HIGH)

# Function to perform logic
def perform_logic():
    initialize_gpio()
    consistent = True  # Assume consistency until proven otherwise
    for label, pin in config.PIN_MAPPING_CONNECTOR_1.items():
        # Skip ground pins
        if "GND" in label:
            continue
        found_in_other_connectors = False
        # Check if the label-pin pair is present in other connectors
        for connector_pins in [config.PIN_MAPPING_CONNECTOR_2, config.PIN_MAPPING_CONNECTOR_3]:
            if label in connector_pins:
                found_in_other_connectors = True
                # If the corresponding pin in the other connector is not high, set consistent to False
                if GPIO.input(connector_pins[label]) != GPIO.HIGH:
                    consistent = False
                    break
        # If the label is not found in other connectors, log a message
        if not found_in_other_connectors:
            print(f"Warning: Label '{label}' not found in other connectors.")
    # Send the status to report.py
    report.send_status(consistent)

# Call the perform_logic() function to execute the logic
# perform_logic()   #   use it to test from this module, called from main already





