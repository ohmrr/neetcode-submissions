class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a = 0
        b = 0

        for n in nums:
            a = a ^ n

        for n in range(len(nums) + 1):
            b = b ^ n
        
        return a ^ b