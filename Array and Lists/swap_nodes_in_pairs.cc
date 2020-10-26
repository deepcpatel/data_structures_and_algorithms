// Link: https://leetcode.com/problems/swap-nodes-in-pairs/

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
        ListNode* swapPairs(ListNode* head)
        {
            ListNode *temp = head, *prev = head, *t1 = NULL;
            int counter = 0;
            
            if(head == NULL)
            {
                return head;
            }
            
            while(temp!= NULL)
            {
                if(temp->next == NULL)
                {
                    return head;
                }
                
                if(counter%2==0)
                {
                    if(temp == head)
                    {
                        t1 = temp->next;
                        temp->next = t1->next;
                        t1->next = temp;
                        head = t1;
                        counter++;
                    }
                    else
                    {
                        prev->next = temp->next;
                        temp->next = temp->next->next;
                        prev->next->next = temp;
                        counter++;
                    }
                }
                counter++;
                prev = temp;
                temp = temp->next;
            }
            return head;
        }
};