import re

# ------------ Frequency + Probability ------------
def isword(s: str) -> bool:
    if re.fullmatch(r"\s+", s):
        return False
    elif re.fullmatch(r"[^\w\s]+", s):  # punctuation only
        return False
    elif re.fullmatch(r"[A-Za-z]+", s):
        return True
    else:
        return False

freq = {}
def find_frequency(word):
    if word not in freq:
        freq[word] = 1
    else:
        freq[word] += 1
    return freq

def find_probability(frequency, tlength):
    return frequency / tlength

# ------------ AVL Tree Node + Class ------------
class AVLNode:
    def __init__(self, word, translation, probability):
        self.word = word
        self.translation = translation
        self.probability = probability
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        # rotation
        x.right = y
        y.left = T2

        # update heights
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        # rotation
        y.left = x
        x.right = T2

        # update heights
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def insert(self, root, node):
        if not root:
            return node
        # normal BST insert by word (alphabetical)
        if node.word < root.word:
            root.left = self.insert(root.left, node)
        elif node.word > root.word:
            root.right = self.insert(root.right, node)
        else:
            return root  # duplicate not allowed

        # update height
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # balance factor
        balance = self.get_balance(root)

        # 4 cases
        if balance > 1 and node.word < root.left.word:
            return self.right_rotate(root)
        if balance < -1 and node.word > root.right.word:
            return self.left_rotate(root)
        if balance > 1 and node.word > root.left.word:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and node.word < root.right.word:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

# ------------ Search Cost ------------
def find_node_and_depth(root, target, depth=1):
    if root is None:
        return None
    if root.word == target:
        return root, depth
    elif target < root.word:
        return find_node_and_depth(root.left, target, depth + 1)
    else:
        return find_node_and_depth(root.right, target, depth + 1)

def expected_search_cost(tree_root, input_file):
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read().lower()
    words = re.findall(r"[a-z]+", text)

    total_cost = 0.0
    for w in words:
        found = find_node_and_depth(tree_root, w, depth=1)
        if found:
            node, depth = found
            total_cost += node.probability * depth
    return total_cost

# ------------ MAIN PROGRAM ------------
with open("English.txt") as f:
    content = f.read()

with open("dict.txt", "r", encoding="utf-8") as fl:
    dictt = fl.read()

# build dictionary
helpdict = {}
for w in dictt.split(";"):
    if ":" in w:
        k, v = w.split(":")
        helpdict[k.strip()] = v.strip()

# count frequencies
inp = content.split()
inp = [item.lower() for item in inp]
count = 0
for word in inp:
    if isword(word):
        count += 1
        frq = find_frequency(word)

# probabilities
prob = {word: find_probability(frq[word], count) for word in frq}

# build AVL tree
tree = AVLTree()
root = None
for word, translation in helpdict.items():
    p = prob[word] if word in prob else 0
    node = AVLNode(word, translation, p)
    root = tree.insert(root, node)

# compute cost
cost = expected_search_cost(root, "English.txt")
print(f"Expected Search Cost (AVL Tree): {cost:.4f}")
