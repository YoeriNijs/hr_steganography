# HR Steganography
Hide messages in plain sight by manipulating gpx heart rates.

## Installation
Make sure you've Python 3.x installed.
```
# Clone this repository
git clone git@github.com:YoeriNijs/hr_steganography.git

# Install necessary packages
pip install -r requirements.txt
```

## Create gpx file with custom message
- Paste a valid gpx file inside the root of the project
- Run main.py and select the `w` option

## Read custom message from gpx file
- Run main.py and select the `r` option
- Make sure that you own a decryption key

## Test a gpx file on HR steganography
- Create a baseline by pasting valid gpx files for the same target device in the `__baseline__` dir
- Run main.py and select the `d` option

## How it works
Will be updated soon.