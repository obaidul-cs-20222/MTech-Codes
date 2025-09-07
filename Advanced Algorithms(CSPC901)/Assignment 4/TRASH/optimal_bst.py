def read_text():
    with open(r'Advanced Algorithms(CSPC901)\Assignment 4\input.txt','r') as file:
        input=file.read().lower()
    input = input.strip() 
    input = input.replace(",", "") 
   # print("Input text:", input)
    words=input.split()
   # print("Words:", words)
    dictionary = {}
    for word in words:
        freq=words.count(word)           
        #print(f"Word:{word} Frequencies:{freq}")
        dictionary[word]=freq
        freq=0
   # print("Frequencies dictionary:", dictionary)    
    probability={}
    sum_count=sum(dictionary.values())
    print("Sum of frequencies:", sum_count)
    for key in dictionary:
        probability[key]=dictionary[key]/sum_count
    #print("Probabilities dictionary:", probability)
    return probability


def add(freq, i, j):
    s = 0
    for k in range(i, j + 1):
        s += freq[k]
    return s

def optCost(freq, i, j):
  
   
    if j < i:
        return 0

   
    if j == i:
        return freq[i]

 
    fsum = add(freq, i, j)

   
    min_val = float('inf')

    
    for r in range(i, j + 1):
        cost = optCost(freq, i, r - 1) + optCost(freq, r + 1, j)
        min_val = min(min_val, cost)

   
    return min_val + fsum

def optimalSearchTree(keys, freq):

    n = len(keys)
    return optCost(freq, 0, n - 1)







# AVL TREE


class AVLNode:
    def __init__(self, key, freq):
        self.key = key
        self.freq = freq
        self.left = None
        self.right = None
        self.height = 1

def getHeight(node):
    return node.height if node else 0

def getBalance(node):
    return getHeight(node.left) - getHeight(node.right) if node else 0

def rightRotate(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))
    x.height = 1 + max(getHeight(x.left), getHeight(x.right))
    return x

def leftRotate(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    x.height = 1 + max(getHeight(x.left), getHeight(x.right))
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))
    return y

def insert(root, key, freq):
    if not root:
        return AVLNode(key, freq)
    if key < root.key:
        root.left = insert(root.left, key, freq)
    else:
        root.right = insert(root.right, key, freq)

    root.height = 1 + max(getHeight(root.left), getHeight(root.right))
    balance = getBalance(root)

    # Balancing cases
    if balance > 1 and key < root.left.key:
        return rightRotate(root)
    if balance < -1 and key > root.right.key:
        return leftRotate(root)
    if balance > 1 and key > root.left.key:
        root.left = leftRotate(root.left)
        return rightRotate(root)
    if balance < -1 and key < root.right.key:
        root.right = rightRotate(root.right)
        return leftRotate(root)

    return root

def buildAVL(keys, freq):
    # Sort keys by decreasing frequency
    items = sorted(zip(keys, freq), key=lambda x: -x[1])
    root = None
    for key, f in items:
        root = insert(root, key, f)
    return root


def expectedCost(node, depth=1):
    if not node:
        return 0
    return (node.freq * depth + expectedCost(node.left, depth + 1) + expectedCost(node.right, depth + 1))





















if __name__ == "__main__":
    probability=read_text()
    print(probability)

    keys=list(probability.keys())
    prob=list(probability.values())
    print("Keys:", keys)
    print("Probabilities:", prob)
    
    answer=optimalSearchTree(keys, prob)    
    print("Optimal Search Tree Cost:", answer)

    avl_root = buildAVL(keys, prob)
    print("AVL Tree constructed.")

    # Step 4: Expected Search Cost in AVL Tree
    avl_cost = expectedCost(avl_root)
    print("Expected Search Cost in AVL Tree:", avl_cost)



#Sun shines, sun warms, moon glows, moon guides, stars shine, stars stay