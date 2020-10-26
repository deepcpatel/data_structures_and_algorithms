# Link: https://leetcode.com/problems/lru-cache/

# Approach: Use Dictionary for O(1) retrieval. Store key-value pair in the dictionary for fast retrieval. However, for LRU cache, you must also
# Keep record of lest used locations. For that you can use doubly linked list. For new value insert nodes in the linked list and store in dictionary (instead of just value)
# with corresponding key. Now, when you want to update the linked list by inserting or removing a node corresponding to a key, simply retrieve the node  from the dictionary
# and update the linked list as done in insert() and remove() function. The updated node will be removed from linked list and re-inserted at the end of the linkedlist since it is recently
# recently.

class Node():
    def __init__(self, value, key, left=None, right=None):
        self.val = value
        self.key = key
        self.left = left
        self.right = right
        
class doubly_linked_list():
    def __init__(self, capacity):
        self.head = None
        self.tail = None
        self.capacity = 0
        self.MAX_CAP = capacity
        
    def remove(self, node):
        if not node:
            return False
        
        left = node.left
        right = node.right
        
        node.left = None
        node.right = None
        
        if node == self.head:
            self.head = right
            
            if self.head:
                self.head.left = None
            
        if node == self.tail:
            self.tail = left
            
            if self.tail:
                self.tail.right = None
            
        if left:    
            left.right = right
        
        if right:
            right.left = left
        
        self.capacity -= 1
        return True
    
    def insert(self, node):
        r_node = False
        temp = None
        
        if self.capacity==self.MAX_CAP:
            temp = self.head
            r_node = self.remove(self.head)
            
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.left = self.tail
            node.right = None
            self.tail.right = node
            self.tail = node
        
        self.capacity += 1
        
        if r_node:
            return temp.key
        return None
            
class LRUCache(object):

    def __init__(self, capacity):
        self.key_val_d = {}
        self.dl_list = doubly_linked_list(capacity)
    
    def get(self, key):
        if key not in self.key_val_d:
            return -1
        else:
            self.dl_list.remove(self.key_val_d[key])
            self.dl_list.insert(self.key_val_d[key])
            return self.key_val_d[key].val

    def put(self, key, value):
        if key in self.key_val_d:
            self.key_val_d[key].val = value
            self.dl_list.remove(self.key_val_d[key])
            self.dl_list.insert(self.key_val_d[key])
        else:
            new_node = Node(value, key)
            self.key_val_d[key] = new_node
            
            r_key = self.dl_list.insert(new_node)
            if r_key:
                del self.key_val_d[r_key]
                
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)