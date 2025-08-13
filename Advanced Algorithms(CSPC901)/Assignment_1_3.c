#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define GROUP_SIZE 5

void swap(int *, int *);
void sort(int *, int, int);
int partitionArray(int *, int, int, int);
int findPivot(int *, int, int);
int selectKth(int *, int, int, int);

long long comparisonCounter = 0;

int main()
{
    srand(time(0));
    int DATA_SIZE[4] = {1000, 10000, 20000, 50000};
    int counter = 0;
    while (counter != 4)
    {
        int *a = (int *)malloc(DATA_SIZE[counter] * sizeof(int));
        int *kthSmallestValues = (int *)malloc(DATA_SIZE[counter] * sizeof(int));
        long long *comparisonStats = (long long *)malloc(DATA_SIZE[counter] * sizeof(long long));

        // Generate random data
        for (int i = 0; i < DATA_SIZE[counter]; i++)
        {
            a[i] = rand() % 100000;
        }

        // Compute i-th smallest elements
        for (int i = 0; i < DATA_SIZE[counter]; i++)
        {
            int *dataCopy = (int *)malloc(DATA_SIZE[counter] * sizeof(int));
            for (int j = 0; j < DATA_SIZE[counter]; j++)
                dataCopy[j] = a[j];

            comparisonCounter = 0;
            kthSmallestValues[i] = selectKth(dataCopy, 0, DATA_SIZE[counter] - 1, i);
            comparisonStats[i] = comparisonCounter;

            free(dataCopy);
        }

        printf("\nInput Size\tIndex\tValue\tComparisons\n");
        printf("%d\t\t", DATA_SIZE[counter]);
        for (int i = 0; i < 3; i++)
        {
            int num = rand() % 10 + 1;
            num = num + i;
            printf("  %d\t %d\t %lld\n", num, kthSmallestValues[num], comparisonStats[i]);
            printf("\t\t");
        }

        free(a);
        free(kthSmallestValues);
        free(comparisonStats);
        counter++;
    }
    printf("\nAll iterations completed.\n");
    return 0;
}

void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

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