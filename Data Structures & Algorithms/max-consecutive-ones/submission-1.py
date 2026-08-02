class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones, current = 0, 0

        for n in nums:
            if n == 1:
                current += 1
                max_ones = max(max_ones, current)
            else:
                current = 0
        
        return max_ones
