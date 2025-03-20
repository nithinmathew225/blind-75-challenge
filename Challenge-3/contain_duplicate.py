from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == len(set(nums)):
            return False
        else:
            return True


obj = Solution()
nums = [1,2,3,1]
print(obj.containsDuplicate(nums))