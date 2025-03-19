from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        high = prices[0]
        lastDifference = 0
        for item in prices:
            if item < low:
                if high - low > lastDifference:
                    lastDifference = high - low
                low = high = item
            elif item > high:
                high = item
        if high - low > lastDifference:
            lastDifference = high - low
        print(lastDifference)
        return lastDifference

obj = Solution()
prices = [7,1,5,3,6,4]
obj.maxProfit(prices)