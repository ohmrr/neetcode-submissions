class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # count = [0] * 3

        # for n in nums:
        #     count[n] += 1

        # i = 0
        # for n, freq in enumerate(count):
        #     while freq > 0:
        #         nums[i] = n
        #         i += 1
        #         freq -= 1

        l, r = 0, len(nums) - 1
        i = 0

        while i <= r:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
                i -= 1

            i += 1
