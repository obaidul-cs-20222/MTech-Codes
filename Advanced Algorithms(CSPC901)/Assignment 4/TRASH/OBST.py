# import re
# from collections import Counter

# # --------------------------
# # 1. Load Dictionary (dict.txt)
# # --------------------------
# def load_dict(filename="dict.txt"):
#     dictionary = {}
#     with open(filename, "r", encoding="utf-8") as f:
#         for line in f:
#             parts = line.strip().split()
#             if len(parts) >= 2:
#                 eng, beng = parts[0], " ".join(parts[1:])
#                 dictionary[eng.lower()] = beng
#     return dictionary


# # --------------------------
# # 2. Tokenize input.txt
# # --------------------------
# def tokenize(filename="input.txt"):
#     with open(filename, "r", encoding="utf-8") as f:
#         text = f.read().lower()
#     return re.findall(r"[a-z']+", text)


# # --------------------------
# # 3. Compute probabilities
# # --------------------------
# def compute_probabilities(tokens):
#     freq = Counter(tokens)
#     total = sum(freq.values())
#     probs = {word: freq[word] / total for word in freq}
#     return probs, freq, total


# # --------------------------
# # 4. OBST using Dynamic Programming
# # --------------------------
# def optimal_bst(keys, p):
#     n = len(keys)
#     e = [[0] * (n + 2) for _ in range(n + 2)]
#     w = [[0] * (n + 2) for _ in range(n + 2)]
#     root = [[0] * (n + 2) for _ in range(n + 2)]

#     for i in range(1, n + 2):
#         e[i][i - 1] = 0
#         w[i][i - 1] = 0

#     for l in range(1, n + 1):  # interval length
#         for i in range(1, n - l + 2):
#             j = i + l - 1
#             e[i][j] = float("inf")
#             w[i][j] = w[i][j - 1] + p[j - 1]
#             for r in range(i, j + 1):
#                 t = e[i][r - 1] + e[r + 1][j] + w[i][j]
#                 if t < e[i][j]:
#                     e[i][j] = t
#                     root[i][j] = r
#     return e, root


# def build_tree(root, keys, i, j):
#     if i > j:
#         return None
#     r = root[i][j]
#     return {
#         "key": keys[r - 1],
#         "left": build_tree(root, keys, i, r - 1),
#         "right": build_tree(root, keys, r + 1, j),
#     }


# def print_tree(node, indent=""):
#     if not node:
#         return
#     print(indent + node["key"])
#     print_tree(node["left"], indent + "  ")
#     print_tree(node["right"], indent + "  ")


# # --------------------------
# # MAIN PIPELINE
# # --------------------------
# if __name__ == "__main__":
#     # 1. Load dictionary (500 entries in dict.txt)
#     dictionary = load_dict("english_bengali_500_words.txt")

#     # 2. Tokenize input file
#     tokens = tokenize("input.txt")

#     # 3. Compute probabilities
#     probs, freq, total = compute_probabilities(tokens)

#     # Use only words that appear in input.txt (Option A)
#     keys = sorted(probs.keys())
#     p = [probs[k] for k in keys]

#     print("\n--- Word Probabilities ---")
#     for k in keys:
#         print(f"{k}: {probs[k]:.3f}")

#     # 4. OBST construction
#     e, root = optimal_bst(keys, p)
#     obst_cost = e[1][len(keys)]
#     obst_tree = build_tree(root, keys, 1, len(keys))

#     # 5. Print result
#     print(f"\nExpected Search Cost (OBST) = {obst_cost:.3f}")
#     print("\nOptimal Binary Search Tree Structure:")
#     print_tree(obst_tree)






































# import re
# from collections import Counter
# import networkx as nx
# import matplotlib.pyplot as plt


# # --------------------------
# # 1. Load Dictionary (dict.txt)
# # --------------------------
# def load_dict(filename="dict.txt"):
#     dictionary = {}
#     try:
#         with open(filename, "r", encoding="utf-8") as f:
#             for line in f:
#                 parts = line.strip().split()
#                 if len(parts) >= 2:
#                     eng, beng = parts[0], " ".join(parts[1:])
#                     dictionary[eng.lower()] = beng
#     except FileNotFoundError:
#         print("⚠️ dict.txt not found, continuing without dictionary.")
#     return dictionary


# # --------------------------
# # 2. Tokenize input.txt
# # --------------------------
# def tokenize(filename="input.txt"):
#     with open(filename, "r", encoding="utf-8") as f:
#         text = f.read().lower()
#     return re.findall(r"[a-z']+", text)


# # --------------------------
# # 3. Compute probabilities
# # --------------------------
# def compute_probabilities(tokens):
#     freq = Counter(tokens)
#     total = sum(freq.values())
#     probs = {word: freq[word] / total for word in freq}
#     return probs, freq, total


