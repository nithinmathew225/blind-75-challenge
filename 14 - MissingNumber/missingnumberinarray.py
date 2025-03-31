from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        nums.sort()
        counter = 0
        if nums[0] != 0:
            return 0
        while counter < length:
            if nums[counter] != counter:
                break
            else:
                counter += 1
        return counter
        #best Solution
        # n = len(nums)
        # expected_sum = n * (n + 1) // 2
        # actual_sum = sum(nums)
        # return expected_sum - actual_sum


obj = Solution()
nums = [3,0,1]
obj.missingNumber(nums)

