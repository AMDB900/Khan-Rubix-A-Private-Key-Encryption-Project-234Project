import os
import time
import pickle
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from padding import read_pi_digits, pad_file, load_and_pad_key_from_file, return_original_file
from xor import xor
from HuffmanEncoding import huffman_encode, huffman_decode
from bytecube import ByteCube
from FibonacciCoding import *

class KhanApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Private-Key Encryption / Decryption Utility")
        self.root.geometry("700x500")
        self.root.resizable(False, False)

        self.pi_digits = read_pi_digits('pi_10000_digits.txt')

        self.input_file = ""
        self.key_file = ""
        self.output_file = ""

        self.using_custom_key = False
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        self.build_ui()

    def build_ui(self):
        frame = tk.Frame(self.root, padx=10, pady=10)
        frame.pack(fill=tk.BOTH, expand=True)

        # File selectors
        tk.Button(frame, text="Select File", command=self.select_input).pack(pady=5)
        tk.Button(frame, text="Select Key", command=self.select_key).pack(pady=5)
        tk.Button(frame, text="Custom Key", command=self.custom_key).pack(pady=5)
        # Encrypt/Decrypt buttons
        btn_frame = tk.Frame(frame)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Encrypt", width=15, command=self.encrypt_ui).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Decrypt", width=15, command=self.decrypt_ui).pack(side=tk.RIGHT, padx=10)

        # Log console
        tk.Label(frame, text="Status / Log:").pack(anchor="w")
        self.log_console = scrolledtext.ScrolledText(frame, height=18, state='disabled')
        self.log_console.pack(fill=tk.BOTH, expand=True)

    def log(self, message):
        self.log_console.config(state='normal')
        self.log_console.insert(tk.END, message + '\n')
        self.log_console.see(tk.END)
        self.log_console.config(state='disabled')
        self.root.update()

    def select_input(self):
        self.input_file = filedialog.askopenfilename(
            title="Select file to encrypt/decrypt",
            initialdir="F:/csus/sem 2/234/project/test_input"
        )
        if self.input_file:
            self.log(f"Selected file: {self.input_file}")

    def select_key(self):
        self.key_file = filedialog.askopenfilename(
            title="Select private key",
            initialdir="F:/csus/sem 2/234/project/test_key"
        )
        if self.key_file:
            self.log(f"Selected key: {self.key_file}")
    def custom_key(self):
        def save_custom_key():
            key_text = entry.get()
            if not key_text:
                messagebox.showwarning("Invalid Key", "Please enter a non-empty key.")
                return
            try:
                temp_key_path = "custom_key.key"
                with open(temp_key_path, 'w') as f:
                    f.write(key_text)
                self.key_file = temp_key_path
                self.using_custom_key = True
                self.log(f"Custom key provided and temporarily saved to {temp_key_path}")
                popup.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save custom key: {e}")

        popup = tk.Toplevel(self.root)
        popup.title("Enter Custom Key")
        popup.geometry("300x120")
        popup.resizable(False, False)

        tk.Label(popup, text="Enter your key:").pack(pady=5)
        entry = tk.Entry(popup, width=40, show="*")  # `show="*"` hides input like a password
        entry.pack(pady=5)
        tk.Button(popup, text="Submit", command=save_custom_key).pack(pady=5)
    def encrypt_ui(self):
        if not self.input_file or not self.key_file:
            messagebox.showerror("Missing Input", "Please select both a file and a key.")
            return

        save_path = filedialog.asksaveasfilename(
            defaultextension=".khn",
            filetypes=[("Encrypted Files", "*.khn")],
            title="Save Encrypted File As"
        )
        if not save_path:
            self.log("❌ Encryption cancelled: No save location provided.")
            return

        self.output_file = save_path
        self.encrypt_file()

    def decrypt_ui(self):
        if not self.input_file or not self.key_file:
            messagebox.showerror("Missing Input", "Please select both a file and a key.")
            return
        self.decrypt_file()

    def encrypt_file(self):
        try:
            start = time.perf_counter()
            self.log("🔐 Starting encryption...")

            with open(self.input_file, 'rb') as f:
                content = f.read()

            self.log(f"Original size: {len(content)} bytes")
            data = pad_file(content, self.input_file)
            self.log(f"Padded size: {len(data)} bytes")

            key = load_and_pad_key_from_file(self.key_file, self.pi_digits)

            # XOR the key against the file in 1KB chunks
            start_time = time.perf_counter()
            xored = xor(data, key)
            end_time = time.perf_counter()
            fxor_time = end_time - start_time  # Time the XOR
            self.log(f"           finished in {fxor_time:7.4f} seconds")
            self.log("✅ XOR encryption done.")


            # Perform Huffman encoding of resulting array
            self.log("Huffman encode... ")
            start_time = time.perf_counter()
            bits, tree = huffman_encode(xored)
            end_time = time.perf_counter()
            tree_data = pickle.dumps(tree)
            tree_len = len(tree_data)

            huffman_time = end_time - start_time  # Time the huffman encoding
            self.log(f"finished in {huffman_time:7.4f} seconds")

            padded_data = fibonacciEncodeLength(bits)
            while(len(padded_data)%8!=0):
                padded_data = padded_data + "1"


            # Binary string to bytes
            encoded_bytes = bytearray(int(padded_data, 2).to_bytes((len(padded_data) + 7) // 8, 'big'))
            #encoded_bytes = hex(int('1' + encoded_data, 2))[2:].encode()

            #############################################
            ##         RUBIK's SHUFFLE ALGORITHM       ##
            ##                GOES HERE                ##
            ## encoded_bytes = shuffle(encoded_bytes)  ##
            #############################################

            self.log("Cube shuffle...   ")
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
            self.log(f"finished in {shuffle_time:7.4f} seconds")

            encryption_time = huffman_time + fxor_time + shuffle_time  # Time the encryption process
            self.log(f"Total encryption time ------- {encryption_time:7.4f} seconds")

            self.log(f"Encrypted size:{len(shuffled_bytes)}")

            # self.log("\nBYTE FREQUENCY ANALYSIS\n-----------------------\n", byte_frequency_analysis(encoded_bytes))
            final = tree_len.to_bytes(4, 'big') + tree_data + shuffled_bytes
            with open(self.output_file, 'wb') as f:
                f.write(final)

            elapsed = time.perf_counter() - start
            self.log(f"✅ File encrypted successfully → {self.output_file}")
            self.log(f"🕒 Time taken: {elapsed:.2f} seconds")
        except Exception as e:
            self.log(f"❌ Encryption error: {e}")

    def decrypt_file(self):
        # try:
        start = time.perf_counter()
        self.log("🔓 Starting decryption...")

        with open(self.input_file, 'rb') as f:
            full = f.read()

        tlen = int.from_bytes(full[:4], 'big')
        tdat = full[4:4 + tlen]
        tree = pickle.loads(tdat)
        shuf = full[4 + tlen:]

        key = load_and_pad_key_from_file(self.key_file, self.pi_digits)

        self.log("\nCube unshuffle... ")
        start_time = time.perf_counter()
        cube_size = 256
        bcube = ByteCube(cube_size)
        bcube.setBytes(shuf)

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
        self.log(f"finished in {unshuffle_time:7.4f} seconds")

        decoded_bytes = ''.join(format(byte, '08b') for byte in unshuffled_bytes)
        #decoded_bytes = bin(int(unshuffled_bytes.decode(), 16))[3:]

        decoded_bytes = fibonacciUnpad(decoded_bytes)

        # Perform Huffman decoding
        self.log("Huffman decode... ")

        start_time = time.perf_counter()
        decoded_data = huffman_decode(decoded_bytes, tree)
        end_time = time.perf_counter()

        decode_time = end_time - start_time  # Time the huffman decoding
        self.log(f"finished in {decode_time:7.4f} seconds")

        self.log("Reverse XOR... ")

        start_time = time.perf_counter()
        decrypted = xor(decoded_data, key)
        end_time = time.perf_counter()

        rxor_time = end_time - start_time  # Time the reverse XOR
        self.log(f"   finished in {rxor_time:7.4f} seconds")

        decryption_time = rxor_time + decode_time + unshuffle_time  # Time the decryption process
        self.log(f"Total decryption time ------- {decryption_time:7.4f} seconds")

        file_data, fname = return_original_file(decrypted)
        with open(fname, 'wb') as f:
            f.write(file_data)

        elapsed = time.perf_counter() - start
        self.log(f"✅ File decrypted → {fname}")
        self.log(f"🕒 Time taken: {elapsed:.2f} seconds")
        # except Exception as e:
        #     self.log(f"❌ Decryption error: {e}")

    def on_close(self):
        if self.using_custom_key and os.path.exists("custom_key.key"):
            try:
                os.remove("custom_key.key")
                self.log("🗑️ Deleted custom_key.key on exit.")
            except Exception as e:
                self.log(f"⚠️ Could not delete custom_key.key: {e}")
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = KhanApp(root)
    root.mainloop()
