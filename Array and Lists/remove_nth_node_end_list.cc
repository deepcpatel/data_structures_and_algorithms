// Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

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
        ListNode* removeNthFromEnd(ListNode* head, int n) 
        {
            ListNode *temp = head, *prev = head;
            int counter=0;
            
            while(temp!=NULL)
            {
                if(counter>=n+1)
                {
                    prev = prev->next;
                }
                temp = temp->next;
                counter++;
            }
            
            if(n>=counter)
            {
                return prev->next;
            }
            else
            {
                prev->next = prev->next->next;
            }
            
            return head;
        }
}; 
