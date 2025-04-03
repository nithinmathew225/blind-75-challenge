class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize dp array with a value greater than the max #possible number of coins (amount + 1)
        dp = [float('inf')] * (amount + 1)
        
        # Base case: 0 amount requires 0 coins
        dp[0] = 0
        
        # Iterate over all amounts from 1 to amount
        for i in range(1, amount + 1):
            # Check each coin denomination
            for coin in coins:
                if i - coin >= 0:  # We can use this coin if the remaining amount is non-negative
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        # If dp[amount] is still infinity, it means we cannot make the amount
        return dp[amount] if dp[amount] != float('inf') else -1
        
