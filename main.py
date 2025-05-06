from xor import *
from HuffmanEncoding import *
from bytecube import *

def get_key():
    """
    Prompts the user to select a file from the 'test_key' directory.

    Lists all available files, lets the user choose one, and the address of the selected file.

    Returns:
        The address of the selected file.
    """
    # List all files in the current directory
    files = [f for f in os.listdir("test_key") if os.path.isfile(os.path.join("test_key", f))]
    content = []
    if not files:
        print("No files found in the directory.")
        exit()
    else:
        for i, file in enumerate(files):
            print(f"{i + 1}: {file}")

        while True:
            try:
                choice = int(input("Enter the number of the file: ")) - 1
                if 0 <= choice < len(files):
                    break
                else:
                    print("Invalid choice, please enter a valid number.")
            except ValueError:
                print("Please enter a number.")

        filename = files[choice]

    return os.path.join("test_key", filename)

# Primary encryption execution
if __name__ == "__main__":

    pi_digits = read_pi_digits('pi_10000_digits.txt')

    ## Getting and padding the file and key
    print("Select a file to encrypt:")
    content, filename = get_file()
    data = pad_file(content, filename)
    print("\nSelect a key file:")
    key = load_and_pad_key_from_file(get_key(), pi_digits)

    print("Padded size:", len(data))
    print()

    ## START OF ENCRYPTION

    # XOR the key against the file in 1KB chunks
    print("XOR... ", end="")

    start_time = time.perf_counter()
    encrypted = xor(data, key)
    end_time = time.perf_counter()

    fxor_time = end_time - start_time  # Time the XOR
    print(f"           finished in {fxor_time:7.4f} seconds")

    # Perform Huffman encoding of resulting array
    print("Huffman encode... ", end="")

    start_time = time.perf_counter()
    encoded_data, tree = huffman_encode(encrypted)
    end_time = time.perf_counter()

    huffman_time = end_time - start_time  # Time the huffman encoding
    print(f"finished in {huffman_time:7.4f} seconds")

    # Binary string to bytes
    encoded_bytes = hex(int('1' + encoded_data, 2))[2:].encode()

    #############################################
    ##         RUBIK's SHUFFLE ALGORITHM       ##
    ##                GOES HERE                ##
    ## encoded_bytes = shuffle(encoded_bytes)  ##
    #############################################

    print("Cube shuffle...   ", end="")
    start_time = time.perf_counter()
    cube_size = 256
    bcube = ByteCube(cube_size)
    bcube.setBytes(encoded_bytes)
    for x in range(cube_size):
        for y in range(cube_size):
            bcube.shiftXY(x, y, key[(x + y * cube_size) % len(key)])

    for x in range(cube_size):
        for z in range(cube_size):
            bcube.shiftXZ(x, z, key[(x + z * cube_size + cube_size * cube_size) % len(key)])

    for y in range(cube_size):
        for z in range(cube_size):
            bcube.shiftYZ(y, z, key[(y + z * cube_size + cube_size * cube_size * 2) % len(key)])

    shuffled_bytes = bcube.getBytes()
    end_time = time.perf_counter()
    shuffle_time = end_time - start_time
    print(f"finished in {shuffle_time:7.4f} seconds")

    ## END OF ENCRYPTION

    encryption_time = huffman_time + fxor_time + shuffle_time  # Time the encryption process
    print(f"Total encryption time ------- {encryption_time:7.4f} seconds")

    print("Encrypted size:", len(shuffled_bytes))

    print("\nBYTE FREQUENCY ANALYSIS\n-----------------------\n", byte_frequency_analysis(encoded_bytes))

    # Output of encryption: .khn filetype
    with open("text.khn", "wb") as file:
        file.write(shuffled_bytes)

    ## START OF DECRYPTION

    ##############################################
    ## encoded_bytes = unshuffle(encoded_bytes) ##
    ##############################################

    print("\nCube unshuffle... ", end="")
    start_time = time.perf_counter()
    cube_size = 256
    bcube = ByteCube(cube_size)
    bcube.setBytes(shuffled_bytes)

    for y in range(cube_size):
        for z in range(cube_size):
            bcube.shiftYZ(y, z, -1 * (key[(y + z * cube_size + cube_size * cube_size * 2) % len(key)]))

    for x in range(cube_size):
        for z in range(cube_size):
            bcube.shiftXZ(x, z, -1 * (key[(x + z * cube_size + cube_size * cube_size) % len(key)]))

    for x in range(cube_size):
        for y in range(cube_size):
            bcube.shiftXY(x, y, -1 * (key[(x + y * cube_size) % len(key)]))

    unshuffled_bytes = bcube.getBytes()
    end_time = time.perf_counter()
    unshuffle_time = end_time - start_time
    print(f"finished in {unshuffle_time:7.4f} seconds")

    # Byte object to binary string
    decoded_bytes = bin(int(unshuffled_bytes.decode(), 16))[3:]

    # Perform Huffman decoding
    print("Huffman decode... ", end="")

    start_time = time.perf_counter()
    decoded_data = huffman_decode(decoded_bytes, tree)
    end_time = time.perf_counter()

    decode_time = end_time - start_time  # Time the huffman decoding
    print(f"finished in {decode_time:7.4f} seconds")

    # XOR the decoded data against the file
    print("Reverse XOR... ", end="")

    start_time = time.perf_counter()
    decrypted = xor(decoded_data, key)
    end_time = time.perf_counter()

    rxor_time = end_time - start_time  # Time the reverse XOR
    print(f"   finished in {rxor_time:7.4f} seconds")

    decryption_time = rxor_time + decode_time + unshuffle_time  # Time the decryption process
    print(f"Total decryption time ------- {decryption_time:7.4f} seconds")

    ## END OF DECRYPTION

    # print("\nDecrypted:", decrypted)
    print("Decrypted size:", len(decrypted))

    print("")
    if encoded_bytes == unshuffled_bytes:
        print("Success: Encoded Data = Unshuffled Data")
    if encrypted == decoded_data:
        print("Success: Decoded  Data = XOR'd Data")
    if decrypted == data:
        print("Success: Original Data = Decrypted Data")

    print("\nExtracting file size and suffix / Removing padding...", end='')

    # Remove padding, extract suffix, and output file
    start_time = time.perf_counter()
    og = return_original_file(decrypted)
    end_time = time.perf_counter()

    extract_time = end_time - start_time  # Time the extraction
    print(f" {extract_time:.4f} seconds")
    print("Extracted size:", len(og))