# # --------------------------
# # 4. OBST (Dynamic Programming)
# # --------------------------
# def optimal_bst(keys, p):
#     n = len(keys)
#     e = [[0] * (n + 2) for _ in range(n + 2)]
#     w = [[0] * (n + 2) for _ in range(n + 2)]
#     root = [[0] * (n + 2) for _ in range(n + 2)]

#     for i in range(1, n + 2):
#         e[i][i - 1] = 0
#         w[i][i - 1] = 0

#     for l in range(1, n + 1):  # interval length
#         for i in range(1, n - l + 2):
#             j = i + l - 1
#             e[i][j] = float("inf")
#             w[i][j] = w[i][j - 1] + p[j - 1]
#             for r in range(i, j + 1):
#                 t = e[i][r - 1] + e[r + 1][j] + w[i][j]
#                 if t < e[i][j]:
#                     e[i][j] = t
#                     root[i][j] = r
#     return e, root


# def build_tree(root, keys, i, j):
#     if i > j:
#         return None
#     r = root[i][j]
#     return {
#         "key": keys[r - 1],
#         "left": build_tree(root, keys, i, r - 1),
#         "right": build_tree(root, keys, r + 1, j),
#     }


# # --------------------------
# # 5. Visualization (Pure Matplotlib)
# # --------------------------
# def add_edges(G, node, parent=None):
#     if not node:
#         return
#     G.add_node(node["key"])
#     if parent:
#         G.add_edge(parent, node["key"])
#     add_edges(G, node["left"], node["key"])
#     add_edges(G, node["right"], node["key"])


# def hierarchy_pos(G, root=None, width=1.0, vert_gap=0.2, vert_loc=0, xcenter=0.5):
#     """
#     Recursively assign positions to nodes for tree layout.
#     Works without pygraphviz.
#     """
#     if root is None:
#         root = list(G.nodes)[0]

#     def _hierarchy_pos(G, root, left, right, vert_loc, pos=None, parent=None):
#         if pos is None:
#             pos = {}
#         pos[root] = ((left + right) / 2, vert_loc)
#         neighbors = list(G.neighbors(root))
#         if neighbors:
#             dx = (right - left) / len(neighbors)
#             nextx = left
#             for neighbor in neighbors:
#                 pos = _hierarchy_pos(G, neighbor, nextx, nextx + dx, vert_loc - vert_gap, pos, root)
#                 nextx += dx
#         return pos

#     return _hierarchy_pos(G, root, 0, width, vert_loc)


# def visualize_tree(tree):
#     G = nx.DiGraph()
#     add_edges(G, tree)

#     pos = hierarchy_pos(G, tree["key"])
#     plt.figure(figsize=(8, 6))
#     nx.draw(G, pos, with_labels=True, arrows=False,
#             node_size=2000, node_color="lightblue",
#             font_size=10, font_weight="bold")
#     plt.title("Optimal Binary Search Tree")
#     plt.show()


# # --------------------------
# # MAIN PIPELINE
# # --------------------------
# if __name__ == "__main__":
#     # 1. Load dictionary (dict.txt)
#     dictionary = load_dict("english_bengali_500_words.txt")

#     # 2. Tokenize input file
#     tokens = tokenize("input.txt")

#     # 3. Compute probabilities
#     probs, freq, total = compute_probabilities(tokens)

#     # Use only words that appear in input.txt (Option A)
#     keys = sorted(probs.keys())
#     p = [probs[k] for k in keys]

#     print("\n--- Word Probabilities ---")
#     for k in keys:
#         print(f"{k}: {probs[k]:.3f}")

#     # 4. OBST construction
#     e, root = optimal_bst(keys, p)
#     obst_cost = e[1][len(keys)]
#     obst_tree = build_tree(root, keys, 1, len(keys))

#     # 5. Print result
#     print(f"\nExpected Search Cost (OBST) = {obst_cost:.3f}")

#     # 6. Visualize
#     if obst_tree:
#         visualize_tree(obst_tree)







































import re
from collections import Counter
import networkx as nx
import matplotlib.pyplot as plt


# --------------------------
# 1. Load Dictionary (dict.txt)
# --------------------------
def load_dict(filename="dict.txt"):
    dictionary = {}
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) >= 2:
                    eng, beng = parts[0], " ".join(parts[1:])
                    dictionary[eng.lower()] = beng
    except FileNotFoundError:
        print("dict.txt not found, continuing without dictionary.")
    return dictionary


# --------------------------
# 2. Tokenize input.txt
# --------------------------
def tokenize(filename="input.txt"):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read().lower()
    return re.findall(r"[a-z']+", text)


