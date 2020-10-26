# Link: https://leetcode.com/problems/reveal-cards-in-increasing-order/

# Approach: Reverse simulate the steps given. Sort the given deck array. Extract elements from tail and insert into a new deque() at beginning. But, before each insertion rotate the dequq() in
# right direction. Do this till you reach beginning of the deck and return the deque.

from collections import deque

'''
deque.rotate() works similar to following

def rotate(ans_array):
    if ans_array:
        el = ans_array.pop()
        ans_array.appendleft(el)
    return ans_array
'''

class Solution:
    def deckRevealedIncreasing(self, deck):
        self.ans_array = deque()
        deck.sort()
        
        for i in range(len(deck)-1, -1, -1):
            elem = deck[i]
            
            self.ans_array.rotate()
            self.ans_array.appendleft(elem)

        return self.ans_array