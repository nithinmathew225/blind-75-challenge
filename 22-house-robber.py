class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # If there's only one house, return its value
        if len(nums) == 1:
            return nums[0]
        
        # If there are two houses, return the maximum of the two
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        # Initialize the dp array
        dp = [0] * len(nums)
        
        # Base cases
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        # Fill the dp array
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        
        # The last element in dp contains the maximum amount of money we can rob
        return dp[-1]

        
