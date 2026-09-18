class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l) // 2

            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1

        if nums[l] <= target <= nums[len(nums) - 1]:
            r = len(nums) - 1
        else:
            l = 0

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l += 1
            else:
                r -= 1
        
        return -1