// Link: https://leetcode.com/problems/reverse-nodes-in-k-group/

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
        ListNode* reverseKGroup(ListNode* head, int k)
        {
            ListNode *start = head, *end = head, *temp = NULL, *prev_node = NULL, *prev_head = head, *prev_prev_head = NULL;
            int counter = 0, t = 0;
            
            while(end != NULL || start != NULL)
            {
                if(start == end)
                {
                    if(t == 1)
                    {
                        head = temp;
                    }
                    
                    if(t>1)
                    {
                        prev_prev_head->next = temp;
                    }
                    
                    if(t>0)
                    {
                        prev_prev_head = prev_head;
                        prev_head = start;
                    }
                    
                    counter = k;
                    t++;
                }
                
                if(counter > 0)
                {
                    end = end->next;
                    temp = end;
                    counter--;
                    
                    if(counter > 0 && end == NULL)
                    {
                        break;
                    }
                }
                
                if(counter == 0)
                {
                    prev_node = start;
                    start = start->next;
                    prev_node->next = temp;
                    temp = prev_node;
                }
            }
            
            
            if(start == NULL && end == NULL)
            {
                if(t == 1)
                {
                    head = temp;
                }

                if(t>1)
                {
                    prev_prev_head->next = temp;
                }

                if(t>0)
                {
                    prev_prev_head = prev_head;
                    prev_head = start;
                }
            }
            
            return head;
        }
}; 
