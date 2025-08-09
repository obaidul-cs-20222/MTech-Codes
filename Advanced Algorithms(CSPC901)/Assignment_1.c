#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define SIZE 10000
#define GROUP_SIZE 5

long long comparison_count = 0; // count comparisons

// Swap function
void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Simple insertion sort for small groups
void insertionSort(int arr[], int left, int right)
{
    for (int i = left + 1; i <= right; i++)
    {
        int key = arr[i];
        int j = i - 1;
        while (j >= left && (++comparison_count && arr[j] > key))
        {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

// Partition around a pivot value
int partition(int arr[], int left, int right, int pivot)
{
    int i;
    for (i = left; i <= right; i++)
    {
        comparison_count++;
        if (arr[i] == pivot)
            break;
    }
    swap(&arr[i], &arr[right]); // move pivot to end

    int storeIndex = left;
    for (i = left; i < right; i++)
    {
        comparison_count++;
        if (arr[i] < pivot)
        {
            swap(&arr[storeIndex], &arr[i]);
            storeIndex++;
        }
    }
    swap(&arr[storeIndex], &arr[right]); // move pivot to its final place
    return storeIndex;
}

// Recursive Median of Medians function to find pivot
int medianOfMedians(int arr[], int left, int right)
{
    int n = right - left + 1;

    if (n <= GROUP_SIZE)
    {
        insertionSort(arr, left, right);
        return arr[left + n / 2];
    }

    int numMedians = (n + GROUP_SIZE - 1) / GROUP_SIZE;
    int medians[numMedians];

    for (int i = 0; i < numMedians; i++)
    {
        int subLeft = left + i * GROUP_SIZE;
        int subRight = subLeft + GROUP_SIZE - 1;
        if (subRight > right)
            subRight = right;

        insertionSort(arr, subLeft, subRight);
        medians[i] = arr[subLeft + (subRight - subLeft) / 2];
    }

    return medianOfMedians(medians, 0, numMedians - 1);
}

// Deterministic selection (Median of Medians)
int selectKth(int arr[], int left, int right, int k)
{
    if (left == right)
        return arr[left];

    int pivot = medianOfMedians(arr, left, right);
    int pivotIndex = partition(arr, left, right, pivot);

    if (k == pivotIndex)
        return arr[k];
    else if (k < pivotIndex)
        return selectKth(arr, left, pivotIndex - 1, k);
    else
        return selectKth(arr, pivotIndex + 1, right, k);
}

int main()
{
    int arr[SIZE];
    int ith_smallest[SIZE];
    long long comparisons[SIZE];
    srand(time(NULL));

    // Generate random array
    for (int i = 0; i < SIZE; i++)
    {
        arr[i] = rand() % 100000;
    }

    // Find i-th smallest for i=1 to SIZE
    for (int i = 1; i <= SIZE; i++)
    {
        int temp[SIZE];
        for (int j = 0; j < SIZE; j++)
            temp[j] = arr[j];

        comparison_count = 0;
        ith_smallest[i - 1] = selectKth(temp, 0, SIZE - 1, i - 1);
        comparisons[i - 1] = comparison_count;
    }

    // Show first 10 results
    printf("i\tValue\tComparisons\n");
    for (int i = 0; i < 10; i++)
    {
        printf("%d\t%d\t%lld\n", i + 1, ith_smallest[i], comparisons[i]);
    }

    return 0;
}