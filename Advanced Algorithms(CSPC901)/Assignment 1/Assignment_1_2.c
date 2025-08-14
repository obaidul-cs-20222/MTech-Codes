#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define DATA_SIZE 10000
#define GROUP_SIZE 5

void swap(int *, int *);
void sort(int *, int, int);
int partitionArray(int *, int, int, int);
int findPivot(int *, int, int);
int selectKth(int *, int, int, int);

long long comparisonCounter = 0;

// Swap two integers
void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Insertion sort for small groups
void sort(int *array, int left, int right)
{
    for (int i = left + 1; i <= right; i++)
    {
        int key = array[i];
        int j = i - 1;
        while (j >= left && (++comparisonCounter && array[j] > key))
        {
            array[j + 1] = array[j];
            j--;
        }
        array[j + 1] = key;
    }
}

// Partition array around a pivot value
int partitionArray(int *array, int left, int right, int pivotValue)
{
    int pivotIndex = left;
    for (; pivotIndex <= right; pivotIndex++)
    {
        comparisonCounter++;
        if (array[pivotIndex] == pivotValue)
            break;
    }
    swap(&array[pivotIndex], &array[right]);

    int storeIndex = left;
    for (int i = left; i < right; i++)
    {
        comparisonCounter++;
        if (array[i] < pivotValue)
        {
            swap(&array[i], &array[storeIndex]);
            storeIndex++;
        }
    }
    swap(&array[storeIndex], &array[right]);
    return storeIndex;
}

// Recursive median-of-medians pivot selection
int findPivot(int *a, int left, int right)
{
    int size = right - left + 1;

    if (size <= GROUP_SIZE)
    {
        sort(a, left, right);
        return a[left + size / 2];
    }

    int numGroups = (size + GROUP_SIZE - 1) / GROUP_SIZE;
    int *medians = (int *)malloc(numGroups * sizeof(int));

    for (int i = 0; i < numGroups; i++)
    {
        int groupStart = left + i * GROUP_SIZE;
        int groupEnd = groupStart + GROUP_SIZE - 1;
        if (groupEnd > right)
            groupEnd = right;

        sort(a, groupStart, groupEnd);
        medians[i] = a[groupStart + (groupEnd - groupStart) / 2];
    }

    int pivot = findPivot(medians, 0, numGroups - 1);
    free(medians);
    return pivot;
}

// Deterministic selection algorithm
int selectKth(int *a, int left, int right, int k)
{
    if (left == right)
        return a[left];

    int pivot = findPivot(a, left, right);
    int pivotIndex = partitionArray(a, left, right, pivot);

    if (k == pivotIndex)
        return a[k];
    else if (k < pivotIndex)
        return selectKth(a, left, pivotIndex - 1, k);
    else
        return selectKth(a, pivotIndex + 1, right, k);
}

int main()
{
    srand(time(0));

    int *a = (int *)malloc(DATA_SIZE * sizeof(int));
    int *kthSmallestValues = (int *)malloc(DATA_SIZE * sizeof(int));
    long long *comparisonStats = (long long *)malloc(DATA_SIZE * sizeof(long long));

    // Generate random data
    for (int i = 0; i < DATA_SIZE; i++)
    {
        a[i] = rand() % 100000;
    }

    // Compute i-th smallest elements
    for (int i = 0; i < DATA_SIZE; i++)
    {
        int *dataCopy = (int *)malloc(DATA_SIZE * sizeof(int));
        for (int j = 0; j < DATA_SIZE; j++)
            dataCopy[j] = a[j];

        comparisonCounter = 0;
        kthSmallestValues[i] = selectKth(dataCopy, 0, DATA_SIZE - 1, i);
        comparisonStats[i] = comparisonCounter;

        free(dataCopy);
    }

    // Display first 10 results
    printf("Index\tValue\tComparisons\n");
    for (int i = 0; i < 10; i++)
    {
        printf("%d\t%d\t%lld\n", i + 1, kthSmallestValues[i], comparisonStats[i]);
    }

    free(a);
    free(kthSmallestValues);
    free(comparisonStats);

    return 0;
}

// #include <stdio.h>
// #include <stdlib.h>
// #include <time.h>

// #define SIZE 10000
// #define GROUP_SIZE 5

// long long comparison_count = 0;
// int *a; // dynamically allocated array

