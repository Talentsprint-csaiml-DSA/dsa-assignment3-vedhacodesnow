import heapq
from collections import defaultdict, Counter

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Compare nodes based on frequency (for heapq)
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(freq_map):
    # Create a priority queue (min-heap)
    heap = [HuffmanNode(char, freq) for char, freq in freq_map.items()]
    heapq.heapify(heap)
    
    # Build the Huffman Tree
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        
        merged = HuffmanNode(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        
        heapq.heappush(heap, merged)
    
    return heap[0]  # The root of the tree

def generate_huffman_codes(root):
    codes = {}
    
    def generate_code(node, current_code):
        if not node:
            return
        if node.char is not None:
            codes[node.char] = current_code
        generate_code(node.left, current_code + "0")
        generate_code(node.right, current_code + "1")
    
    generate_code(root, "")
    return codes

def huffman_coding(input_string):
    # Step 1: Count the frequency of characters
    freq_map = Counter(input_string)
    
    # Step 2: Build the Huffman Tree
    root = build_huffman_tree(freq_map)
    
    # Step 3: Generate Huffman Codes
    huffman_codes = generate_huffman_codes(root)
    
    # Step 4: Encode the input string
    encoded_string = ''.join(huffman_codes[char] for char in input_string)
    
    return encoded_string
