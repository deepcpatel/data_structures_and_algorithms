// Link: https://leetcode.com/problems/add-two-numbers/

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
        ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) 
        {
            int carry = 0, sum;
            ListNode *n1 = l1, *n2 = l2, *prev1, *prev2;
            
            while(n1 != NULL && n2 != NULL)
            {
                sum = n1->val + n2->val + carry;
                    
                carry = sum/10;
                sum = sum%10;
                
                n1->val = sum;
                n2->val = sum;

                prev1 = n1;
                prev2 = n2;
                
                n1 = n1->next;
                n2 = n2->next;
            }
            
            if(n1 == NULL && n2 == NULL)
            {
                if(carry != 0)
                {
                    prev1->next = new ListNode(carry);
                }
                return l1;
            }
            else if(n2 == NULL)
            {
                while(n1 != NULL && carry != 0)
                {
                    sum = n1->val + carry;
                    
                    carry = sum/10;
                    sum = sum%10;

                    n1->val = sum;
                    
                    prev1 = n1;
                    n1 = n1->next;
                }
                
                if(carry != 0)
                {
                    prev1->next = new ListNode(carry);
                }
                return l1;
            }
            else
            {
                while(n2 != NULL && carry != 0)
                {
                    sum = n2->val + carry;
                    
                    carry = sum/10;
                    sum = sum%10;

                    n2->val = sum;
                    
                    prev2 = n2;
                    n2 = n2->next;
                }
                
                if(carry != 0)
                {
                    prev2->next = new ListNode(carry);
                }
                return l2;
            }
        }
};