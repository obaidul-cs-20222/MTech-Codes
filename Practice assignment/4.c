#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

/* -------- Task 4A: Insertion Sort (Pointer-based) -------- */
void insertion_sort_ptr(int *data, int size)
{
    int *p, *q, temp;
    for (p = data + 1; p < data + size; p++)
    {
        temp = *p;
        q = p - 1;
        while (q >= data && *q > temp)
        {
            *(q + 1) = *q;
            q--;
        }
        *(q + 1) = temp;
    }
}

/* -------- Task 4B: Custom token extraction (like strtok) -------- */
char *custom_tokenizer(char *input, const char *delimiters)
{
    static char *next;
    if (input != NULL)
        next = input; // set starting point

    if (next == NULL)
        return NULL;

    // Skip leading delimiters
    next += strspn(next, delimiters);
    if (*next == '\0')
        return NULL;

    char *start = next;
    next = strpbrk(next, delimiters);
    if (next != NULL)
    {
        *next = '\0';
        next++;
    }
    return start;
}

/* -------- Task 4C: Shell Sort -------- */
void shell_sort(int *data, int size)
{
    for (int gap = size / 2; gap > 0; gap /= 2)
    {
        for (int i = gap; i < size; i++)
        {
            int temp = data[i];
            int j = i;
            while (j >= gap && data[j - gap] > temp)
            {
                data[j] = data[j - gap];
                j -= gap;
            }
            data[j] = temp;
        }
    }
}

int main()
{
    /* --- Test Insertion Sort --- */
    int nums1[] = {9, 5, 1, 4, 3};
    int len1 = sizeof(nums1) / sizeof(nums1[0]);
    insertion_sort_ptr(nums1, len1);

    printf("Insertion Sort result: ");
    for (int i = 0; i < len1; i++)
    {
        printf("%d ", nums1[i]);
    }
    printf("\n");

    /* --- Test Custom Tokenizer --- */
    char text[] = "C,Java;Python|Go";
    char *tok = custom_tokenizer(text, ",;|");

    printf("Extracted tokens: ");
    while (tok != NULL)
    {
        printf("%s ", tok);
        tok = custom_tokenizer(NULL, ",;|");
    }
    printf("\n");

    /* --- Test Shell Sort --- */
    int nums2[] = {12, 34, 54, 2, 3};
    int len2 = sizeof(nums2) / sizeof(nums2[0]);
    shell_sort(nums2, len2);

    printf("Shell Sort result: ");
    for (int i = 0; i < len2; i++)
    {
        printf("%d ", nums2[i]);
    }
    printf("\n");

    return 0;
}
