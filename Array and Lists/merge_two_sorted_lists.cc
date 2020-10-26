// Link: https://leetcode.com/problems/merge-two-sorted-lists/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution 
{
    public:
        ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) 
        {
            ListNode *prev = NULL, *h1 = l1, *h2 = l2, *main = l1, *temp2 = NULL;
            
            if(l1 == NULL)
            {
                return l2;
            }
            
            if(l2 == NULL)
            {
                return l1;
            }
            
            while(h1 != NULL && h2 != NULL)
            {
                // cout<<h1->val<<" "<<h2->val<<"\n";
                if(h1->val > h2->val)
                {
                    if(h1 == l1)
                    {
                        temp2 = h2->next;
                        h2->next = h1;
                        prev = h2;
                        main = h2;
                        l1 = h2;
                        h2 = temp2;
                    }
                    else
                    {
                        temp2 = h2->next;
                        h2->next = h1;
                        prev->next = h2;
                        prev = h2;
                        h2 = temp2;
                    }
                }
                else
                {
                    prev = h1;
                    h1 = h1->next;
                }
            }
    
            if(h1 == NULL && h2 != NULL)
            {
                prev->next = h2;
            }
            return main;
        }
}; 
