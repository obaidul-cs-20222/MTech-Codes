#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

/* ------------ Stack Implementation for Expression Handling ------------ */
#define STACK_CAPACITY 100
typedef struct
{
    int topIndex;
    char data[STACK_CAPACITY];
} CharStack;

void pushChar(CharStack *stack, char ch)
{
    stack->data[++(stack->topIndex)] = ch;
}

char popChar(CharStack *stack)
{
    return stack->data[(stack->topIndex)--];
}

char peekChar(CharStack *stack)
{
    return stack->data[stack->topIndex];
}

int isStackEmpty(CharStack *stack)
{
    return stack->topIndex == -1;
}

int operatorPriority(char op)
{
    if (op == '+' || op == '-')
        return 1;
    if (op == '*' || op == '/')
        return 2;
    return 0;
}

void convertInfixToPostfix(const char *infixExpr, char *postfixExpr)
{
    CharStack st;
    st.topIndex = -1;
    int outIndex = 0;

    for (int i = 0; infixExpr[i] != '\0'; i++)
    {
        char current = infixExpr[i];
        if (isalnum(current))
        {
            postfixExpr[outIndex++] = current;
        }
        else if (current == '(')
        {
            pushChar(&st, current);
        }
        else if (current == ')')
        {
            while (!isStackEmpty(&st) && peekChar(&st) != '(')
            {
                postfixExpr[outIndex++] = popChar(&st);
            }
            popChar(&st); // remove '('
        }
        else
        { // operator
            while (!isStackEmpty(&st) &&
                   operatorPriority(peekChar(&st)) >= operatorPriority(current))
            {
                postfixExpr[outIndex++] = popChar(&st);
            }
            pushChar(&st, current);
        }
    }
    while (!isStackEmpty(&st))
    {
        postfixExpr[outIndex++] = popChar(&st);
    }
    postfixExpr[outIndex] = '\0';
}

/* ------------ Simple Hash Table (Linear Probing) ------------ */
#define TABLE_SIZE 10
typedef struct
{
    int key;
    int value;
} HashEntry;

HashEntry *table[TABLE_SIZE] = {NULL};

int hashFunc(int key)
{
    return key % TABLE_SIZE;
}

void insertEntry(int key, int value)
{
    int idx = hashFunc(key);
    while (table[idx] != NULL && table[idx]->key != -1)
    {
        idx = (idx + 1) % TABLE_SIZE;
    }
    HashEntry *newItem = (HashEntry *)malloc(sizeof(HashEntry));
    newItem->key = key;
    newItem->value = value;
    table[idx] = newItem;
}

int findValue(int key)
{
    int idx = hashFunc(key);
    int attempts = 0;
    while (table[idx] != NULL && attempts < TABLE_SIZE)
    {
        if (table[idx]->key == key)
            return table[idx]->value;
        idx = (idx + 1) % TABLE_SIZE;
        attempts++;
    }
    return -1; // not found
}

/* ------------ Main Menu ------------ */
int main()
{
    int option;
    char infix[100], postfix[100];
    int key, val, searchResult;

    do
    {
        printf("\n--- Menu ---\n");
        printf("1. Convert infix to postfix\n");
        printf("2. Insert into hash table\n");
        printf("3. Search in hash table\n");
        printf("0. Exit\n");
        printf("Enter choice: ");
        scanf("%d", &option);

        switch (option)
        {
        case 1:
            printf("Enter infix expression (single-letter operands): ");
            scanf("%s", infix);
            convertInfixToPostfix(infix, postfix);
            printf("Postfix: %s\n", postfix);
            break;
        case 2:
            printf("Enter key: ");
            scanf("%d", &key);
            printf("Enter value: ");
            scanf("%d", &val);
            insertEntry(key, val);
            printf("Inserted (%d, %d)\n", key, val);
            break;
        case 3:
            printf("Enter key to search: ");
            scanf("%d", &key);
            searchResult = findValue(key);
            if (searchResult == -1)
                printf("Key not found\n");
            else
                printf("Value: %d\n", searchResult);
            break;
        case 0:
            printf("Goodbye!\n");
            break;
        default:
            printf("Invalid selection\n");
        }
    } while (option != 0);

    return 0;
}
