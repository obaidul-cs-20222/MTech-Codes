#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>

#define MAX_LEVEL 16
#define P 0.5

int main(void)
{
    srand((unsigned)time(NULL));

    int sizes[] = {1000, 5000, 10000, 20000};
    int m = sizeof(sizes) / sizeof(sizes[0]);

    for (int k = 0; k < m; ++k)
    {
        int n = sizes[k];
        SkipList *sl = create_skiplist();

        double t_insert = measure(insert, sl, n);
        double t_search = measure_search(sl, n);
        double t_delete = measure(delete_key, sl, n);

        printf("Size %d: Insert=%.6fs, Search=%.6fs, Delete=%.6fs\n",
               n, t_insert, t_search, t_delete);

        free_skiplist(sl);
    }

    return 0;
}

typedef struct Node
{
    int key;
    struct Node **forward; // array of forward pointers
    int level;
} Node;

typedef struct SkipList
{
    int level;
    Node *header;
} SkipList;

static int random_level(void)
{
    int lvl = 0;
    while (((double)rand() / RAND_MAX) < P && lvl < MAX_LEVEL)
    {
        lvl++;
    }
    return lvl;
}

static Node *create_node(int key, int level)
{
    Node *n = (Node *)malloc(sizeof(Node));
    n->key = key;
    n->level = level;
    n->forward = (Node **)calloc(level + 1, sizeof(Node *));
    return n;
}

SkipList *create_skiplist(void)
{
    SkipList *sl = (SkipList *)malloc(sizeof(SkipList));
    sl->level = 0;
    sl->header = create_node(-1, MAX_LEVEL);
    return sl;
}

void insert(SkipList *sl, int key)
{
    Node *update[MAX_LEVEL + 1];
    Node *current = sl->header;

    for (int i = sl->level; i >= 0; --i)
    {
        while (current->forward[i] && current->forward[i]->key < key)
        {
            current = current->forward[i];
        }
        update[i] = current;
    }

    current = current->forward[0];

    if (current == NULL || current->key != key)
    {
        int lvl = random_level();
        if (lvl > sl->level)
        {
            for (int i = sl->level + 1; i <= lvl; ++i)
            {
                update[i] = sl->header;
            }
            sl->level = lvl;
        }

        Node *new_node = create_node(key, lvl);
        for (int i = 0; i <= lvl; ++i)
        {
            new_node->forward[i] = update[i]->forward[i];
            update[i]->forward[i] = new_node;
        }
    }
}

bool search(SkipList *sl, int key)
{
    Node *current = sl->header;
    for (int i = sl->level; i >= 0; --i)
    {
        while (current->forward[i] && current->forward[i]->key < key)
        {
            current = current->forward[i];
        }
    }
    current = current->forward[0];
    return current && current->key == key;
}

void delete_key(SkipList *sl, int key)
{
    Node *update[MAX_LEVEL + 1];
    Node *current = sl->header;

    for (int i = sl->level; i >= 0; --i)
    {
        while (current->forward[i] && current->forward[i]->key < key)
        {
            current = current->forward[i];
        }
        update[i] = current;
    }

    current = current->forward[0];

    if (current && current->key == key)
    {
        for (int i = 0; i <= sl->level; ++i)
        {
            if (update[i]->forward[i] != current)
                break;
            update[i]->forward[i] = current->forward[i];
        }
        // free node
        free(current->forward);
        free(current);

        while (sl->level > 0 && sl->header->forward[sl->level] == NULL)
        {
            sl->level--;
        }
    }
}

void free_skiplist(SkipList *sl)
{
    Node *current = sl->header->forward[0];
    while (current)
    {
        Node *next = current->forward[0];
        free(current->forward);
        free(current);
        current = next;
    }
    free(sl->header->forward);
    free(sl->header);
    free(sl);
}

// #include <stdio.h>
// #include <stdlib.h>
// #include <time.h>
// #include <stdbool.h>

// Forward declarations from the implementation file if split.
// For single-file usage, paste this below the implementation.
// extern SkipList *create_skiplist(void);
// extern void insert(SkipList *sl, int key);
// extern bool search(SkipList *sl, int key);
// extern void delete_key(SkipList *sl, int key);
// extern void free_skiplist(SkipList *sl);

// Measure elapsed time in seconds using clock()
static double measure(void (*fn)(SkipList *, int), SkipList *sl, int n)
{
    clock_t start = clock();
    for (int i = 0; i < n; ++i)
        fn(sl, i);
    clock_t end = clock();
    return (double)(end - start) / CLOCKS_PER_SEC;
}

static double measure_search(SkipList *sl, int n)
{
    clock_t start = clock();
    for (int i = 0; i < n; ++i)
        (void)search(sl, i);
    clock_t end = clock();
    return (double)(end - start) / CLOCKS_PER_SEC;
}
