def climbStairs(n):
    if n == 1:
        return 1

    # Initialize the base cases
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    # Fill the dp array based on the recurrence relation
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

# Example usage:
print(climbStairs(2))  # Output: 2
print(climbStairs(3))  # Output: 3
