# import matplotlib.pyplot as plt
# import networkx as nx

# def optimalSearchTree(keys, freq):
#     n = len(keys)

#     # Cost and root matrices
#     cost = [[0 for _ in range(n)] for _ in range(n)]
#     root = [[0 for _ in range(n)] for _ in range(n)]

#     # Base case: one key
#     for i in range(n):
#         cost[i][i] = freq[i]
#         root[i][i] = i

#     # Fill for chains of length 2..n
#     for length in range(2, n + 1):
#         for i in range(n - length + 1):
#             j = i + length - 1
#             cost[i][j] = float("inf")

#             fsum = sum(freq[i:j + 1])

#             for r in range(i, j + 1):
#                 left = cost[i][r - 1] if r > i else 0
#                 right = cost[r + 1][j] if r < j else 0
#                 c = left + right + fsum

#                 if c < cost[i][j]:
#                     cost[i][j] = c
#                     root[i][j] = r

#     return cost, root


# # Build tree recursively
# def buildTree(root, keys, i, j):
#     if j < i:
#         return None
#     r = root[i][j]
#     return {
#         "key": keys[r],
#         "left": buildTree(root, keys, i, r - 1),
#         "right": buildTree(root, keys, r + 1, j)
#     }


# # Add edges to graph
# def add_edges(tree, G, parent=None):
#     if tree is None:
#         return
#     node = tree["key"]
#     G.add_node(node)
#     if parent:
#         G.add_edge(parent, node)
#     add_edges(tree["left"], G, node)
#     add_edges(tree["right"], G, node)


# # Recursive layout for binary tree
# def hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5, pos=None, parent=None):
#     if pos is None:
#         pos = {root: (xcenter, vert_loc)}
#     else:
#         pos[root] = (xcenter, vert_loc)

#     neighbors = list(G.neighbors(root))
#     if parent is not None and parent in neighbors:
#         neighbors.remove(parent)
#     if len(neighbors) != 0:
#         dx = width / 2
#         nextx = xcenter - width/2 - dx/2
#         for neighbor in neighbors:
#             nextx += dx
#             pos = hierarchy_pos(G, neighbor, width=dx, vert_gap=vert_gap,
#                                 vert_loc=vert_loc - vert_gap, xcenter=nextx,
#                                 pos=pos, parent=root)
#     return pos


# # Example usage
# #keys = ["sun", "shines", "warms", "moon", "glows", "guides", "stars", "shine", "stay"]
# #freq = [0.1667, 0.0833, 0.0833, 0.1667, 0.0833, 0.0833, 0.1667, 0.0833, 0.0833]



# def read_text():
#     with open(r'Advanced Algorithms(CSPC901)\Assignment 4\input.txt','r') as file:
#         input=file.read().lower()
#     input = input.strip() 
#     input = input.replace(",", "") 
#    # print("Input text:", input)
#     words=input.split()
#    # print("Words:", words)
#     dictionary = {}
#     for word in words:
#         freq=words.count(word)           
#         #print(f"Word:{word} Frequencies:{freq}")
#         dictionary[word]=freq
#         freq=0
#    # print("Frequencies dictionary:", dictionary)    
#     probability={}
#     sum_count=sum(dictionary.values())
#     print("Sum of frequencies:", sum_count)
#     for key in dictionary:
#         probability[key]=dictionary[key]/sum_count
#     #print("Probabilities dictionary:", probability)
#     return probability

# probability=read_text()
# print(probability)

# keys=list(probability.keys())
# prob=list(probability.values())
# cost, root = optimalSearchTree(keys, prob)
# tree = buildTree(root, keys, 0, len(keys) - 1)

# print("Optimal Cost:", cost[0][len(keys)-1])

# # Draw
# G = nx.DiGraph()
# add_edges(tree, G)

# pos = hierarchy_pos(G, tree["key"])
# plt.figure(figsize=(10,6))
# nx.draw(G, pos, with_labels=True, arrows=False,
#         node_size=2500, node_color="lightblue",
#         font_size=10, font_weight="bold")
# plt.title("Optimal Binary Search Tree (OBST)", fontsize=14)
# plt.show()







import matplotlib.pyplot as plt
import networkx as nx

def optimalSearchTree(keys, freq):
    n = len(keys)

    # Cost and root matrices
    cost = [[0 for _ in range(n)] for _ in range(n)]
    root = [[0 for _ in range(n)] for _ in range(n)]

    # Base case: one key
    for i in range(n):
        cost[i][i] = freq[i]
        root[i][i] = i

    # Fill for chains of length 2..n
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            cost[i][j] = float("inf")

            fsum = sum(freq[i:j + 1])

            for r in range(i, j + 1):
                left = cost[i][r - 1] if r > i else 0
                right = cost[r + 1][j] if r < j else 0
                c = left + right + fsum

                if c < cost[i][j]:
                    cost[i][j] = c
                    root[i][j] = r

    return cost, root


# Build tree recursively
def buildTree(root, keys, freqs, i, j):
    if j < i:
        return None
    r = root[i][j]
    return {
        "key": f"{keys[r]} ({freqs[r]:.3f})",  # include probability
        "left": buildTree(root, keys, freqs, i, r - 1),
        "right": buildTree(root, keys, freqs, r + 1, j)
    }


# Add edges to graph
def add_edges(tree, G, parent=None):
    if tree is None:
        return
    node = tree["key"]
    G.add_node(node)
    if parent:
        G.add_edge(parent, node)
    add_edges(tree["left"], G, node)
    add_edges(tree["right"], G, node)


# Recursive layout for binary tree
def hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5, pos=None, parent=None):
    if pos is None:
        pos = {root: (xcenter, vert_loc)}
    else:
        pos[root] = (xcenter, vert_loc)

    neighbors = list(G.neighbors(root))
    if parent is not None and parent in neighbors:
        neighbors.remove(parent)
    if len(neighbors) != 0:
        dx = width / 2
        nextx = xcenter - width/2 - dx/2
        for neighbor in neighbors:
            nextx += dx
            pos = hierarchy_pos(G, neighbor, width=dx, vert_gap=vert_gap,
                                vert_loc=vert_loc - vert_gap, xcenter=nextx,
                                pos=pos, parent=root)
    return pos



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



probability=read_text()

print(probability)

keys=list(probability.keys())
prob=list(probability.values())

# Example usage
#keys = ["sun", "shines", "warms", "moon", "glows", "guides", "stars", "shine", "stay"]
#freq = [0.1667, 0.0833, 0.0833, 0.1667, 0.0833, 0.0833, 0.1667, 0.0833, 0.0833]

cost, root = optimalSearchTree(keys, prob)
tree = buildTree(root, keys, prob, 0, len(keys) - 1)

print("Optimal Cost:", cost[0][len(keys)-1])

# Draw
G = nx.DiGraph()
add_edges(tree, G)

pos = hierarchy_pos(G, tree["key"])
plt.figure(figsize=(12,7))
nx.draw(G, pos, with_labels=True, arrows=False,
        node_size=250, node_color="lightblue",
        font_size=9, font_weight="bold")
plt.title("Optimal Binary Search Tree (OBST) with Probabilities", fontsize=14)
plt.show()
