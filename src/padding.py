"""
References:
https://www.geeksforgeeks.org/python-strings-encode-method/
https://www.geeksforgeeks.org/hashlib-module-in-python/
"""

import secrets
import time
import hashlib
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
def read_pi_digits(file_path):
    """
    Opens a file containing the digits of pi and reads its contents, removing non integer digits.

    Returns:
        A string containing the digits of pi without decimal points or whitespaces.
    """
    file_path = resource_path(file_path)
    with open(file_path, 'r') as f:
        pi_digits = f.read()  # Read all digits as a string
    return pi_digits.replace(".", "").strip()  # Remove the decimal point and any whitespace

def hash_key(key):
    """
    Hashes the provided key using SHA-256 and returns the hash as an integer.

    Args:
        key (str or bytes): The key to be hashed.

    Returns:
        An integer representing the hash of the key.
    """
    # Use SHA-256 hash function to generate a digest of the key
    key_bytes = key.encode('utf-8') if isinstance(key, str) else key
    hash_digest = hashlib.sha256(key_bytes).hexdigest()  # Get the hex digest
    return int(hash_digest, 16)  # Convert hex digest to an integer

def pad_key_with_pi(key, pi_digits, target_length=1024):
    """
    Pads the provided key with digits from pi to ensure it reaches the target length.

    Args:
        key (str or bytes): The key to be padded.
        pi_digits (str): A string containing the digits of pi.
        target_length (int): The desired length of the padded key. Default is 1024.
    
    Returns:
        key (bytes): The padded key as bytes.
    """
    # Ensure the key is in bytes
    if isinstance(key, str):
        key = key.encode('utf-8')

    # Calculate the starting index from the hash of the key
    start_index = hash_key(key) % len(pi_digits)

    # Pad the key with digits from pi, wrapping around if necessary
    padding_needed = target_length - len(key)
    if padding_needed > 0:
        # Create a list to hold the padding
        padding = []
        
        # Start adding digits from pi starting at the calculated index
        current_index = start_index
        for _ in range(padding_needed):
            padding.append(pi_digits[current_index])  # Add the current digit to the padding list
            current_index = (current_index + 1) % len(pi_digits)  # Move to the next index, wrapping around if needed

        # Convert the list of digits into a string, then encode as bytes
        padding_string = ''.join(padding)
        padding_bytes = padding_string.encode('utf-8')

        # Append the padding to the key
        key += padding_bytes

    elif padding_needed < 0:
        key = key[:target_length]  # Truncate the key if it's too long

    return key

def load_and_pad_key_from_file(file_path, pi_digits, target_length=1024):
    """
    Loads a key from a file and pads it with digits from pi to ensure it reaches the target length.

    Args:
        file_path (str): The path to the file containing the key.
        pi_digits (str): A string containing the digits of pi.
        target_length (int): The desired length of the padded key. Default is 1024.
    
    Returns:
        key (bytes): The padded key as bytes from pad_key_with_pi.
    """
    with open(file_path, 'rb') as f:
        key = f.read()  # Read the key from the file as bytes
    
    return pad_key_with_pi(key, pi_digits, target_length)

def pad_file(file_content, input_file_path, seed=12345):
    """
    Pads the contents of a file to ensure it reaches a size of 16MB.

    Args:
        file_content (bytes): The content of the file to be padded.
        input_file_path (str): The path to the input file.
        seed (int): Seed for random number generation. Default is 12345.
        
    Returns:
        A bytearray containing the padded file content.
    """
    # Read the content of the input file

    if len(file_content) > (12 * 1024 * 1024): # 12 MB
        print(f"Error: File size is {len(file_content)}B. File must be less than {12 * 1024 * 1024}B in size.")
        exit()
    
    print(f"Padding {input_file_path} ...", end='')
    start = time.perf_counter()
    
    # Extract the length of the string (4 bytes)
    content_length = len(file_content)
    
    # Get the file suffix (file extension)
    file_suffix = os.path.splitext(input_file_path)[1].encode('utf-8')  # Ensure it's a byte string
    print(file_suffix)
    while len(file_suffix) < 5: # Pad the extension to 5 bytes (covers .docx)
        file_suffix = file_suffix + b'0'
        
    # Append the 4-byte length of the content and file suffix
    linear_array = bytearray(content_length.to_bytes(4, byteorder='little') + file_suffix + file_content)
    
    # Calculate how much padding is needed to reach 16MB
    total_size = 16 * 1024 * 1024  # 16 MB
    current_size = len(linear_array)
    
    # Pad to 16MB with random bytes
    padding_needed = total_size - current_size
    linear_array += secrets.token_bytes(padding_needed)
    
    # Ensure the final array size is exactly 16MB
    if len(linear_array) != total_size:
        print("Error: File size != 16MB")
        exit()
    
    end = time.perf_counter()
    print(f" {end - start:.4f} seconds")

    return bytes(linear_array)

def return_original_file(content, file_name):
    """
    Extracts the original file from the padded content.

    Args:
        content (bytes): The padded content containing the original file data.

    Returns:
        data (bytes): The original file data extracted from the padded content.
    """
    # Extract the length of the string (4 bytes)
    content_length = content[0:4]
    length = int.from_bytes(content_length, byteorder='little')
    
    # Get the file suffix (file extension)
    file_suffix = content[4:9]
    suffix = file_suffix.split(b'0')[0]

    # Gather file data based on length of the string
    data = content[9:9 + length]

    text = file_name + suffix.decode('utf-8', errors="ignore")
    
    return data, text

# For testing purposes
if __name__ == "__main__":
    
    # pad_key_with_pi example usage:
    pi_digits = read_pi_digits('pi_10000_digits.txt')  # Load the pi digits from a file
    key = "mmmmmmmmmmmmmmmmmy secret key"  # Example key
    padded_key = pad_key_with_pi(key, pi_digits)
    print(padded_key.hex())
    print(len(padded_key))  # This should print 1024 if the padding is correct
    
    # load_and_pad_key_from_file example usage:
    file_key = load_and_pad_key_from_file('Screenshot 2025-02-20 160715.png', pi_digits)
    print(file_key.hex())
    print(len(file_key))  # Should print 1024 if the padding is correct

    """
    # Example usage for 
    input_file_path = 'test_input/1.docx'  # Replace with your file path
    linear_array = pad_file(input_file_path)

    # Output file should be 16MB with the data as described

    print(f"Linear array created with size: {len(linear_array)} bytes")
    print(return_original_file(linear_array))"
    """
