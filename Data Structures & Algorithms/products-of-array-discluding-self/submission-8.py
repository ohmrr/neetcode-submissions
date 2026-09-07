class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product, num_zeroes = 1, 0

        for n in nums:
            if n == 0:
                num_zeroes += 1
            else:
                product *= n
            
        if num_zeroes > 1:
            return [0] * len(nums)

        for i, n in enumerate(nums):
            if num_zeroes:
                if n:
                    nums[i] = 0
                else:
                    nums[i] = product
            else:
                nums[i] = product // nums[i]

        return nums