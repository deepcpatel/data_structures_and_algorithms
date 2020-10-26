# Link: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
 
'''
# Approach : Inorder Simulation
# Original Solution Article: https://leetcode.com/articles/convert-sorted-list-to-binary-search-tree/

Intuition

As we know, there are three different types of traversals for a binary tree:

    Inorder
    Preorder and
    Postorder traversals.

The inorder traversal on a binary search tree leads to a very interesting outcome.

Elements processed in the inorder fashion on a binary search tree turn out to be sorted in ascending order.

The approach listed here make use of this idea to formulate the construction of a binary search tree. The reason we are able to use this idea in this problem is because we are given a sorted linked list initially.

Before looking at the algorithm, let us look at how the inorder traversal actually leads to a sorted order of nodes' values.

The critical idea based on the inorder traversal that we will exploit to solve this problem, is:

We know that the leftmost element in the inorder traversal has to be the head of our given linked list. Similarly, the next element in the inorder traversal will be the second element in the linked list and so on. This is made possible because the initial list given to us is sorted in ascending order.

Now that we have an idea about the relationship between the inorder traversal of a binary search tree and the numbers being sorted in ascending order, let's get to the algorithm.

Algorithm

Let's quickly look at a pseudo-code to make the algorithm simple to understand.

➔ function formBst(start, end)
➔      mid = (start + end) / 2
➔      formBst(start, mid - 1)
➔
➔      TreeNode(head.val)
➔      head = head.next
➔       
➔      formBst(mid + 1, end)
➔

Iterate over the linked list to find out it's length. We will make use of two different pointer variables here to mark the beginning and the end of the list. Let's call them start and end with their initial values being 0 and length - 1 respectively.
Remember, we have to simulate the inorder traversal here. We can find out the middle element by using (start + end) / 2. Note that we don't really find out the middle node of the linked list. We just have a variable telling us the index of the middle element. We simply need this to make recursive calls on the two halves.
Recurse on the left half by using start, mid - 1 as the starting and ending points.

The invariance that we maintain in this algorithm is that whenever we are done building the left half of the BST, the head pointer in the linked list will point to the root node or the middle node (which becomes the root). So, we simply use the current value pointed to by head as the root node and progress the head node by once i.e. head = head.next
We recurse on the right hand side using mid + 1, end as the starting and ending points.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def half_itr(self, start, end):
        tree_node = None
        
        if start<=end:
            mid = (start + end)//2
            n1 = self.half_itr(start, mid-1)

            tree_node = TreeNode(self.head.val)
            self.head = self.head.next

            n2 = self.half_itr(mid+1, end)

            tree_node.left = n1
            tree_node.right = n2
        
        return tree_node
        
    def sortedListToBST(self, head):
        self.head, temp = head, head
        list_length = 0
        
        while temp != None:
            temp = temp.next
            list_length += 1    
        
        return self.half_itr(0, list_length-1)