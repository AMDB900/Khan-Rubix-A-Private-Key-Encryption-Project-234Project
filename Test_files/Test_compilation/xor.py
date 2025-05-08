import sys


def xor(text, key):
    """
    Applies XOR encryption to the given text using the provided key.

    Args:
        text (bytes): The content to be encrypted or decrypted.
        key (bytes): The key used for XOR operation.

    Returns:
        bytes: The XORed result.
    """
    if len(text) != (16 * 1024 * 1024):
        print(f"Error: File size is {len(text)}B. File must be {16 * 1024 * 1024}B.")
        sys.exit()

    offset = 1024
    if len(key) != offset:
        print(f"Error: Key size is {len(key)}B. Key must be {offset}B.")
        sys.exit()

    return bytes(text[i] ^ key[i % offset] for i in range(len(text)))
