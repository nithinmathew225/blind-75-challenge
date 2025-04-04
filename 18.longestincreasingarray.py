class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subseq = []
    
        for num in nums:
            pos = bisect.bisect_left(subseq, num)
            if pos == len(subseq):
                subseq.append(num)
            else:
                subseq[pos] = num
        
        return len(subseq)
