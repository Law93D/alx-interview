0x08. Making Change
Algorithm
Python

Problem Overview
Given a list of coin denominations and a total amount, determine the minimum number of coins needed to make up that amount. If it is not possible to make the exact amount, return -1. If the amount is 0 or less, return 0.

Concepts
Greedy Algorithms: These algorithms build up a solution piece by piece, always choosing the next piece that offers the most immediate benefit. For the coin change problem, the greedy approach works well if the coin denominations are such that it always yields an optimal solution (e.g., US coins). However, for arbitrary denominations, it might not work.

Dynamic Programming: This approach solves problems by breaking them down into simpler subproblems. It is effective for the coin change problem when the greedy approach might not work. It involves creating a table where each entry represents the minimum number of coins needed to make up that amount.

Approach
Greedy Algorithm
Sort the coins in descending order.
Try to use the largest coin denomination as much as possible, then move to the next largest coin, and so on.
This approach might fail for some denominations, so it's important to consider dynamic programming as well.
Dynamic Programming
Create a list dp where dp[i] represents the minimum number of coins needed to make amount i.
Initialize dp[0] to 0 (since no coins are needed to make 0).
For other amounts, initialize dp[i] to infinity (or a large number).
Update dp based on previously computed values, using the relation:

dp[i]=min(dp[i],dp[i−coin]+1)

for each coin.
