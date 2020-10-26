# Link: https://leetcode.com/discuss/general-discussion/475924/My-experience-and-notes-for-learning-DP
''' 
A littile bit of my history of learning DP

DP has always been an obstacle when preparing for interviews. For me it is one of the hardest topic. There were several times in the past that I tried to master it, but all attempts
failed. Either because I could not find good resources, or because I did not have enough time to really dive into it, have a lot of practice, and identify different patterns. To tell
the truth, I even feared that I would never be able to understand it well.

This winter I had another attempt, and made up my mind to grasp the techique. I solved/read 45 DP problems of different patterns in 4 days (yes, you might think that is quite slow).
At the begining, I struggled as much as all my previous attempts, but slowly I found I am getting better and I start to be able to think in the DP-way. Today I solved several problems
independently, with memoization and tabulation and even space optimizations, I think I am finally understand this category of problem. The process is hard and frustrating, I know! Thus,
I want to share my experience so that you might get some help.

Resources / My way of learning

The resources I recommend for learning DP. I use them in the order as listed.

  1.Dynamic Programming [https://www.geeksforgeeks.org/dynamic-programming/]
    If you are not familiar with DP yet, there's no point in diving into Leetcode problems directly. The explanation of Basic Concepts is very clear. You could also try the first
    several basic problems to have a taste of DP.

  2.Some typical/famous DP problems (OPTIONAL)
    I would recommend you to try to read (you might not be able to solve it, which is totally fine!) several DP problems to have a tiny peek into DP. You do not really need try to
    identify the pattern or memorize the solution. Just to get some feeling about DP. You may not need it, but this is helpful for me. I recommend Longest Common Subsequence, 0/1 
    Knapsack, Climbing Stairs.

  3.From good to great. How to approach most of DP problems. [https://leetcode.com/problems/house-robber/discuss/156523/From-good-to-great.-How-to-approach-most-of-DP-problems.]
    A very good illustration of the motivation behind DP. DP is essentially an optimizaton for pure recursion. If we are solving overlapping subproblems, we can save result to subproblems,
    we avoid repeated computations. This also shows the implementaion: how to convert recursion code to memoization, and to tabulation. For me, it is very helpful.

  4.Dynamic Programming Patterns (MUST READ) [https://leetcode.com/discuss/general-discussion/458695/dynamic-programming-patterns]
    Best post on DP ever! The summarized pattern, problem statement and approach are very helpful. I would say my previous efforts of learning DP brings me at point 3 (which is not easy as
    to understand the motivation and the implementation of DP are hard already!). For the last 4 days, I spent most of my time working on problems, grouped by patterns, mentioned in the post.
    All my previous nightmares on DP gone! You cannot afford to miss this post!
    Other notes I made when reading the post:

        -> The statement, approach and code snippet for each pattern in the original post is helpful and comprehensive.

        -> Pattern 1 and 2 are kind of similar.

        -> One hint of pattern 3 problems is that they usually involve a list/array of numbers, either explicitly or implicity, like in 1130, 96 and 1039.

        -> DP on strings is usually, if not always, done by comparing two chars at a time.

  5.Back to Back SWE [https://www.youtube.com/channel/UCmJz2DV1a3yfgrR7GqRtUUA]
    Video explanation on many algorithm problems, including DPs. Detailed, slow and clear. There are several sentences from this guy, which I always remind myself when solving DP problems:
    "DP is not about building dp table. It is about identifying subproblem, and caching answers to subproblems in order to solve the original problem".

DP implementation tips

With the following tips in mind, the implementation for memoization and tabulation is trivial!

    The most important step, and also the first step, in solving DP problem is to identify the recursive equation. Then the implementation just follows recursion -> memoization -> tabulation.

    For tabulation, every entry, like dp[i][j], that could be used must be filled. However for memoization, the value might not exist in the dp table because you can directly provide it in
    the return value of solve(mem, i, j).

    It is easy to convert recursion to memoization. For tabulation, draw graph to see clearly how the dp table is filled up(Lower rows to higher rows, or reverse? Left to right, or reverse?
    Upper left to lower right, or reverse?). The direction of filling up the dp table affects the values of the loop variables used in tabulation. A common error occurs when the for loop does
    not conform to the way in which the dp table is filled.

Two styles of dp table

Quite commonly, dp tables are built such that dp[m][n] is the ultimate solution. However, there are also a number of DP problems where a variable is updated when building the dp table and the
variables contains the final answer(e.g., 647).

Last note: keeps practicing! I think I would review those problems for several rounds in the coming weeks, just to keep my self comfortable with DP. When practicing, try to solve with recursive,
memoization, tabulation, and even optimize the space when possible.
'''