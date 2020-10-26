# Link: https://leetcode.com/problems/data-stream-as-disjoint-intervals/

'''
Approach:
Link: https://leetcode.com/problems/data-stream-as-disjoint-intervals/discuss/513717/Python3-or-Simple-O(n)-addNum-and-O(1)-getNum-with-follow-up-answered

Time Complexity :

addNum : O(n)

getIntervals : O(1)

Space Complexity : O(n)

In this approach, we save all the intervals in their raw format i.e we are optimizing for getIntervals.
We internally represent the intervals as a list of intervals (as expected in the getIntervals. Initially this will be an empty list i.e self._X = [].

When we invoke a call to addNum, we first do a binary search of [val] on the intervals self._X. i.e idx = bisect(self._X, [val]). Our goal here is to find multiple things based on idx. Let's list them

i. We have to find if the leftmost bound for this val i.e as seen to the left, can be it added to an existing interval or does it warrant a new interval (keep in mind, we are only looking to the left). It warrants a new interval iff, idx is 0 (this means that there is no interval smaller than val) OR if the next smaller interval's end + 1 is smaller than val. .

Examples

    self._X = [1,1], [4,4], [10,12] and val = 0 .. this gives idx = 0 and we have to create a new interval for this at 0 such as that self._X = [[0,0, [1,1],[4,4], [10,12]]

    If self._X = [1,1], [4,4], [10,12] and val = 6, then idx = 2. But we see that the interval at idx-1 i.e [4,4]'s end value + 1 is smaller than val. This we cannot touch any existing interval.

In both these cases, the starting index as seen to the left is idx (referred to as l_idx going forward) i.e we cannot touch/extend the interval at position idx-1. Correspondingly, the value is val(referred to as l_val going forward). If these conditions do not meet, we can extend the interval on the left i.e

Example if self._X = [1,1], [4,4], [10,12] and val = 5, then idx=2 as well but the interval on the left's end value 4 is just 1 smaller than val, so it can be extended. In cases like these, l_idx will be idx and l_val will be val.

ii. Similar to what we did for left side of self._X, we have to do it for right side as well. If the idx is equal to length of self._X (i.e if it's greater than the last interval), or if the interval to the right's start value -1 is greater than the val, then it warrant's a new interval as seen from the right. Only additionaly care we have to take is consider the element on the left's end range as well as bisect does not respect the end of the interval. This is the reason why we do r_val = max(val, self._X[idx-1][1] if idx > 0 else -float('inf')). If it can extend the interval on the right, we simply take r_idx to idx+1 and r_val to be the end of interval on the right. The examples for these can be built similar to the case (i)

Finally, we update the part of the array where we have to insert the new interval as self._X[l_idx:r_idx] = [[l_val, r_val]]

For getIntervals, we don't have to do any work as self._X already stores the intervals.

W.r.t to the follow up Q. this type of arrangement works well because we aggressively merge the intervals as the time for addNum is O(n) and we should strive to keep n as small as we can.
'''

from bisect import bisect

class SummaryRanges(object):

    def __init__(self):
        self.X = []

    def addNum(self, val):
        if len(self.X) == 0:
            self.X.append([val, val])
        else:
            idx = bisect(self.X, [val])
            
            if idx == 0 or self.X[idx-1][1] + 1 < val:  # We have to create new tuple
                lidx = idx
                lval = val
            else:           # We can modify existing tuple
                lidx = idx-1
                lval = self.X[idx-1][0]
                
            if idx == len(self.X) or self.X[idx][0]-1 > val:
                ridx = idx
                rval = max(val, self.X[idx-1][1] if idx > 0 else -float('inf'))
            else:
                ridx = idx+1
                rval = self.X[idx][1]
            
            self.X[lidx:ridx] = [[lval, rval]]
    def getIntervals(self):
        return self.X
    
# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
