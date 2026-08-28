class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0] * n

        prefix = 1
        for i in range(n):
            # 1     2       4       6
            # 1     1       2       8
            output[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]

        return output
