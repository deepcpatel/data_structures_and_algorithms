# Link: https://leetcode.com/problems/brick-wall/

# Approach: We have to find minimum bricks that will be crossed. For that, we have to find a line that passes through maximum number of bricks without crossing them
# for this, we calculate the sum of each brick length in each row of wall and increment counter to 1 (i.e. brick_count[sum] += 1) which indicates that this brick configuration
# exist in a row of the wall. We will select the configuration (sum) with highest number of count (rows) in hashtable (i.e. max_v = max(max_v, brick_count[s])). Thus, those
# number of rows will be passed without crossing the linr and the remaining (total_rows-max_v) will be crossed thus it is answer.


class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        
        rows = len(wall)
        
        if rows == 0:
            return 0
        
        brick_count = {}
        max_v = 0
        
        for r in range(rows):
            s = 0
            for l in range(len(wall[r])-1):
                s += wall[r][l]
                brick_count[s] = brick_count.get(s, 0) + 1
                max_v = max(max_v, brick_count[s])
        return rows-max_v