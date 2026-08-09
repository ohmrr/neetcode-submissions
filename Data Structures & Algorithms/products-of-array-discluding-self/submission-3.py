class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        curr = 1

        for i in range(1, len(nums)):
            curr *= nums[i - 1]
            prefix.append(curr)
        
        suffix = [1] * len(nums)
        curr = 1
        for i in range(len(nums) - 2, -1, -1):
            curr *= nums[i + 1]
            suffix[i] = curr

        output = []
        for i in range(len(prefix)):
            output.append(prefix[i] * suffix[i])

        return output