// // Swap helper
// static inline void swapVals(int *p, int *q)
// {
//     int temp = *p;
//     *p = *q;
//     *q = temp;
// }

// // Insertion sort for small ranges (modified style)
// void insertionSortRange(int arr[], int left, int right)
// {
//     for (int idx = left + 1; idx <= right; idx++)
//     {
//         int hold = arr[idx];
//         int j = idx - 1;
//         while (j >= left && (++comparison_count && arr[j] > hold))
//         {
//             arr[j + 1] = arr[j];
//             j--;
//         }
//         arr[j + 1] = hold;
//     }
// }

// // Partition identical in behavior to original, but restructured
// int splitAroundPivot(int arr[], int start, int end, int pivotVal)
// {
//     int i = start;
//     // find pivot position in array
//     for (; i <= end; i++)
//     {
//         comparison_count++;
//         if (arr[i] == pivotVal)
//             break;
//     }
//     swapVals(&arr[i], &arr[end]); // pivot to end

//     int storePos = start;
//     for (i = start; i < end; i++)
//     {
//         comparison_count++;
//         if (arr[i] < pivotVal)
//         {
//             swapVals(&arr[storePos], &arr[i]);
//             storePos++;
//         }
//     }
//     swapVals(&arr[storePos], &arr[end]); // pivot to final location
//     return storePos;
// }

// // Median of Medians pivot selection
// int pickMedianOfMedians(int arr[], int left, int right)
// {
//     int count = right - left + 1;
//     if (count <= GROUP_SIZE)
//     {
//         insertionSortRange(arr, left, right);
//         return arr[left + count / 2];
//     }

//     int totalGroups = (count + GROUP_SIZE - 1) / GROUP_SIZE;
//     int *medianVals = malloc(totalGroups * sizeof(int));
//     if (!medianVals)
//     {
//         fprintf(stderr, "Allocation failed.\n");
//         exit(EXIT_FAILURE);
//     }

//     for (int g = 0; g < totalGroups; g++)
//     {
//         int gStart = left + g * GROUP_SIZE;
//         int gEnd = gStart + GROUP_SIZE - 1;
//         if (gEnd > right)
//             gEnd = right;

//         insertionSortRange(arr, gStart, gEnd);
//         medianVals[g] = arr[gStart + (gEnd - gStart) / 2];
//     }

//     int median = pickMedianOfMedians(medianVals, 0, totalGroups - 1);
//     free(medianVals);
//     return median;
// }

// // Deterministic selection
// int kthSmallest(int arr[], int left, int right, int k)
// {
//     if (left == right)
//         return arr[left];

//     int pivotVal = pickMedianOfMedians(arr, left, right);
//     int pivotPos = splitAroundPivot(arr, left, right, pivotVal);

//     if (k == pivotPos)
//         return arr[k];
//     else if (k < pivotPos)
//         return kthSmallest(arr, left, pivotPos - 1, k);
//     else
//         return kthSmallest(arr, pivotPos + 1, right, k);
// }

// int main()
// {
//     srand(time(0));
//     a = malloc(SIZE * sizeof(int));
//     if (!a)
//     {
//         printf(stderr, "Memory allocation failed.\n");
//         return EXIT_FAILURE;
//     }

//     for (int i = 0; i < SIZE; i++)
//     {
//         a[i] = rand() % 100000;
//     }

//     int *orderStats = malloc(SIZE * sizeof(int));
//     long long *compLog = malloc(SIZE * sizeof(long long));
//     if (!orderStats || !compLog)
//     {
//         printf(stderr, "Memory allocation failed.\n");
//         free(a);
//         return 1;
//     }

//     for (int i = 1; i <= SIZE; i++)
//     {
//         int *tempCopy = malloc(SIZE * sizeof(int));
//         if (!tempCopy)
//         {
//             printf(stderr, "Memory allocation failed.\n");
//             free(a);
//             free(orderStats);
//             free(compLog);
//             return 1;
//         }
//         for (int j = 0; j < SIZE; j++)
//             tempCopy[j] = a[j];

//         comparison_count = 0;
//         orderStats[i - 1] = kthSmallest(tempCopy, 0, SIZE - 1, i - 1);
//         compLog[i - 1] = comparison_count;
//         free(tempCopy);
//     }

//     printf("i\tValue\tComparisons\n");
//     for (int i = 0; i < 10; i++)
//     {
//         printf("%d\t%d\t%lld\n", i + 1, orderStats[i], compLog[i]);
//     }

