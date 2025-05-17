# Project Documentation
## Members
- Ethan Baker (ethanbaker@csus.edu)
- Andrei Bayani (adbayani@csus.edu)
- Alex Oswalt (aoswalt@csus.edu)
- Patrick Purta (ppurta@csus.edu)
- Kevin Shiroya (kshiroya@csus.edu)
## Overview
Khan-Rubix is an executable utility that allows users to encrypt a file of up to 12Mb using a key of up to 1Kbytes in length, and a corresponding decryption function that takes the encrypted file as input and, given the same key, produces the original file.

## Table of Contents
- [Instructions for Non-Technical Users](#nontech)
- [Additional Instructions for Moderately Technical Users](#modtech)
- [Further Instructions for Highly Technical Users](#hightech)
- [Executable Installation](#executable-installation)
- [Project Usage](#project-usage)
- [Modules](#modules)
- [Byte Frequency Analysis](#bytes)

## Instructions for Non-Technical Users <a name="nontech"></a>
The application has a gui built for user convience with widgets that indicate each function performed by the program. \
There are 5 widgets that are shown by the program:
- Select a File: Allows the user to select a file from their machine that will be encrypted or decrypted.
- Select a Key: Allows the user to select a file from thier machineto act as a key to perform the encryption or decryption functions. Mutually exclusive with Custom Key.
- Custom Key: Prompts the user to type in an input to act as a key for either function. Mutually exclusive with Select a Key.
- Encrypt: After selecting a file and providing a key through either key widget, select this to perform an encryption. This will prompt the user to select a location on their PC and file name to save the file as a .khn encrypted file.
- Decrypt: The user must have selected a .khn file as a file, and provided the correct key for this to function. Selecting this widget will prompt the user to provide a name for the decrypted file. The file will be generated in the same folder as the executable.

### Steps for Encrypting a File
1. Run the executable.
2. Click the 'Select a File' widget and select the file you want to encrypt from your file explorer.
3. Click either the 'Select a Key' or 'Custom Key' widget.
4. If selecting 'Select a Key,' navigate the file explorer to find the key you want to use.
5. If selecting 'Custom Key,' type the key you want into the prompt that will pop up.
6. Click the 'Encrypt' widget. Navigate to where you want to store your file and provide a file name then press enter.

### Steps for Decrypting a File
1. Run the executable.
2. Click the 'Select a File' widget and select the file you want to decrypt from your file explorer. Ensure that this is a .khn file
3. Click either the 'Select a Key' or 'Custom Key' widget.
4. If selecting 'Select a Key,' navigate the file explorer to find the key you want to use.
5. If selecting 'Custom Key,' type the key you want into the prompt that will pop up.
6. Click the 'Decrypt' widget. The program will prompt you to provide a name to the decrypted file.
7. The decrypted file will be found in the same directory as the executable.
## Additional Instructions for Moderately Technical Users <a name="modtech"></a>
The program comes with zero dependencies as all come pre-compiled with the executable. \
Refer to [Executable Installation](#executable-installation) for downloading the executable. \
Refer to [Project Usage](#project-usage) for installing the source code to your machine. \
All source code is located in the /src folder while all test files are located in Test_files.
## Further Instructions for Highly Technical Users to Customize the Program.<a name="hightech"></a>
For compilation of source code, do the following:
- Install Pyinstaller:
```
pip install pyinstaller
```
- For windows, Do the following commands from root of project:
```
cd src
```
```
pyinstaller --onefile --noconsole --add-data "pi_10000_digits.txt;." app_gui.py
```
- If you would like to edit the pi constant, change the contents of "pi_10000_digits.txt" 

The program only uses base python libraries so no installations other than python need to be performed. \
The instructions provided currently only work on Windows and was tested on Windows 10/11.
## Executable Installation <a name="executable-installation"></a>
The windows executable is provided as Khan-Rubix Encryptor.exe. \
Download that file or the project as zip. \
The executable only works on Windows and was tested using Windows 10/11. For Mac, please refer to [Project Usage](#project-usage)
## Project Usage <a name="project-usage"></a>

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/your-repository.git
    ```
2. Navigate to the project directory:
    ```bash
    cd path/to/the/project/root
    ```
### Running the Project
Run from cmd or Powershell. For instance:

Windows
```bash
cd path/to/the/project/root
python main.py
```

MacOS
```bash
cd path/to/the/project/root
python3 main.py
```

## Modules Used <a name="modules"></a>
### main.py
Main use for terminal execution. Performs encryption and decryption. \
original file -> key padding -> xor -> huffman encoding -> fibonacci coding -> byte shifting -> encrypted file \
encrypted file -> key padding -> byte shifting -> fibonacci decode -> huffman decode -> xor -> decrypted file \
For a custom key, make a txt file with the string you want to use as a custom key.
### app_gui.py
Contains gui in the Khan-Rubix Encryptor.exe \
Includes custom key function that uses entered string as a key.
### byte_frequency_analysis.py
Analyzes the frequency of each byte in the input data and returns an array
    with the most frequent byte as the first element.

    Args:
        data: Bytes or bytearray object.

    Returns:
        A list of byte patterns, sorted by frequency (descending) and byte value (ascending) during tie-breakers.
        
### HuffmanEncoding.py
Tools for Huffman Encoding.

### padding.py
Tools for padding keys and input files. Keys will be padded to 1KB using a hash function 
of the key to select where to start adding garbage data from pi digits. Padding will
wrap around to the start of the pi digits. Files will be padded to 12MB with information
about the length of the file, the filetype, and with random bytes from the original string.


### xor.py
```
def xor(text, key) -> bytes

    Args:
        text: Bytes or bytearray. Textual input that you want to encrypt
        key: Bytes or bytearray. The length of the key must be exactly 1KB.
```

### bytecube.py
Main file for bytecube implementation. Includes tools for bytecube manipulation.

### FibonacciCoding.py
File containing fibonacci coding for data padding.

## List of Files

### main.py
Main file for terminal executable
### app_gui.py
Executable gui file.
### test_input
Folder with testing files.
* 1.docx - Word Document file. Includes text, tables, charts and images.
* 2 - Random Numbers
* 3 - All Zeros
* 4 - All Ones
* 5 - "01010101010..."
* 6.png - Testing image
### testing
Folder for xor key integration and speed comparison.
* xor_key_integration.py
* xor_speed_compare.py
### test_key
Folder with testing keys. They are the same as the test_input files.
### pi_10000_digits.txt
Text file with the first ten-thousand digits of pi.
### xor.py
### HuffmanEncoding.py
### bytecube.py
### test_file_randomization.ipynb
### padding.py
### byte_frequency_analysis.py
### Randomization.py
### FibonacciEncoding.py
### README.md
