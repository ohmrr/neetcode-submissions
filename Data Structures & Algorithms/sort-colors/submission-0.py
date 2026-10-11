class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3

        for n in nums:
            count[n] += 1

        i = 0
        for n, freq in enumerate(count):
            while freq > 0:
                nums[i] = n
                i += 1
                freq -= 1

        