//     free(a);
//     free(orderStats);
//     free(compLog);
//     return 0;
// }

// part 2

// #include <stdio.h>
// #include <stdlib.h>
// #include <time.h>

// #define DATA_SIZE 10000
// #define CHUNK_SIZE 5

// long long comparison_counter = 0;

// // Swap two integers
// void exchange(int *x, int *y)
// {
//     int temp = *x;
//     *x = *y;
//     *y = temp;
// }

// // Insertion sort for small segments
// void sort(int *array, int start, int end)
// {
//     for (int i = start + 1; i <= end; i++)
//     {
//         int current = array[i];
//         int j = i - 1;
//         while (j >= start && (++comparison_counter && array[j] > current))
//         {
//             array[j + 1] = array[j];
//             j--;
//         }
//         array[j + 1] = current;
//     }
// }

// // Partition array around a pivot
// int divideAroundPivot(int *array, int start, int end, int pivot)
// {
//     int pivotIndex = start;
//     for (; pivotIndex <= end; pivotIndex++)
//     {
//         comparison_counter++;
//         if (array[pivotIndex] == pivot)
//             break;
//     }
//     exchange(&array[pivotIndex], &array[end]);

//     int storeIndex = start;
//     for (int i = start; i < end; i++)
//     {
//         comparison_counter++;
//         if (array[i] < pivot)
//         {
//             exchange(&array[i], &array[storeIndex]);
//             storeIndex++;
//         }
//     }
//     exchange(&array[storeIndex], &array[end]);
//     return storeIndex;
// }

// // Recursive median-of-medians pivot selection
// int findPivot(int *a, int start, int end)
// {
//     int length = end - start + 1;

//     if (length <= CHUNK_SIZE)
//     {
//         sort(a, start, end);
//         return a[start + length / 2];
//     }

//     int numChunks = (length + CHUNK_SIZE - 1) / CHUNK_SIZE;
//     int *medians = (int *)malloc(numChunks * sizeof(int));

//     for (int i = 0; i < numChunks; i++)
//     {
//         int chunkStart = start + i * CHUNK_SIZE;
//         int chunkEnd = chunkStart + CHUNK_SIZE - 1;
//         if (chunkEnd > end)
//             chunkEnd = end;

//         sort(a, chunkStart, chunkEnd);
//         medians[i] = a[chunkStart + (chunkEnd - chunkStart) / 2];
//     }

//     int pivot = findPivot(medians, 0, numChunks - 1);
//     free(medians);
//     return pivot;
// }

// // Deterministic selection algorithm
// int Select(int *array, int start, int end, int k)
// {
//     if (start == end)
//         return array[start];

//     int pivot = findPivot(array, start, end);
//     int pivotIndex = divideAroundPivot(array, start, end, pivot);

//     if (k == pivotIndex)
//         return array[k];
//     else if (k < pivotIndex)
//         return Select(array, start, pivotIndex - 1, k);
//     else
//         return Select(array, pivotIndex + 1, end, k);
// }

// int main()
// {
//     srand((unsigned int)time(NULL));

//     int *data = (int *)malloc(DATA_SIZE * sizeof(int));
//     int *results = (int *)malloc(DATA_SIZE * sizeof(int));
//     long long *comparisonLog = (long long *)malloc(DATA_SIZE * sizeof(long long));

//     // Generate random data
//     for (int i = 0; i < DATA_SIZE; i++)
//     {
//         data[i] = rand() % 100000;
//     }

//     // Compute i-th smallest elements
//     for (int i = 0; i < DATA_SIZE; i++)
//     {
//         int *copy = (int *)malloc(DATA_SIZE * sizeof(int));
//         for (int j = 0; j < DATA_SIZE; j++)
//             copy[j] = data[j];

//         comparison_counter = 0;
//         results[i] = Select(copy, 0, DATA_SIZE - 1, i);
//         comparisonLog[i] = comparison_counter;

//         free(copy);
//     }

//     // Display first 10 results
//     printf("Index\tValue\tComparisons\n");
//     for (int i = 0; i < 10; i++)
//     {
//         printf("%d\t%d\t%lld\n", i + 1, results[i], comparisonLog[i]);
//     }

//     free(data);
//     free(results);
//     free(comparisonLog);

//     return 0;
// }