#!/usr/bin/python3

def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): List of coin values.
        total (int): The total amount to be made with the coins.

    Returns:
        int: The fewest number of coins needed to make the total.
    """
    if total <= 0:
        return 0

    # Initialize the dp array with infinity
    dp = [float('inf')] * (total + 1)

    # Base case
    dp[0] = 0

    # Fill the dp array
    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
