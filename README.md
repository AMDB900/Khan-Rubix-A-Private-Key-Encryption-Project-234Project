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
- [Executable Installation](#executable-installation)
- [Project Usage](#project-usage)
- [Modules](#modules)
- [Byte Frequency Analysis](#bytes)

## Instructions for Non-Technical Users <a name="nontech"></a>
The application has a gui built for user convience with widgets that indicate each function performed by the program \
There are 5 widgets that are shown by the program: \
- Select a File: Allows the user to select a file that will be encrypted or decrypted.
- Select a Key: Allows the user to select a file to act as a key to perform the encryption or decryption functions.
- Custom Key:
- Encrypt:
- Decrypt:
## Executable Installation <a name="executable-installation"></a>
The windows executable is provided as Khan-Rubix Encryptor.exe. \
Download that file or the project as zip.
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

## Modules <a name="modules"></a>
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

### Randomization.py
Tools to generate random keys, patterns for shuffling, and huffman-encoded data.

### xor.py
```
def xor(text, key) -> bytes

    Args:
        text: Bytes or bytearray. Textual input that you want to encrypt
        key: Bytes or bytearray. The length of the key must be exactly 1KB.
```

### bytecube.py
Main file for bytecube implementation. Includes tools for bytecube manipulation.

## List of Files
### main.py
Main executable.
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
### Screenshot 2025-02-20 160715
### xor.py
### HuffmanEncoding.py
### bytecube.py
### test_file_randomization.ipynb
### padding.py
### byte_frequency_analysis.py
### Randomization.py
### README.md
