# Project Documentation

## Overview
Khan-Rubix is an executable utility that allows users to encrypt a file of up to 12Mb using a key of up to 1Kbytes in length, and a corresponding decryption function that takes the encrypted file as input and, given the same key, produces the original file.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Modules](#modules)

## Installation

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/your-repository.git
    ```
2. Navigate to the project directory:
    ```bash
    cd path/to/the/project/root
    ```

## Usage
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

## Modules
### 234_project.ipynb

### byte_frequency_analysis.py
Analyzes the frequency of each byte in the input data and returns an array
    with the most frequent byte as the first element.

    Args:
        data: Bytes or bytearray object.

    Returns:
        A list of byte patterns, sorted by frequency (descending) and byte value (ascending) during tie-breakers.
        
### HuffmanEncoding.py

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

## bytecube.py

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
