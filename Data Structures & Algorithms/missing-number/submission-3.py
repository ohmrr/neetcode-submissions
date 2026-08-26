class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a = 0

        for n in nums:
            a ^= n

        b = 0
        for n in range(len(nums) + 1):
            b ^= n

        return a ^ b
