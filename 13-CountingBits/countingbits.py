from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        return_result = []
        for i in range(n+1):
            print(bin(i).count('1'))
            return_result.append(bin(i).count('1'))
        print(return_result)
        return return_result

obj= Solution()
n = 5
obj.countBits(n)