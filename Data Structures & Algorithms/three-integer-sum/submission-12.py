class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i, n in enumerate(nums):
            if n > 0:
                break

            if i > 0 and nums[i -1] == n:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                summ = n + nums[left] + nums[right]

                if summ > 0:
                    right -= 1
                elif summ < 0:
                    left += 1
                else:
                    result.append([n, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return result