import heapq

def read_char():
    with open(r'input.txt','r') as file:
        input=file.read()
    input = input.strip()  
    print("Input text:", input)
    freq={}
    for char in input:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    print("Character frequencies:", freq)

    return freq,input


class Node:
    def __init__(self, symbol=None, frequency=None):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency

    def __repr__(self):
        return f"Node(symbol={self.symbol}, frequency={self.frequency})"


def huffman_tree(char,freq):
    priority_queue = [Node(char, f) for char, f in zip(char, freq)]
    #print("Initial priority queue:", priority_queue[0])
    heapq.heapify(priority_queue)
    
    while len(priority_queue) > 1:
        left=heapq.heappop(priority_queue)
        right=heapq.heappop(priority_queue)
        new_node=Node(frequency=left.frequency+right.frequency)
        new_node.left=left
        new_node.right=right
        heapq.heappush(priority_queue, new_node)

    return priority_queue[0]

def generate_huffman_codes(node,code="",huffman_codes={}):
    
    if node is not None:
        if node.symbol is not None:
            huffman_codes[node.symbol] = code
        generate_huffman_codes(node.left, code + "0", huffman_codes)
        generate_huffman_codes(node.right, code + "1", huffman_codes)

    return huffman_codes



def decoding(root,s):
    n=len(s)
    ans=""
    current_node=root
    for i in range(n):
        if s[i]=="0":
            current_node = current_node.left
        elif s[i]=="1":
            current_node = current_node.right
        if current_node.left==None and current_node.right==None:
            ans+=current_node.symbol
            current_node=root

    return ans



if __name__ == "__main__":
    freq,input=read_char()
    s=""
    char=list(freq.keys())
    freq=list(freq.values())
    #print("Characters:", char)
    #print("Frequencies:", freq)
    root=huffman_tree(char, freq)
    huffman_codes = generate_huffman_codes(root)
    print("Huffman Codes:")
    for char, code in huffman_codes.items():
        print(f"Character: {char}, Code: {code}")  
         
    for char in input:
        s =s+ huffman_codes[char]
    print("Encoded string:", s)
    with open('encoded.txt', 'w') as file:
         file.write(s)
    decoded_string = decoding(root, s)
    print("Decoded string:", decoded_string)
    with open('decoded.txt', 'w') as file:
         file.write(decoded_string)

    if decoded_string == input:
        print("Huffman Encoding Decoding Successfull")