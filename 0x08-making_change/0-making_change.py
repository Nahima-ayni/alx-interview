#!/usr/bin/python3
"""Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total"""

def makeChange(coins, total):
    # If total is 0 or less, no coins are needed
    if total <= 0:
        return 0
    
    # Initialize dp array with a large number (infinity) 
    # dp[i] represents the minimum number of coins needed for amount i
    dp = [float('inf')] * (total + 1)
    
    # Base case: 0 coins are needed to make the amount 0
    dp[0] = 0
    
    # Iterate over all amounts from 1 to total
    for amount in range(1, total + 1):
        # Try every coin denomination
        for coin in coins:
            if coin <= amount:  # Coin must be less than or equal to the amount
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    # If dp[total] is still infinity, it means we couldn't form the total with given coins
    return dp[total] if dp[total] != float('inf') else -1

