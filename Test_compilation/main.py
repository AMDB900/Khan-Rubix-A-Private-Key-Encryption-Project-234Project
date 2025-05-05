import os
import time
import pickle
import math
import sys
from tkinter import Tk, filedialog
from padding import read_pi_digits, pad_file, load_and_pad_key_from_file, return_original_file
from xor import xor
from huffman import huffman_encode, huffman_decode
from bytecube import ByteCube

def choose_file(prompt_message, folder="."):
    """Open a file chooser dialog, return the selected filepath."""
    print(f"\n{prompt_message}")
    root = Tk()
    root.withdraw()
    path = filedialog.askopenfilename(initialdir=folder, title=prompt_message)
    if not path:
        print("No file selected. Exiting.")
        sys.exit()
    print(f"Selected: {path}")
    return path

def encrypt_file(input_path, key_path, output_path):
    start = time.perf_counter()
    pi = read_pi_digits('pi_10000_digits.txt')

    # read & pad
    with open(input_path,'rb') as f: content = f.read()
    print(f"Original size: {len(content)} bytes")
    data = pad_file(content, input_path)
    print(f"Padded size : {len(data)} bytes")

    # XOR
    key = load_and_pad_key_from_file(key_path, pi)
    print("\nXOR Encryption...")
    t0 = time.perf_counter()
    xored = xor(data, key)
    print(f"  done in {time.perf_counter()-t0:.4f}s")

    # Huffman
    print("Huffman Encoding...")
    t0 = time.perf_counter()
    bits, tree = huffman_encode(xored)
    print(f"  done in {time.perf_counter()-t0:.4f}s")

    # serialize tree
    tree_data = pickle.dumps(tree)
    tree_len  = len(tree_data)

    # bits → int → hex → raw bytes
    bits = '1'+bits
    i    = int(bits,2)
    hx   = hex(i)[2:]
    if len(hx)%2: hx = '0'+hx
    raw  = bytes.fromhex(hx)
    print(f"After hex→bytes: {len(raw)} bytes")

    # 3D shuffle
    print("\n3D ByteCube Shuffle...")
    cube_size = 266
    print(f"Cube size: {cube_size}")
    bc = ByteCube(cube_size)
    bc.setBytes(raw)
    for x in range(cube_size):
        for y in range(cube_size):
            bc.shiftXY(x,y, key[(x+y*cube_size)%len(key)])
    for x in range(cube_size):
        for z in range(cube_size):
            bc.shiftXZ(x,z, key[(x+z*cube_size+cube_size**2)%len(key)])
    for y in range(cube_size):
        for z in range(cube_size):
            bc.shiftYZ(y,z, key[(y+z*cube_size+2*cube_size**2)%len(key)])
    shuf = bc.getBytes()

    # write out
    final = tree_len.to_bytes(4,'big') + tree_data + shuf
    with open(output_path,'wb') as f:
        f.write(final)

    total = time.perf_counter()-start
    print(f"\nEncrypted size: {len(final)} bytes")
    print(f"✅ Encryption done in {total:.4f}s → {output_path}")

def decrypt_file(encrypted_path, key_path):
    start = time.perf_counter()
    pi = read_pi_digits('pi_10000_digits.txt')

    with open(encrypted_path,'rb') as f: full = f.read()
    print(f"\nEncrypted size: {len(full)} bytes")

    # extract tree
    tlen = int.from_bytes(full[:4],'big')
    tdat = full[4:4+tlen]
    tree = pickle.loads(tdat)
    shuf = full[4+tlen:]

    # load key
    key = load_and_pad_key_from_file(key_path, pi)

    # unshuffle
    print("\nCube Unshuffle...")
    cube_size = 266
    print(f"Cube size: {cube_size}")
    bc = ByteCube(cube_size)
    bc.setBytes(shuf)
    for y in range(cube_size):
        for z in range(cube_size):
            bc.shiftYZ(y,z, -key[(y+z*cube_size+2*cube_size**2)%len(key)])
    for x in range(cube_size):
        for z in range(cube_size):
            bc.shiftXZ(x,z, -key[(x+z*cube_size+cube_size**2)%len(key)])
    for x in range(cube_size):
        for y in range(cube_size):
            bc.shiftXY(x,y, -key[(x+y*cube_size)%len(key)])
    raw = bc.getBytes()

    # hex→int→bits
    print("Huffman Decoding...")
    i = int.from_bytes(raw, byteorder='big')
    bits = bin(i)[3:]

    # decode
    data = huffman_decode(bits, tree)[:16*1024*1024]

    # XOR back
    print("\nReverse XOR...")
    plain = xor(data, key)

    # extract original
    print("\nSaving decrypted file...")
    file_data, fname = return_original_file(plain)
    with open(fname,'wb') as f:
        f.write(file_data)

    total = time.perf_counter()-start
    print(f"Decrypted size: {len(file_data)} bytes")
    print(f"✅ Decryption done in {total:.4f}s → {fname}")

def main():
    print("\n" + "="*50)
    print("  Private-Key Encryption / Decryption Utility")
    print("="*50)

    choice = input("1) Encrypt   2) Decrypt   → ").strip()
    if choice=="1":
        inp = choose_file("Select file to ENCRYPT:")
        key = choose_file("Select KEY file:")
        out = input("Save encrypted as (no ext): ").strip() + ".khn"
        encrypt_file(inp, key, out)
    elif choice=="2":
        inp = choose_file("Select ENCRYPTED file:")
        key = choose_file("Select KEY file:")
        decrypt_file(inp, key)
    else:
        print("Invalid option.")

if __name__=="__main__":
    main()
