# Link: https://leetcode.com/problems/airplane-seat-assignment-probability/

'''
# Approach: 
(0). Consider n seats in the plane

(1). Assume Passenger 1 arrives in the plane. He will select a random seat each with probability (1/n). Therefore probability of getting him correct seat (i.e. seat no. 1) is (1/n).

(2). Now assume Passenger 2 arrives. Whether he will get correct seat will depend on Passenger 1. Therefore not getting a correct seat 2 is with probability (1/n) [i.e. if 1 chooses seat 2 with 1/n].

(3). Now, Passenger 3's allocation will depend on Passenger 1 and 2. Passenger 3 will not get seat 3 if 1 directly chooses it with probability (1/n) or Passenger 2 chooses it with probability (1/n)*(1/n-1)) 
     [i.e. 1 randomly chooses 2's seat with (1/n) and 2 randomly chooses 3's seat with (1/n-1) probability].

(4). Similarly for Passenger 4, he will not get seats in following cases:
     (a). 1 randomly chooses seat 4 with (1/n) probability, or
     (b). 1 randomly choose seat 2 and passenger 2 randomly choose seat 4 with probability (1/n)*(1/(n-1)), or
     (c). 1 randomly choose seat 3 and passenger 3 randomly choose seat 4 with combined probability of (1/n)*(1/(n-2)), or
     (d). Passenger 1 choose seat 2 and passenger 2 randomly choose seat 3 and passenger 3 randomly choose seat 4 with probability (1/n)*(1/(n-1))*(1/(n-2)).
     These will combine to form (1/n) + (1/n)*(1/(n-1)) + (1/n)*(1/(n-2)) + (1/n)*(1/(n-1))*(1/(n-2)), total probability of 4 not getting seat 4.

(5). In general for n seats and passenger i (2 < i < n), i will not get seat i with probability:
     P(player i not getting seat i) = (1/n)*(1 + 1/(n-1))*(1 + 1/(n-2))*...*(1 + 1/(n-(i-2))).

(6). For player i == 2, P(player i not getting seat i) = (1/n)

(7). Therefore getting seat i is simply 1 - P(player i not getting seat i).

(8). Mathematically, for all values of n, player n will get seat n with probability 0.5 (check with different values of n above if you do not believe).
'''

# Long Answer:
class Solution(object):
    def nthPersonGetsNthSeat(self, n):
        """
        :type n: int
        :rtype: float
        """
        if n == 1:
            return 1
        
        prev = 1.0/n                    # Passenger 2
        
        for i in range(1, n-1):         # Passenger i
            prev *= (1.0 + 1.0/(n-i))
            
        return (1-prev) 

'''
# Short Answer:
class Solution(object):
    def nthPersonGetsNthSeat(self, n):
        return (1 if n == 1 else 0.5)
'''