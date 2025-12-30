# import matplotlib.pyplot as plt
# import numpy as np

# input_sizes = [1000, 5000, 10000, 20000, 50000]
# max_levels = [10, 10, 11, 13, 15]  # Example max levels used
# avg_levels = [6.5, 7.2, 7.8, 8.5, 9.1]  # Example average levels used
# plt.figure(figsize=(12, 5))
# plt.plot(input_sizes, max_levels, marker='o', color='b', label='Insertion Time')
# plt.title('Skip List Performance Analysis') 
# plt.grid(True)        
# plt.ylabel('levels')
# plt.xlabel('input_sizes')     
# plt.show()



import matplotlib.pyplot as plt

input_sizes = [1000, 5000, 10000, 20000, 50000]
max_levels = [10, 10, 11, 13, 15]   # Example max levels
avg_levels = [1.01, 1.00, 1.01, 1.01, 1.01]  # Example average levels

plt.figure(figsize=(12, 5))

# --- First subplot: Max Levels ---
plt.subplot(2, 1, 1)   # (rows, cols, index)
plt.plot(input_sizes, max_levels, marker='o', color='blue', label='Max Level')
plt.title('Skip List Performance Analysis')
plt.ylabel('Max Level')
plt.xlabel('Input Size')
plt.grid(True)
plt.legend()

# --- Second subplot: Average Levels ---
plt.subplot(2, 1, 2)
plt.plot(input_sizes, avg_levels, marker='s', color='orange', label='Average Level')
plt.ylabel('Average Level')
plt.xlabel('Input Size')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()