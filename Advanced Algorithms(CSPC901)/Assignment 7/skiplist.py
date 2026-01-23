import random
import matplotlib.pyplot as plt

MAX_LEVEL = 20
P = 0.5


# Node structure definition

class Node:
    def __init__(self, key, level):
        self.key = key
        self.level = level
        self.forward = [None] * (level + 1)


# Skip List definition
class SkipList:

        # - level: current highest level in use
        # - max_level_reached: the maximum level reached historically
        # - header: header node (acts as start of all levels)
        # - total_levels: cumulative level count of all nodes (for average calculation)
        # - node_count: total number of nodes
        
    def __init__(self):
        self.level = 0
        self.max_level_reached = 0
        self.header = Node(-1, MAX_LEVEL)
        self.total_levels = 0
        self.node_count = 0

    def random_level(self):
        lvl = 0
        while random.random() < P and lvl < MAX_LEVEL:
            lvl += 1
        return lvl

    def insert(self, key):
        update = [None] * (MAX_LEVEL + 1)
        current = self.header

        for i in range(self.level, -1, -1):# Step 1: Traverse top-down to find where to insert
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current # Node before insertion point on this level

        current = current.forward[0]

        if current is None or current.key != key:# Step 2: If the key is not already in the list, insert it
            lvl = self.random_level()

            if lvl > self.level:  # If new node's level is higher than current max level, update header
                for i in range(self.level + 1, lvl + 1):
                    update[i] = self.header
                self.level = lvl  # Update current list level

            self.max_level_reached = max(self.max_level_reached, lvl)

            new_node = Node(key, lvl)  # Step 3: Create new node and insert into each level
            for i in range(lvl + 1):
                new_node.forward[i] = update[i].forward[i]
                update[i].forward[i] = new_node

            self.total_levels += lvl
            self.node_count += 1

    def avg_level(self):
        if self.node_count == 0:
            return 0
        return self.total_levels / self.node_count



random.seed()

sizes = [1000, 5000, 10000, 20000, 50000]
avg_levels = []

for n in sizes:
    sl = SkipList()
    for i in range(n):
        sl.insert(i)

    avg_levels.append(sl.avg_level())
    print(f"n = {n}, Average levels searched ≈ {sl.avg_level():.3f}")


plt.figure()
plt.plot(sizes, avg_levels, marker='o')
plt.xlabel("Number of elements (n)")
plt.ylabel("Average number of levels searched")
plt.title("Skip List: n vs Average Number of Levels Searched")
plt.grid(True)
plt.show()

