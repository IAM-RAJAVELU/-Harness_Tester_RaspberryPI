#   FILE NAME   :   report.py
#   AUTHOR      :   Rajavelu Balasubramanian
#   DATE        :   06-05-2024

#   DESCRIPTION :
#           This file contains the functionality to generate a report based on the consistency
#           of labels in the harness tester application. 
#           
#           It includes the `send_status()` function, which receives a boolean value 
#           indicating the consistency of labels and prints a message accordingly. 
# 
#           The script also includes logic to interact with the GPIO pins, 
#           specifically to control an LED indicator based on the consistency status. 
#
#           If running on a Raspberry Pi, it imports the RPi.GPIO module and initializes GPIO pins accordingly. If RPi.GPIO is not available (e.g., running on a different platform), it uses a mock implementation provided by the `unittest.mock` module.

#  TODOs       :
#   - Implement mocking of GPIO functionality for non-Raspberry Pi platforms.
#   - Explore options for generating reports with encryption for enhanced security.

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

# Define the GPIO pin for the LED
LED_PIN = 16

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

def send_status(consistent):
    if consistent:
        print("All labels are consistent.")
        # TODO: Log the result to a file, trigger LED indicator, etc.
        # Turn on the LED
        GPIO.output(LED_PIN, GPIO.HIGH)
    else:
        print("Labels are inconsistent.")
        # TODO: Log the result to a file, trigger LED indicator, etc.
        # Turn off the LED
        GPIO.output(LED_PIN, GPIO.LOW)
