import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency

def build_huffman_tree(data):
    frequency_dict = defaultdict(int)
    for char in data:
        frequency_dict[char] += 1

    priority_queue = [Node(char, freq) for char, freq in frequency_dict.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left_child = heapq.heappop(priority_queue)
        right_child = heapq.heappop(priority_queue)

        internal_node = Node(None, left_child.frequency + right_child.frequency)
        internal_node.left = left_child
        internal_node.right = right_child

        heapq.heappush(priority_queue, internal_node)

    return priority_queue[0]

def generate_huffman_codes(root, current_code="", codes=None):
    if codes is None:
        codes = {}

    if root is not None:
        if root.char is not None:
            codes[root.char] = current_code
        generate_huffman_codes(root.left, current_code + "0", codes)
        generate_huffman_codes(root.right, current_code + "1", codes)

    return codes

def huffman_encode(data):
    root = build_huffman_tree(data)
    codes = generate_huffman_codes(root)

    encoded_data = "".join(codes[char] for char in data)
    return encoded_data, codes

def huffman_decode(encoded_data, codes):
    reverse_codes = {code: char for char, code in codes.items()}
    current_code = ""
    decoded_data = ""

    for bit in encoded_data:
        current_code += bit
        if current_code in reverse_codes:
            decoded_data += reverse_codes[current_code]
            current_code = ""

    return decoded_data

if __name__ == "__main__":
    data = "kunal nawale"

    encoded_data, codes = huffman_encode(data)
    print("Original data:", data)
    print("Encoded data:", encoded_data)
    decoded_data = huffman_decode(encoded_data, codes)
    print("Decoded data:", decoded_data)
