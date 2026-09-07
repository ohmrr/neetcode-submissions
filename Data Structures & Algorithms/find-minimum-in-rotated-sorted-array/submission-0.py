class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = nums[0]

        for i in range(1, len(nums)):
            minimum = min(minimum, nums[i])

        return minimum