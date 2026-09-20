class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums) - 1
        max_sum = -1
        nums.sort()

        while left < right:
            summ = nums[left] + nums[right]

            if summ < k:
                max_sum = max(max_sum, summ)
                left += 1
            else:
                right -= 1

        return max_sum

        