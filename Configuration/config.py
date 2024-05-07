#   FILE NAME   :   config.py
#   AUTHOR      :   Rajavelu Balasubramanian
#   DATE        :   06-05-2024
#   REFERENCE   :   https://www.raspberrypi.com/documentation/computers/raspberry-pi.html
#   SCHEMATIC   :   https://datasheets.raspberrypi.com/rpi4/raspberry-pi-4-reduced-schematics.pdf?_gl=1*1kbzena*_ga*NDEwODA5NzQ0LjE3MTQ1MDE3NjM.*_ga_22FD70LWDS*MTcxNDkzMTU3My4yLjEuMTcxNDkzMTU5NS4wLjAuMA..

#   DESCRIPTION :
#           1. We use a key-value(Pin name - pin number) pair i.e dictionaries in python to represent
#              pin name and the corresponding GPIO/Pin number
#           2. To avoid usage of magic numbers GPIO module has been imported
#              Configuration settings based on PDF and the Reference hyperlink mentioned above
#           3. Followed BCM numbering, so changes in rpi version wouldn't affect, which means if 23 is used it is GPIO23
#              Note: 27 and 28 are reserved for I2C with EEPROM

# GPIO pin mappings for Connector 1
PIN_MAPPING_CONNECTOR_1 = {
    'Green_CAN_High': 2,
    'Blue_CAN_Low': 3,
    'Orange_LV_12V': 4,
    'Brown_LIGHT_OUT_GND': [9,17],   #  First index is ground pin and seond index is GPIO
    'Red_HV_42V': 10,
    'Black_GND': [25,11]             #  First index is ground pin and seond index is GPIO
}

# GPIO pin mappings for Connector 2
PIN_MAPPING_CONNECTOR_2 = {
    'Red_HV_42V': 5,
    'Black_GND': [39,6],         #  First index is ground pin and seond index is GPIO   
    'Blue_CAN_Low': 13,
    'Orange_LV_12V': 19,
    'Green_CAN_High': 26,  
    'Brown_LIGHT_OUT_GND': [6,18]  #  First index is ground pin and seond index is GPIO 
}

# GPIO pin mappings for Connector 3
PIN_MAPPING_CONNECTOR_3 = {
    'Orange_LV_12V': 23,
    'White_HV_42V': 24,         
    'Brown_LIGHT_OUT_GND': [14,25],  #  First index is ground pin and seond index is GPIO
    'Green_CAN_High': 8,
    'Black_GND': [20,7],             #  First index is ground pin and seond index is GPIO
    'Purple_CAN_Low': 12
}



