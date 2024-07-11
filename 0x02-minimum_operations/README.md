# Minimum Operations to Achieve `n` Characters

## Problem Statement

Given a text file that initially contains a single character 'H', and a text editor that supports only two operations:
1. **Copy All:** Copies the entire content of the file.
2. **Paste:** Appends the copied content to the file.

Write a method `minOperations(n)` that calculates the minimum number of operations needed to achieve exactly `n` 'H' characters in the file. If it's impossible to achieve exactly `n` 'H's, return `0`.

### Example

For `n = 9`:
- Start with `H`.
- **Copy All**: Copy the single 'H'.
- **Paste**: Append to get `HH`.
- **Paste**: Append to get `HHH`.
- **Copy All**: Copy the three 'H's.
- **Paste**: Append to get `HHHHHHH`.
- **Paste**: Append to get `HHHHHHHHH`.

Total operations: `6` (2 `Copy All`, 4 `Paste`).

### Approach

1. **Initialization:**
   - Start with `ops = 0` (to count operations).
   - Initialize `root = 2` (since Copy All and Paste operations are used minimally).

2. **Factorization Process:**
   - Loop while `root <= n`.
   - If `n % root == 0`:
     - Add `root` to `ops` (representing the number of operations needed for each factor).
     - Update `n` to `n / root` (reduce the problem size).
     - Decrement `root` to check for smaller factors.
   - Increment `root` to explore other factors.

3. **Termination:**
   - The loop terminates when `root` exceeds `n`.
   - Return the accumulated `ops` as the minimum number of operations needed.

### Detailed Steps

1. **Check Divisibility:**
   - If `n` is divisible by `root`, it means `root` is a valid factor.
   - Update operations count and reduce `n`.

2. **Update Factors:**
   - Decrease `root` to explore smaller potential factors, but increment it to find the next valid factor.

3. **Return Result:**
   - After all factors are processed, return the total operations.

### Complexity

- **Time Complexity:** Depends on the number of factors of `n`, which is generally manageable for practical values of `n`.
- **Space Complexity:** O(1), as only a few variables are used.

### Code Example

```python
def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H characters
    """
    if n < 2:
        return 0
    ops, root = 0, 2
    while root <= n:
        if n % root == 0:
            ops += root
            n = n / root
            root -= 1
        root += 1
    return ops
```

### Notes

- **Initial Setup:** The file starts with `1 H`. To achieve more, operations must be planned strategically.
- **Factorization Insight:** Each factorization step represents a valid combination of operations needed to build up the number of 'H's efficiently.

For more details on implementation or to test different values of `n`, use the provided function and examples.

