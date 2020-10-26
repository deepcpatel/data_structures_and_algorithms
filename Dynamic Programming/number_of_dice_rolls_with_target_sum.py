# Link: https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

# Approach: Define remaining number of dice left, and target sum left so far. Make a function which recursively reaches closer to target by subtracting the dice numbers from it and consequently
# number of available dices decreases. Now, at each die roll, you could have either one possibility, either target is greater than max_die_num*num_dice, which is unfeasible, thus don't move further
# and return 0 possibilities, or target == 0 and remaining_dice == 0. In which case, you return 1 successfull possibility or finally target > 0 and remaining_dice > 0. In that case role another die
# and subtract the facevalue from target and recursively get successful possibility. At each recursion, save total successful possibilities for each (remaining_dice, target) pair for memoization.

class Solution(object):
    def rolls(self, target, remaining_dice, dice_size):
        tup = (remaining_dice, target)  # Current state
        
        if tup not in self.count_dict:
            count = 0
            
            if target > remaining_dice*dice_size:       # Infeasible, target is greater than max possible sum
                pass
            elif target == 0 and remaining_dice == 0:   # Target already achieved
                count = 1        
            elif target > 0 and remaining_dice > 0:     # Target is achieveable and thus roll a die and go to next step
                for i in range(1, dice_size+1):
                    count += self.rolls(target-i, remaining_dice-1, dice_size)
            
            self.count_dict[tup] = count    # Memoization
                    
        return self.count_dict[tup] # Return final result
        
    def numRollsToTarget(self, d, f, target):
        self.count_dict = {}          
        return self.rolls(target, d, f) % (10**9 + 7)   # Modulo (Note: don't do num % (10^9 + 7). Its XOR operation in Python)