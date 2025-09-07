import re


with open("English.txt") as f:
    content=f.read()

with open("dict.txt","r",encoding="utf-8") as fl:
    dictt=fl.read()

    #-------------checks if the string is a word-------------

def isword(str)->bool: 
    if re.fullmatch(r"\s+", str): #checks only space
        return False
    elif re.fullmatch(r"[^\w\s]+", str):  # checks only punctuation
        return False
    elif re.fullmatch(r"[A-Za-z]+", str):
        return True
    else:
        return False

#-----------------finds the frequency of a word in the input text file---------------
freq={}
def find_frequency(word): 
    
    if word not in freq:
        freq[word]=1
    else:
        freq[word]+=1
    return freq
    # print(freq)

#-----------finds the probability of a worde in the text file-----------------
def find_probability(frequency,tlength): 

    probability=frequency/tlength
    return probability
#----------------create tree---------------
class Node:
    def __init__(self, word, translation, probability):
        self.word = word
        self.translation = translation
        self.probability = probability
        self.left = None
        self.right = None

class MaxBinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, root, node):
        if root is None:
            return node
        if node.probability > root.probability:
            node.left = root
            return node
        else:
            root.right = self.insert(root.right, node)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(f"{root.word} ({root.translation}) -> {root.probability:.4f}")
            self.inorder(root.right)


#-------------------------------
prob={}
inp=[]
dict_original=[]
dict_original=dictt.split(";")

helpdict={}
for w in dict_original:
    f=[]
    f=w.split(":")
    helpdict[f[0]]=f[1]

inp=content.split()
inp=[item.lower() for item in inp]
count=0
for word in inp:
    res=isword(word)
    if res:
        count+=1
        frq=find_frequency(word)

for word in frq:
    prob[word]=find_probability(frq[word],count)



# ---------build_max_binary_tree--------
tree = MaxBinaryTree()

for word,translation in helpdict.items():
    if word.strip() in frq:
       
        p=prob[word.strip()]
        node = Node(word, translation, p)
        tree.root = tree.insert(tree.root, node)
    else:
        p=0
        node = Node(word, translation, p)
        tree.root = tree.insert(tree.root, node)


print("Inorder traversal of Max Binary Tree:")
tree.inorder(tree.root)


 #---------------calculating the cost to search a word---------------

def find_node_and_depth(root, target, depth=1):
    if root is None:
        return None
    if root.word == target:
        return root, depth
    left = find_node_and_depth(root.left, target, depth + 1)
    if left:
        return left
    return find_node_and_depth(root.right, target, depth + 1)

# ---- compute expected search cost ----
def expected_search_cost(tree_root, input_file):
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read().lower()

    words = re.findall(r"[a-z]+", text)   # extract words only
    total_cost = 0.0

    for w in words:
        w=" "+w+" "
        found = find_node_and_depth(tree_root, w, depth=1)
        if found:   # word exists in tree
            node, depth = found
            total_cost += node.probability * depth
        # if word not found in tree → skip it

    return total_cost




cost = expected_search_cost(tree.root, "English.txt")
print(f"Expected Search Cost: {cost:.4f}")

