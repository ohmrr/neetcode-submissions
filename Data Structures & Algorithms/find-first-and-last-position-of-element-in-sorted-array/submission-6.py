class Solution:
    def binary_search(self, nums, target, leftBias):
            left, right = 0, len(nums) - 1
            i = - 1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    i = mid

                    if leftBias:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return i

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binary_search(nums, target, True)
        right = self.binary_search(nums, target, False)

        return [left, right]

