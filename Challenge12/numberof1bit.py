

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

obj = Solution()
n= 128
print(obj.hammingWeight(n))