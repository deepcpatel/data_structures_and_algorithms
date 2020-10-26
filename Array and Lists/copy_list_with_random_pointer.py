# Link: https://leetcode.com/problems/copy-list-with-random-pointer/

"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        temp, head2, temp2 = head, None, None
        node_dict = {}
        
        while temp != None:
            if temp2 == None:
                head2 = Node(temp.val)
                temp2 = head2
            else:
                temp2.next = Node(temp.val)
                temp2 = temp2.next;
            
            node_dict[temp] = temp2     # Storing References
            temp = temp.next
        
        temp, temp2 = head, head2
        
        while temp != None:
            if temp.random == None:
                temp2.random = None
            else:
                temp2.random = node_dict[temp.random]
            temp = temp.next
            temp2 = temp2.next
        return head2