# --------------------------
# 3. Compute probabilities
# --------------------------
def compute_probabilities(tokens):
    freq = Counter(tokens)
    total = sum(freq.values())
    probs = {word: freq[word] / total for word in freq}
    return probs, freq, total


# --------------------------
# 4. OBST (Dynamic Programming)
# --------------------------
def optimal_bst(keys, p):
    n = len(keys)
    e = [[0] * (n + 2) for _ in range(n + 2)]
    w = [[0] * (n + 2) for _ in range(n + 2)]
    root = [[0] * (n + 2) for _ in range(n + 2)]

    for i in range(1, n + 2):
        e[i][i - 1] = 0
        w[i][i - 1] = 0

    for l in range(1, n + 1):  # interval length
        for i in range(1, n - l + 2):
            j = i + l - 1
            e[i][j] = float("inf")
            w[i][j] = w[i][j - 1] + p[j - 1]
            for r in range(i, j + 1):
                t = e[i][r - 1] + e[r + 1][j] + w[i][j]
                if t < e[i][j]:
                    e[i][j] = t
                    root[i][j] = r
    return e, root


def build_tree(root, keys, i, j):
    if i > j:
        return None
    r = root[i][j]
    return {
        "key": keys[r - 1],
        "left": build_tree(root, keys, i, r - 1),
        "right": build_tree(root, keys, r + 1, j),
    }


# --------------------------
# 5. AVL Expected Search Cost
# --------------------------
def build_balanced_bst(keys):
    """Recursively build a perfectly balanced BST from sorted keys."""
    if not keys:
        return None
    mid = len(keys) // 2
    return {
        "key": keys[mid],
        "left": build_balanced_bst(keys[:mid]),
        "right": build_balanced_bst(keys[mid + 1:]),
    }


def compute_expected_cost(tree, probs, depth=1):
    """Compute expected search cost = sum(p[i] * depth)."""
    if not tree:
        return 0
    return (
        probs[tree["key"]] * depth
        + compute_expected_cost(tree["left"], probs, depth + 1)
        + compute_expected_cost(tree["right"], probs, depth + 1)
    )


# --------------------------
# 6. Visualization (Optional for OBST)
# --------------------------
def add_edges(G, node, parent=None):
    if not node:
        return
    G.add_node(node["key"])
    if parent:
        G.add_edge(parent, node["key"])
    add_edges(G, node["left"], node["key"])
    add_edges(G, node["right"], node["key"])


def hierarchy_pos(G, root=None, width=1.0, vert_gap=0.2, vert_loc=0):
    if root is None:
        root = list(G.nodes)[0]

    def _hierarchy_pos(G, root, left, right, vert_loc, pos=None):
        if pos is None:
            pos = {}
        pos[root] = ((left + right) / 2, vert_loc)
        neighbors = list(G.neighbors(root))
        if neighbors:
            dx = (right - left) / len(neighbors)
            nextx = left
            for neighbor in neighbors:
                pos = _hierarchy_pos(G, neighbor, nextx, nextx + dx, vert_loc - vert_gap, pos)
                nextx += dx
        return pos

    return _hierarchy_pos(G, root, 0, width, vert_loc)


def visualize_tree(tree):
    G = nx.DiGraph()
    add_edges(G, tree)
    pos = hierarchy_pos(G, tree["key"])
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, arrows=False,
            node_size=2000, node_color="lightblue",
            font_size=10, font_weight="bold")
    plt.title("Optimal Binary Search Tree")
    plt.show()


# --------------------------
# MAIN PIPELINE
# --------------------------
if __name__ == "__main__":
    # 1. Load dictionary (dict.txt)
    dictionary = load_dict("dict.txt")

    # 2. Tokenize input file
    tokens = tokenize("input.txt")

    # 3. Compute probabilities
    probs, freq, total = compute_probabilities(tokens)

    # Use only words that appear in input.txt (Option A)
    keys = sorted(probs.keys())
    p = [probs[k] for k in keys]

    print("\n--- Word Probabilities ---")
    for k in keys:
        print(f"{k}: {probs[k]:.3f}")

    # 4. OBST construction
    e, root = optimal_bst(keys, p)
    obst_cost = e[1][len(keys)]
    obst_tree = build_tree(root, keys, 1, len(keys))

    # 5. AVL expected cost
    avl_tree = build_balanced_bst(keys)
    avl_cost = compute_expected_cost(avl_tree, probs)

    # Results
    print(f"\nExpected Search Cost (OBST) = {obst_cost:.3f}")
    print(f"Expected Search Cost (AVL)  = {avl_cost:.3f}")

    # 6. Visualize OBST
    if obst_tree:
        visualize_tree(obst_tree)


