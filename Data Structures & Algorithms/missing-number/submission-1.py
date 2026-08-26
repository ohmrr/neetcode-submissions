class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        seen = set()

        for num in nums:
            seen.add(num)

        for num in range(n):
            if num not in seen:
                return num