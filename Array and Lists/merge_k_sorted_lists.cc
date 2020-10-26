// Link: https://leetcode.com/problems/merge-k-sorted-lists/

// Approach: Initially iterated overall the k lists and merged them one by one using "merge2list" function. However, I later
// read that one can perform divide and conquer method. Means divide the array of list heads into 2 parts and merge them one
// by one. Eg: list of pointer heads [l1, l2, l3, l4, l5, l6], we divide then as [l1, l2, l3] and [l4, l5, l6]. We further divide
// each of them as [l1, l2], [l3], [l4, l5], [l6]. Now we merge [l1, l2] to form [la], [l4, l5] to form [lb]. We merge [la] and
// [l3] to form [lc] and [lb] and [l6] to form [ld]. And finally we merge [lc] and [ld] to form final merged list. Complexity:
// O(N*log(k)). Here N is number of node in each list and k is number of list in total. The previous approach takes O(N*k) time.

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
    private:
        ListNode* merge2list(ListNode* head, ListNode* list)
        {
            ListNode *p1 = head, *p2 = list, *prev_p1 = NULL, *temp = NULL;
            
            if(head == NULL)
            {
                head = list;
                return head;
            }
            
            while(p1 != NULL && p2 != NULL)
            {
                if(p1->val >= p2->val)
                {
                    temp = p2;
                    p2 = p2->next;
                        
                    temp->next = p1;
                    
                    if(p1 == head)
                    {
                        head = temp; 
                    }
                    else
                    {
                        prev_p1->next = temp;
                    }
                    prev_p1 = temp;
                }
                else
                {
                    prev_p1 = p1;
                    p1 = p1->next;
                }
            }
            
            if(p1 == NULL)
            {
                prev_p1->next = p2;
            }
            return head;
        }
        
        ListNode* divide_conquer(int start, int end, vector<ListNode*>& lists)
        {
            if(start == end)
            {
                return lists[start];
            }
            else
            {
                int div = (start+end)/2;
                return merge2list(divide_conquer(start, div, lists), divide_conquer(div+1, end, lists));   
            }
        }
    
    public:
        ListNode* mergeKLists(vector<ListNode*>& lists)
        {
            int n = lists.size();
            
            if(n == 0)
            {
                return NULL;
            }
            return divide_conquer(0, n-1, lists);
        }
};