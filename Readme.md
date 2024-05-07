# Project Name

## Description
This project is a harness tester for Raspberry Pi.

## Folder Organization:

HARNESS_TESTER_RASPBERRYPI/
│
├── Configuration/
│   └── config.py
│
├── Logic/
│   └── logic.py
│
├── Reports/
│   └── report.py
│
├── harness_tester.service
├── main.py
├── output.log     <-- for service outputs
├── error.log      <-- for service outputs
└── README.md



## Installation
1. Clone the repository.
2. Install required dependencies including Rpi.GPIO library and python 3.12.3 or latest
3. Run `main.py`.

## Usage
- Modify `config.py` to configure the harness tester.
- Run `main.py` to start the tester.

## Contributors
- Rajavelu Balasubramanian

## License
## Todo

## Future Implementations
- Usage of flags based on service running to select ground or gpio pin for the _GND based pins in connectors
- Report generation as a file with encryption
- Initiation of the main.py or the service itself only by selective user 


