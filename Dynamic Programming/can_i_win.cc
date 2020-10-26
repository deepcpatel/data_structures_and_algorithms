// Link: https://leetcode.com/problems/can-i-win/

/*
Explanation: (By Other)
My Thinking process

Like other game problem, this problem obviously should use dp. But how can we define the dp state? First, we can easily come out dp[target][state], 
that means when we face target and current state can I win. Second, how to present the state? We should realize state represent the usage of choosable 
integer. From description of this problem, we know the choosable integer is equal or less than 20 and it can't be re-used. Okay, hashmap comes to mind.
So the current problem is how to make a connection between hashmap and state. Up to this point, we find this is actually a TSP DP problem. Because the 
choosable integers is equal to or less than 20, we can use a integer instead of hashmap to represent the state(a integer has 32 bits, each bit represent 
the usage of its index).

For example:
0000 0000 0000 0000 0000 0000 0010 0010: binary form of 34, it means we have already used 1 and 5.
And now, we want to use numer 3 to make a try, it becomes:
0000 0000 0000 0000 0000 0000 0010 0110: actually, it is 34 ^ (1 << 2).
So if the current state is chs and we want to try number i + 1, next state is chs ^ (1 << i).

Further more, we find a chs can only correspond to a target, because when we try number i + 1, next target will be target - (i + 1).That means, chs ^ (1 << i) 
only correspond to target - (i + 1), won't be any others. So we need not use target, finally the dp state is dp[chs], it means if current usage of choosable 
integers is chs can I win.

The next thing is easy, if we can win, that means when we choose a integer the next turn's person can't win.

class Solution {
    public boolean canIWin(int maxChoosableInteger, int desiredTotal) {
        if (desiredTotal <= 0) return true;
        // 1 + 2 + ... + maxChoosableInteger < desiredTotal means can't reach to desiredTotal
        if (maxChoosableInteger * (maxChoosableInteger + 1) / 2 < desiredTotal) return false;
        int[] dp = new int[1 << maxChoosableInteger];
        return dfs(dp, 0, maxChoosableInteger, desiredTotal);
    }
    
    public boolean dfs(int[] dp, int chs, int max, int target) {
        // target <= 0 means the prior one wins
        if (target <= 0) return false;
        if (dp[chs] != 0) return dp[chs] == 1;
        boolean win = false;
        for (int i = 0; i < max; i++) {
            // i + 1 not use
            if ((chs & (1 << i)) == 0) {
                // thers is a trick: short circuit, when win is true, the next dfs won't be invoke
                win = win || !dfs(dp, chs ^ (1 << i), max, target - i - 1);
            }
        }
        dp[chs] = win ? 1 : -1;
        return win;
    }
}
*/

class Solution
{
    public:
        boolean canIWin(int maxChoosableInteger, int desiredTotal) 
        {
            if (desiredTotal <= 0)
                return true;

            // 1 + 2 + ... + maxChoosableInteger < desiredTotal means can't reach to desiredTotal
            if (maxChoosableInteger * (maxChoosableInteger + 1) / 2 < desiredTotal)
                return false;

            int[] dp = new int[1 << maxChoosableInteger];

            return dfs(dp, 0, maxChoosableInteger, desiredTotal);
        }
    
        boolean dfs(int[] dp, int chs, int max, int target)
        {
            // target <= 0 means the prior one wins
            if (target <= 0)
                return false;

            if (dp[chs] != 0)
                return dp[chs] == 1;

            boolean win = false;
            
            for (int i = 0; i < max; i++)
            {
                // i + 1 not use
                if ((chs & (1 << i)) == 0)
                {
                    // thers is a trick: short circuit, when win is true, the next dfs won't be invoke
                    win = win || !dfs(dp, chs ^ (1 << i), max, target - i - 1);
                }
            }
            
            dp[chs] = win ? 1 : -1;
            return win;
        }
}
