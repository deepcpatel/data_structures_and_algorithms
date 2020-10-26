# Link: https://leetcode.com/problems/word-ladder/

# Approach: To find the distance between start and end word through the list, perform BFS through the list [Not DFS, I tried and failed]. What you have to do is that
# start from beginWord and search all the words from list which arr one edit away from beginWord. Add all those words to a queue and not again iterate over them to find 
# next set of one_edit words until you find the endWord or exhausted out of list. Now, at every iteration, you can check whether two words are one edit away or not. This will
# take O(m*n) time for n words in list each having m length [I tried and ime limit exceeds comes]. Other way is to generate all the possible edits (possible_words function) of
# currrent word with 1 character change at each position and check whether each new word exist in original list or not (using set for O(1) search). This will only take O(25*m)
# time. This way you check all the words and finally reach to endWord.   

from collections import deque

class Solution(object):
    
    def possible_words(self, word, w_set):
        ans_li = []
        
        for i in range(len(word)):
            for c in range(ord('a'), ord('z')+1):
                new_word = word[:i] + chr(c) + word[i+1:]
                
                if new_word in w_set:
                    ans_li.append(new_word)
                    w_set.remove(new_word)       
        return ans_li
    
    def calc_distance(self, bword, eword, w_list):
        wordq, w_set = deque([bword]), set(w_list)
        level = 1
        
        if eword not in w_set:
            return 0
        
        while len(wordq) != 0:
            q_len = len(wordq)
            
            for i in range(q_len):
                word = wordq.popleft()
                poss_li = self.possible_words(word, w_set)

                for w in poss_li:
                    if w == eword:
                        return level+1   
                    wordq.append(w)
            
            level += 1
        return 0
    
    def ladderLength(self, beginWord, endWord, wordList):
        if beginWord == endWord:
            return 1
        else:
            return self.calc_distance(beginWord, endWord, wordList)