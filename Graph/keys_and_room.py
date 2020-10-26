# Link: https://leetcode.com/problems/keys-and-rooms/

# Approach: Standard DFS. Visit each room starting from 0. From each room obtain keys and store them into stack. During each iteration, visit the rooms after popping keys from the stack.
# After each visit mark the rooms as visited by adding [-1] and never visit them again

class Solution(object):
    def canVisitAllRooms(self, rooms):
        N, stack = len(rooms)-1, []
        
        # Emptying the first Room
        stack.extend(rooms[0])
        rooms[0] = [-1]         # Appending -1 marks visited
        
        # DFS
        while len(stack)>0:
            i = stack.pop()     # Popping each room key and visiting it
            
            if len(rooms[i]) == 0 or rooms[i][0] != -1:     # Visit only originally empty rooms or the ones never visited
                stack.extend(rooms[i])  # Adding new rooms keys to the stack
                rooms[i] = [-1]         # Marking room as visited by apppending -1 (even empty roome will be marked visited)
                N -= 1                  # Decreasing counts for each room visited
        
        return N == 0