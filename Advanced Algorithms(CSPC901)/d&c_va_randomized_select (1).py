import random
import numpy as np
import time
import matplotlib.pyplot as plt

#..................D and C select Algorithm .................................
#................merge_sort to sort the subscripts and medians list ................
def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    left_sorted, left_comparisons = merge_sort(left_half)
    right_sorted, right_comparisons = merge_sort(right_half)
    merged_array, merge_comparisons = merge(left_sorted, right_sorted)
    total_comparisons = left_comparisons + right_comparisons + merge_comparisons
    return merged_array, total_comparisons

def merge(left, right):
    sorted_array = []
    i = j = 0
    comparisons = 0
    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    return sorted_array, comparisons
#..............................................................................

#.......................median of median method................................ 
def median_of_medians(arr,k_th,comparison_count):
    length_of_subscript = 5
    subscripts = []
    for i in range(0,len(arr),length_of_subscript):
        sorted_array, comparisons = merge_sort(arr[i:i+length_of_subscript])
        subscripts.append(sorted_array)
        comparison_count += comparisons
    # print(subscripts)
    medians = []
    for i in range(0,len(subscripts)):
        temp = subscripts[i]
        # print('temp',temp)
        medians.append(temp[len(temp)//2])
    # print('medians',medians)
    sorted_array, comparisons = merge_sort(np.array(medians))
    pivot = sorted_array[len(sorted_array)//2]
    comparison_count += comparisons
    
    left = [j for j in arr if j < pivot]
    right = [j for j in arr if j > pivot]
    comparison_count += len(left)
    comparison_count += len(right)
    
    k = len(left)
    if k_th < k:
        return median_of_medians(left,k_th,comparison_count)
    elif k_th > k:
        return median_of_medians(right,k_th-k-1,comparison_count)
    else:
        return pivot,comparison_count

#..................D and C select Algorithm .................................
    
#..................Randomized Select Algorithm...............................
def randomized_select(arr, k_th, comparison_count=0):
    if len(arr) == 1:
        return arr[0], comparison_count

    # Pick a random pivot index and swap the pivot with the last element
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    arr[pivot_index], arr[-1] = arr[-1], arr[pivot_index]

    left, right, comparisons = partition(arr, pivot)
    comparison_count += comparisons

    k = len(left)

    if k_th < k:
        return randomized_select(left, k_th, comparison_count)
    elif k_th > k:
        return randomized_select(right, k_th - k - 1, comparison_count)
    else:
        return pivot, comparison_count

def partition(arr, pivot):
    left = []
    right = []
    comparisons = 0
    for element in arr[:-1]: 
        comparisons += 1
        if element < pivot:
            left.append(element)
        else:
            right.append(element)
    return left, right, comparisons
#..................Randomized Select Algorithm...............................

def measure_time(algorithm, x, y):
    start = time.time()
    result, comparison_count = algorithm(x, y, comparison_count = 0)
    end = time.time()
    return end - start, result, comparison_count

#...........test to check wheather the algorithms are returning the right results...........
# arr = [5,10,8,7,21,9,1,4,3,6,75]
# k_th = 8
# result1, count1 = randomized_select(arr,k_th-1,0)
# result2, count2 = median_of_medians(arr,k_th-1,0)
# print(f'Result of Randomized: {result1}')
# print(f'Result of D and C {result2}')

if __name__ == "__main__":
    no_of_comparison = []  
    ks = []
    k_th_least_elements = []
    size_array = [100, 500, 1000, 3000, 5000, 10000, 20000, 30000, 50000]
    dandc_time_taken = [] 
    randomized_time_taken = []
    
    
    for size in size_array:
        arr = list(random.sample(range(1, 100000), size))
        k_th = random.randint(1, size)
        # for k_th in np.array(random.sample(range(1, size), 3)):
        #     ks.append(k_th)
        
        d_and_c_time, d_and_c_kth_value, d_and_c_comparisons = measure_time(median_of_medians, arr, k_th)
        rand_time, rand_kth_value, rand_comparisons = measure_time(randomized_select, arr, k_th)
        no_of_comparison.append(d_and_c_comparisons)
        no_of_comparison.append(rand_comparisons)
        k_th_least_elements.append(d_and_c_kth_value)
        k_th_least_elements.append(rand_kth_value)
        dandc_time_taken.append(d_and_c_time)
        randomized_time_taken.append(rand_time)
    print(len(randomized_time_taken),randomized_time_taken)
    print(len(dandc_time_taken),dandc_time_taken)
    
    X_values = [100, 500, 1000, 3000, 5000, 10000, 20000, 30000, 50000]
    plt.figure(figsize=(12,5))
    plt.plot(X_values, dandc_time_taken, label = 'D & C Select execution time', color ='orange')
    plt.plot(X_values, randomized_time_taken, label = 'Randomized Select execution time', color = 'blue')
    plt.title('D & C Select VS Randomized Select')
    plt.xlabel('no. of elements')
    plt.ylabel('time taken (seconds)')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    
   

