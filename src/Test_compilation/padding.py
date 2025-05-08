import secrets
import time
import os
import hashlib
import sys

def read_pi_digits(file_path):
    with open(file_path, 'r') as f:
        pi_digits = f.read()
    return pi_digits.replace(".", "").strip()

def hash_key(key):
    key_bytes = key.encode('utf-8') if isinstance(key, str) else key
    return int(hashlib.sha256(key_bytes).hexdigest(), 16)

def pad_key_with_pi(key, pi_digits, target_length=1024):
    if isinstance(key, str):
        key = key.encode('utf-8')
    start_index = hash_key(key) % len(pi_digits)
    padding_needed = target_length - len(key)
    if padding_needed > 0:
        padding = [pi_digits[(start_index + i) % len(pi_digits)] for i in range(padding_needed)]
        key += ''.join(padding).encode('utf-8')
    elif padding_needed < 0:
        key = key[:target_length]
    return key

def load_and_pad_key_from_file(file_path, pi_digits, target_length=1024):
    with open(file_path, 'rb') as f:
        key = f.read()
    return pad_key_with_pi(key, pi_digits, target_length)

def pad_file(file_content, input_file_path, seed=12345):
    if len(file_content) > (12 * 1024 * 1024):
        print(f"Error: File size is {len(file_content)}B. Must be <12MB.")
        exit()

    start = time.perf_counter()
    content_length = len(file_content)
    file_suffix = os.path.splitext(input_file_path)[1].encode('utf-8')
    while len(file_suffix) < 5:
        file_suffix += b'0'

    linear_array = bytearray(content_length.to_bytes(4, 'little') + file_suffix + file_content)
    padding_needed = (16 * 1024 * 1024) - len(linear_array)
    linear_array += secrets.token_bytes(padding_needed)

    if len(linear_array) != 16 * 1024 * 1024:
        print("Error: Final file size != 16MB.")
        sys.exit()


    end = time.perf_counter()
    print(f"Padding complete in {end - start:.4f} seconds")

    return bytes(linear_array)

def return_original_file(content):
    content_length = int.from_bytes(content[:4], 'little')
    suffix = content[4:9].rstrip(b'0')  # safer
    data = content[9:9 + content_length]
    file_name = "decrypted" + suffix.decode('utf-8', errors="ignore")
    return data, file_name
