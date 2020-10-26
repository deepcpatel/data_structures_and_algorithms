// Link : https://practice.geeksforgeeks.org/problems/check-for-bst/1

#include <bits/stdc++.h>
using namespace std;
/* A binary tree node has data, pointer to left child
   and a pointer to right child */
struct Node 
{
    int data;
    Node* right;
    Node* left;
    
    Node(int x)
    {
        data = x;
        right = NULL;
        left = NULL;
    }
};
/* Returns true if the given tree is a binary search tree
 (efficient version). */
bool isBST(struct Node*);
bool check_bst(struct Node*);

int isBSTUtil(struct Node* node, int min, int max);
/* Driver program to test size function*/
int main()
{
    int t;
    struct Node *child;
    scanf("%d", &t);
    while (t--)
    {
        map<int, Node*> m;
        int n;
        scanf("%d",&n);
        struct Node *root = NULL;
        while (n--)
        {
            Node *parent;
            char lr;
            int n1, n2;
            scanf("%d %d %c", &n1, &n2, &lr);
            if (m.find(n1) == m.end())
            {
                parent = new Node(n1);
                m[n1] = parent;
                if (root == NULL)
                    root = parent;
            }
            else
                parent = m[n1];
            child = new Node(n2);
            if (lr == 'L')
                parent->left = child;
            else
                parent->right = child;
            m[n2]  = child;
        }
        cout << isBST(root) << endl;
    }
    return 0;
}

/*Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above.*/

/* A binary tree node has data, pointer to left child
   and a pointer to right child  
struct Node {
    int data;
    Node* left, * right;
}; */

// Note: Iperformed Inorder traversal and made sure that the previous element is always smaller than next element by using
// maxi variable to keep track of maximum element till now, otherwise it is not BST

int maxi = -1;

bool check_bst(struct Node* root)
{
    if(root != NULL)
    {
        if(!check_bst(root->left))
        {
            return false;
        }
        if(root->data > maxi)
        {
            maxi = root->data;
        }
        else
        {
            return false;
        }
        if(!check_bst(root->right))
        {
            return false;
        }
        return true;
    }
    return true;
}

bool isBST(struct Node* root) 
{
    maxi = -1;
    return check_bst(root);
}