#include <stdio.h>
#include <stdlib.h>

/* ------------ Singly Linked List ------------ */
typedef struct ListNode
{
    int value;
    struct ListNode *next;
} ListNode;

ListNode *appendNode(ListNode *head, int val)
{
    ListNode *newNode = malloc(sizeof(ListNode));
    newNode->value = val;
    newNode->next = NULL;
    if (!head)
        return newNode;
    ListNode *current = head;
    while (current->next)
        current = current->next;
    current->next = newNode;
    return head;
}

void printList(ListNode *head)
{
    if (!head)
    {
        printf("Linked list is empty.\n");
        return;
    }
    while (head)
    {
        printf("%d -> ", head->value);
        head = head->next;
    }
    printf("NULL\n");
}

ListNode *removeNode(ListNode *head, int val)
{
    ListNode *curr = head, *prev = NULL;
    while (curr && curr->value != val)
    {
        prev = curr;
        curr = curr->next;
    }
    if (!curr)
    {
        printf("Value %d not found.\n", val);
        return head;
    }
    if (!prev)
        head = curr->next;
    else
        prev->next = curr->next;
    free(curr);
    return head;
}

void clearList(ListNode *head)
{
    while (head)
    {
        ListNode *tmp = head;
        head = head->next;
        free(tmp);
    }
}

/* ------------ Binary Search Tree ------------ */
typedef struct TreeNode
{
    int value;
    struct TreeNode *left, *right;
} TreeNode;

TreeNode *createTreeNode(int val)
{
    TreeNode *node = malloc(sizeof(TreeNode));
    node->value = val;
    node->left = node->right = NULL;
    return node;
}

TreeNode *insertBST(TreeNode *root, int val)
{
    if (!root)
        return createTreeNode(val);
    if (val < root->value)
        root->left = insertBST(root->left, val);
    else
        root->right = insertBST(root->right, val);
    return root;
}

void preorderTraversal(TreeNode *root)
{
    if (root)
    {
        printf("%d ", root->value);
        preorderTraversal(root->left);
        preorderTraversal(root->right);
    }
}

void inorderTraversal(TreeNode *root)
{
    if (root)
    {
        inorderTraversal(root->left);
        printf("%d ", root->value);
        inorderTraversal(root->right);
    }
}

void destroyTree(TreeNode *root)
{
    if (!root)
        return;
    destroyTree(root->left);
    destroyTree(root->right);
    free(root);
}

/* ------------ Main Menu ------------ */
int main()
{
    int choice;
    ListNode *listHead = NULL;
    TreeNode *treeRoot = NULL;

    do
    {
        printf("\n--- Data Structure Menu ---\n");
        printf("1. Append to Linked List\n");
        printf("2. Display Linked List\n");
        printf("3. Delete from Linked List\n");
        printf("4. Insert into Binary Tree\n");
        printf("5. Preorder Tree Traversal\n");
        printf("6. Inorder Tree Traversal\n");
        printf("0. Quit\n");
        printf("Your selection: ");
        scanf("%d", &choice);

        int num;
        switch (choice)
        {
        case 1:
            printf("Enter integer to append: ");
            scanf("%d", &num);
            listHead = appendNode(listHead, num);
            break;
        case 2:
            printList(listHead);
            break;
        case 3:
            printf("Enter integer to remove: ");
            scanf("%d", &num);
            listHead = removeNode(listHead, num);
            break;
        case 4:
            printf("Enter integer to insert into tree: ");
            scanf("%d", &num);
            treeRoot = insertBST(treeRoot, num);
            break;
        case 5:
            printf("Preorder: ");
            preorderTraversal(treeRoot);
            printf("\n");
            break;
        case 6:
            printf("Inorder: ");
            inorderTraversal(treeRoot);
            printf("\n");
            break;
        case 0:
            clearList(listHead);
            destroyTree(treeRoot);
            printf("Program terminated.\n");
            break;
        default:
            printf("Invalid choice, please try again.\n");
        }
    } while (choice != 0);

    return 0;
}
