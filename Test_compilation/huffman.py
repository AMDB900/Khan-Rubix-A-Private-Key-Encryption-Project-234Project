
import heapq
from collections import Counter

class HuffmanNode:
    def __init__(self, byte, freq):
        self.byte = byte
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq
    
def byte_frequency_analysis(data):
    if not isinstance(data, (bytes, bytearray)):
        raise TypeError("Input data must be bytes or bytearray")
    byte_counts = Counter(data)
    sorted_bytes = sorted(byte_counts.items(), key=lambda item: (-item[1], item[0]))
    return sorted_bytes
    
def build_huffman_tree(byte_frequencies):
    heap = [HuffmanNode(byte, freq) for byte, freq in byte_frequencies]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left, merged.right = left, right
        heapq.heappush(heap, merged)
    return heap[0]




def generate_huffman_codes(node, prefix=b"", huffman_codes=None):
    if huffman_codes is None:
        huffman_codes = {}
    if node is None:
        return
    if node.byte is not None:
        huffman_codes[node.byte] = prefix
    else:
        generate_huffman_codes(node.left, prefix + b"0", huffman_codes)
        generate_huffman_codes(node.right, prefix + b"1", huffman_codes)
    return huffman_codes

def huffman_encode(data):
    byte_frequencies = byte_frequency_analysis(data)
    root = build_huffman_tree(byte_frequencies)
    huffman_codes = generate_huffman_codes(root)
    encoded_data = "".join(huffman_codes[byte].decode() for byte in data)
    return encoded_data, root

def huffman_decode(data, tree):
    decoded_data = bytearray()
    node = tree
    for bit in data:
        if bit == '0':
            node = node.left
        else:
            node = node.right
        if node.byte is not None:
            decoded_data.append(node.byte)
            node = tree
    return decoded_data

