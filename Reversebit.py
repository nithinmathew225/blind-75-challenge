class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_num = 0
        for i in range(32):  
            reversed_num = (reversed_num << 1) | (n & 1)  
            n >>= 1  
        return reversed_num

obj= Solution()
n = 00000010100101000001111010011100
print(obj.reverseBits(n))