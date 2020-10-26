# Link: https://www.geeksforgeeks.org/tree-isomorphism-problem/

'''
Given two Binary Trees. Check whether they are Isomorphic or not.

Example 1:

Input:
 T1    1     T2:   1
     /   \        /  \
    2     3      3    2
   /            /
  4            4
Output: No

Example 2:

Input:
T1    1     T2:    1
    /  \         /   \
   2    3       3     2
  /                    \
  4                     4
Output: Yes

Your Task:
You don't need to read input or print anything. Your task is to complete the function isIsomorphic() that takes the root nodes of both the Binary Trees as its input and returns True if the two trees are isomorphic. Else, it returns False. (The driver code will print Yes if th returned values is true, otherwise false.)

Note: 
Two trees are called isomorphic if one of them can be obtained from other by a series of flips, i.e. by swapping left and right children of a number of nodes. Any number of nodes at any level can have their children swapped. Two empty trees are isomorphic.
For example, following two trees are isomorphic with following sub-trees flipped: 2 and 3, NULL and 6, 7 and 8.
ISomorphicTrees

Expected Time Complexity: O(min(M,N)) where M and N are the sizes of the two trees.
Expected Auxiliary Space: O(min(H1,H2)) where H1 and H2 are the heights of the two trees.

Constraints:
1<=Number of nodes<=105
'''

# Approach: Resurcively call the isIsomorphic function to check whether each subtree of the tree is isomorphic or not. At each call Return false if Node values are not same. Moreover perform and operation
# between (root1.data ==  root2.data) and isomorphic check of subtrees. To check whether subtree are isomorphic, we have two cases:
# (1). Either nodes are not flipped, thus we will do ((isIsomorphic(root1.left, root2.left) and isIsomorphic(root1.right, root2.right)). Or (2). If nodes are flipped, then we will do
# (isIsomorphic(root1.left, root2.right) and isIsomorphic(root1.right, root2.left)).

# Return True if the given trees are isomotphic. Else return False.
def isIsomorphic(root1, root2): 
    
    if root1 == root2 == None:
        return True
    elif root1 == None or root2 == None:
        return False
    else:
        return (root1.data == root2.data) and \
                ((isIsomorphic(root1.left, root2.left) and \
                isIsomorphic(root1.right, root2.right)) or \
                (isIsomorphic(root1.left, root2.right) and \
                isIsomorphic(root1.right, root2.left)))