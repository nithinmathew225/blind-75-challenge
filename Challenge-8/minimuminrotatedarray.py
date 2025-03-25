from typing import List
class Solution:
    #my solution
    def findMin(self, nums: List[int]) -> int:
        first_number = nums[0]
        minnumber = first_number
        total_length = len(nums)
        if nums[0] < nums[total_length-1]:
            return nums[0]
        else:
            for i in range(1, total_length):
                minnumber = min(first_number, nums[i])
                if minnumber != first_number:
                    first_number = minnumber
                    break

        return minnumber
    #best solution
    # def findMin(self, nums: List[int]) -> int:
    #     left, right = 0, len(nums) - 1
    #
    #     while left < right:
    #         mid = (left + right) // 2
    #         if nums[mid] > nums[right]:
    #             left = mid + 1
    #         else:
    #             right = mid
    #
    #     return nums[left]


obj = Solution()
nums= [3,4,5,1,2]
print(obj.findMin(nums))