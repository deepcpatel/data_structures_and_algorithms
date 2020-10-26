// Link: https://leetcode.com/problems/range-sum-of-bst/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution 
{   int sum = 0;
 
    public:
        int rangeSumBST(TreeNode* root, int L, int R)
        {
            if(root != NULL)
            {
                if(root->val>=L && root->val<=R)
                {
                    sum = sum + root->val;
                }
                
                if(root->val>L)
                {
                    rangeSumBST(root->left, L, R);
                }
                
                if(root->val<R)
                {
                    rangeSumBST(root->right, L, R);
                }
            }
            return sum;
        }
}; 
