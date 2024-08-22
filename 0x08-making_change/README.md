# README Notes: "0. Change Comes from Within" Project

## Overview
The "0. Change Comes from Within" project is a classic algorithmic problem where the goal is to determine the minimum number of coins required to make a given total amount using a list of available coin denominations. This problem can be solved using different algorithmic approaches, such as greedy algorithms and dynamic programming.

## Problem Statement
Given a total amount `n` and a list of coin denominations, the objective is to find the minimum number of coins required to make up the amount `n`. 

For example:
- **Input**: `n = 11`, `denominations = [1, 2, 5]`
- **Output**: `3` (Explanation: 11 = 5 + 5 + 1)

## Key Concepts and Strategies

### 1. **Greedy Algorithms**
A greedy algorithm builds up a solution step by step, always choosing the option that looks best at each step. In the context of the coin change problem, a greedy approach might work by always picking the largest denomination coin that is less than or equal to the remaining amount.

- **Advantages**: Greedy algorithms are usually faster because they do not explore all possibilities.
- **Limitations**: Greedy algorithms do not always produce the optimal solution, especially when the coin denominations do not allow for simple greedy choices (e.g., denominations like 1, 3, 4).

**Example**: If you have denominations [1, 3, 4] and you need to make 6, a greedy approach might choose two 3-coins, but the optimal solution is actually using a 4-coin and a 2-coin (from using dynamic programming).

### 2. **Dynamic Programming (DP)**
Dynamic programming provides a more comprehensive approach for solving optimization problems. It involves breaking down the problem into smaller, overlapping subproblems and solving them recursively or iteratively. DP is particularly useful when a greedy approach fails to provide the optimal solution.

- **Principle**: In DP, you store the results of subproblems in a table and reuse them to avoid redundant computations. This leads to a significant reduction in time complexity.
- **Optimal Substructure**: The problem can be divided into subproblems such that the solution to the main problem can be constructed from the solutions to the subproblems.
- **Overlapping Subproblems**: The same subproblems are solved multiple times, which makes it beneficial to cache solutions.

**DP Table Construction**: Create a table `dp[]` where `dp[i]` represents the minimum number of coins required to make up amount `i`. Initialize `dp[0] = 0` and fill the table using previously computed results.

**Example**:
For denominations [1, 2, 5] and an amount of 11, the DP table will look like this:
- `dp[0] = 0`
- `dp[1] = 1` (1 coin of 1)
- `dp[2] = 1` (1 coin of 2)
- `dp[3] = 2` (2 coins of 1 + 1 coin of 2)
- And so on...

### 3. **Algorithmic Complexity**
- **Greedy Approach**: Generally has a time complexity of `O(n)` if the denominations are pre-sorted.
- **Dynamic Programming Approach**: Has a time complexity of `O(n * m)`, where `n` is the amount and `m` is the number of coin denominations. This approach typically consumes more memory as well (`O(n)` space complexity for the DP table).

### 4. **Problem-Solving Strategies**
- **Recursive Approach**: Solve the problem recursively by trying to use each coin and then solving the reduced subproblem. This may lead to overlapping subproblems and can be optimized with memoization.
- **Iterative Approach**: Using a bottom-up DP approach by filling a table iteratively, which often leads to more efficient solutions.

### 5. **Python Programming**
Python will be used to implement the solution. Key techniques include:
- List comprehensions for concise operations on lists.
- Efficient use of loops and conditional statements.
- Recursive functions with memoization if taking the recursive DP approach.

## Resources

1. **Python Official Documentation**
   - [More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html) (for loops, if statements)

2. **GeeksforGeeks Articles**
   - [Coin Change | DP-7](https://www.geeksforgeeks.org/coin-change-dp-7/)
   - [Greedy Algorithm to find Minimum number of Coins](https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/)

3. **YouTube Tutorials**
   - [Dynamic Programming - Coin Change Problem](https://www.youtube.com/watch?v=Y0ZqKpToTic) (visual step-by-step explanation of the dynamic programming approach)

## Steps to Completion

1. **Understand the problem**: Carefully read the problem statement and understand the requirements.
2. **Evaluate different approaches**: Choose between a greedy approach or dynamic programming depending on the coin denominations.
3. **Implement the solution**: Write efficient Python code to solve the problem, using appropriate algorithmic strategies.
4. **Test your solution**: Test your code with various test cases to ensure correctness and efficiency.
5. **Analyze the complexity**: Evaluate the time and space complexity of your implementation.

## Conclusion
This project requires balancing efficiency and correctness through careful selection of the appropriate algorithmic approach. While greedy algorithms might work in some cases, dynamic programming often provides a more robust solution for complex cases. The concepts of optimal substructure and overlapping subproblems are key to developing an efficient dynamic programming solution for the coin change problem.
