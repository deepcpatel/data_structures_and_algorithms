# Link: https://leetcode.com/problems/minimum-cost-for-tickets/

''' 
# Others Approach: https://leetcode.com/problems/minimum-cost-for-tickets/solution/
# My Approach: Basically, lets's say at Day 1, we want to find that which ticket will yield lower value (either of Day 1 + all cost after that day, or a week and all the cost after one week or
one month and all the cost after one month). This is done recursively as in line 29. However, a day may not be in our travelling list 'days' on which we jumped after paying ticket, therefore
we go to immediate day after that day using year_days list (line 28). Basically, year_days for each day in it stores index to next immediate day in the 'days' list. 
'''

class Solution(object):
    def mincostTickets(self, days, costs):
        year_days = [-1]*366
        counter, i = 1, 0
        cost_ar = [-1]*len(days)
        
        while counter < 366:
            if counter > days[i]:
                i += 1
                if i == len(days):
                    break
            year_days[counter] = i
            counter += 1
        
        def recur(day):            
            if day > days[-1]:
                return 0
            
            idx = year_days[day]
            if cost_ar[idx] == -1:
                cost_ar[idx] = min(costs[0]+recur(days[idx]+1), costs[1]+recur(days[idx]+7), costs[2]+recur(days[idx]+30))
            return cost_ar[idx]
            
        return recur(1) 