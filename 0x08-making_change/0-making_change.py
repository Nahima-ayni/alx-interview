#!/usr/bin/python3
"""Given a pile of coins of different values,
    determine the fewest number of coins needed to meet a given amount total"""

def makeChange(coins, total):
    # If total is 0 or less, no coins are needed
    if total <= 0:
        return 0
    
    # Sort coins in descending order to attempt larger coins first
    coins.sort(reverse=True)
    
    # Initialize dp array with infinity (impossible to reach amount initially)
    dp = [float('inf')] * (total + 1)
    
    # Base case: 0 coins are needed to make the amount 0
    dp[0] = 0
    
    # Iterate over all amounts from 1 to total
    for amount in range(1, total + 1):
        # Try every coin denomination
        for coin in coins:
            if coin > amount:
                continue  # Skip if the coin is larger than the current amount
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
            # Optimization: If we find an exact match, break early
            if dp[amount] == dp[amount - coin] + 1:
                break
    
    # If dp[total] is still infinity, it means we couldn't form the total with given coins
    return dp[total] if dp[total] != float('inf') else -1

