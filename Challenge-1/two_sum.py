from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = dict()

        for i, num in enumerate(nums):
            complement = target - num
            if complement in prev_map:
                print(prev_map[complement])
                print(i)
                return [prev_map[complement], i]
            prev_map[num] = i



obj = Solution()
nums = [2,7,11,15]
target = 9
obj.twoSum(nums,target)