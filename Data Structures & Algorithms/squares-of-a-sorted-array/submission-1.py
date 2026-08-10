class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        mid = len(nums) // 2
        left, right = mid - 1, mid

        squared = []

        while left >= 0 and right < len(nums):
            if nums[left] ** 2 <= nums[right] ** 2:
                squared.append(nums[left] ** 2)
                left -= 1

            if nums[left] ** 2 >= nums[right] ** 2:
                squared.append(nums[right] ** 2)
                right += 1

        return squared 