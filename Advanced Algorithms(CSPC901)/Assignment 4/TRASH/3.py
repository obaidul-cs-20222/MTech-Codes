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
#         print("dict.txt not found, continuing without dictionary.")
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

#     for l in range(1, n + 1):
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
# # 5. AVL Expected Search Cost
# # --------------------------
# def build_balanced_bst(keys):
#     if not keys:
#         return None
#     mid = len(keys) // 2
#     return {
#         "key": keys[mid],
#         "left": build_balanced_bst(keys[:mid]),
#         "right": build_balanced_bst(keys[mid + 1:]),
#     }

# def compute_expected_cost(tree, probs, depth=1):
#     if not tree:
#         return 0
#     return (
#         probs[tree["key"]] * depth
#         + compute_expected_cost(tree["left"], probs, depth + 1)
#         + compute_expected_cost(tree["right"], probs, depth + 1)
#     )

# # --------------------------
# # 6. Visualization
# # --------------------------
# def add_edges(G, node, parent=None):
#     if not node:
#         return
#     G.add_node(node["key"])
#     if parent:
#         G.add_edge(parent, node["key"])
#     add_edges(G, node["left"], node["key"])
#     add_edges(G, node["right"], node["key"])

# def hierarchy_pos(G, root=None, width=1.0, vert_gap=0.2, vert_loc=0):
#     if root is None:
#         root = list(G.nodes)[0]

#     def _hierarchy_pos(G, root, left, right, vert_loc, pos=None):
#         if pos is None:
#             pos = {}
#         pos[root] = ((left + right) / 2, vert_loc)
#         neighbors = list(G.neighbors(root))
#         if neighbors:
#             dx = (right - left) / len(neighbors)
#             nextx = left
#             for neighbor in neighbors:
#                 pos = _hierarchy_pos(G, neighbor, nextx, nextx + dx, vert_loc - vert_gap, pos)
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
#     # 1. Load dictionary
#     dictionary = load_dict("dict.txt")

#     # 2. Tokenize input
#     tokens = tokenize("input.txt")

#     # 3. Compute probabilities
#     probs, freq, total = compute_probabilities(tokens)

#     # 4. Filter words that exist in dict.txt
#     filtered_keys = sorted([word for word in probs if word in dictionary])
#     p = [probs[word] for word in filtered_keys]

#     print("\n--- Word Probabilities (with Bengali) ---")
#     for word in filtered_keys:
#         print(f"{word}: {probs[word]:.3f}")

#     # 5. OBST construction
#     e, root = optimal_bst(filtered_keys, p)
#     obst_cost = e[1][len(filtered_keys)]
#     obst_tree = build_tree(root, filtered_keys, 1, len(filtered_keys))

#     # 6. AVL construction
#     avl_tree = build_balanced_bst(filtered_keys)
#     avl_cost = compute_expected_cost(avl_tree, probs)

#     # 7. Results
#     print(f"\nExpected Search Cost (OBST) = {obst_cost:.3f}")
#     print(f"Expected Search Cost (AVL)  = {avl_cost:.3f}")

#     # 8. Visualize OBST
#     if obst_tree:
#         visualize_tree(obst_tree)


# #Rain fell softly, softly on the rooftops. Children danced, danced with joy. Silence followed, and the world listened




















































import re
from collections import Counter
import networkx as nx
import matplotlib.pyplot as plt

# --------------------------
# 1. Load Dictionary
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
# 2. Tokenize input
# --------------------------
def tokenize(filename="input.txt"):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read().lower()
    return re.findall(r"[a-z']+", text)

# --------------------------
# 3. Compute probabilities
# --------------------------
def compute_probabilities(tokens, dictionary):
    freq = Counter(tokens)
    total = sum(freq.values())
    probs = {}
    for word in freq:
        if word in dictionary:
            probs[word] = freq[word] / total
        else:
            probs[word] = 0.0
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

    for l in range(1, n + 1):
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

def build_tree(root, keys, probs, i, j):
    if i > j:
        return None
    r = root[i][j]
    key = keys[r - 1]
    return {
        "key": key,
        "label": f"{key} ({probs[key]:.3f})",
        "left": build_tree(root, keys, probs, i, r - 1),
        "right": build_tree(root, keys, probs, r + 1, j),
    }

# --------------------------
# 5. AVL Expected Search Cost
# --------------------------
def build_balanced_bst(keys, probs):
    if not keys:
        return None
    mid = len(keys) // 2
    key = keys[mid]
    return {
        "key": key,
        "label": f"{key} ({probs[key]:.3f})",
        "left": build_balanced_bst(keys[:mid], probs),
        "right": build_balanced_bst(keys[mid + 1:], probs),
    }

def compute_expected_cost(tree, probs, depth=1):
    if not tree:
        return 0
    return (
        probs[tree["key"]] * depth
        + compute_expected_cost(tree["left"], probs, depth + 1)
        + compute_expected_cost(tree["right"], probs, depth + 1)
    )

# --------------------------
# 6. Visualization
# --------------------------
def add_edges(G, node, parent=None):
    if not node:
        return
    G.add_node(node["label"])
    if parent:
        G.add_edge(parent, node["label"])
    add_edges(G, node["left"], node["label"])
    add_edges(G, node["right"], node["label"])

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

def visualize_tree(tree, title="Optimal Binary Search Tree"):
    G = nx.DiGraph()
    add_edges(G, tree)
    pos = hierarchy_pos(G, tree["label"])
    plt.figure(figsize=(10, 7))
    nx.draw(G, pos, with_labels=True, arrows=False,
            node_size=2000, node_color="lightgreen",
            font_size=10, font_weight="bold")
    plt.title(title)
    plt.show()

# --------------------------
# MAIN PIPELINE
# --------------------------
if __name__ == "__main__":
    dictionary = load_dict("dict.txt")
    tokens = tokenize("input.txt")
    probs, freq, total = compute_probabilities(tokens, dictionary)

    print("\n--- Word Probabilities ---")
    for word in sorted(probs):
        bengali = dictionary.get(word, "—")
        print(f"{word}: {probs[word]:.3f} ")

    # Filter only dictionary words for tree construction
    filtered_keys = sorted([word for word in probs if word in dictionary and probs[word] > 0])
    p = [probs[word] for word in filtered_keys]

    # OBST
    e, root = optimal_bst(filtered_keys, p)
    obst_cost = e[1][len(filtered_keys)]
    obst_tree = build_tree(root, filtered_keys, probs, 1, len(filtered_keys))

    # AVL
    avl_tree = build_balanced_bst(filtered_keys, probs)
    avl_cost = compute_expected_cost(avl_tree, probs)

    print(f"\nExpected Search Cost (OBST) = {obst_cost:.3f}")
    print(f"Expected Search Cost (AVL)  = {avl_cost:.3f}")

    if obst_tree:
        visualize_tree(obst_tree)