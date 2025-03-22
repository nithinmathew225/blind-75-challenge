import math
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #mysolution
        product = 0
        contains_zero  = 0 in nums
        resultlist = []
        if contains_zero == True:
            zero_count = nums.count(0)
            if zero_count > 1 :
                for _ in range(len(nums)):
                    resultlist.append(0)
            elif zero_count == 1 :
                for item in nums:
                    if item == 0:
                        temp_array = nums.copy()
                        temp_array.remove(item)
                        resultlist.append(int(math.prod(temp_array)))
                    else:
                        resultlist.append(0)
        else:
            product = math.prod(nums)
            for item in nums:
                resultlist.append(int(product/item))


        return resultlist
        #best solution
        # n = len(nums)
        # result = [1] * n
        #
        # # Left product pass
        # left_product = 1
        # for i in range(n):
        #     result[i] = left_product
        #     left_product *= nums[i]
        #
        # # Right product pass
        # right_product = 1
        # for i in range(n - 1, -1, -1):
        #     result[i] *= right_product
        #     right_product *= nums[i]
        #
        # return result


obj = Solution()
nums = [1,2,3,4]
print(obj.productExceptSelf(nums))