class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if mid > right, left = mid + 1
        # [3, 4, 5, 6, 1, 2]
        #  L -----> M     R

        # if mid < right, right = mid
        # [5, 6, 1, 2, 3, 4]
        #     L  M <----- R

        left, right = 0, len(nums) - 1

        while left <= right:
            # avoids integer overflow in languages with fixed size integers, not necessary in python but preferred
            mid = left + (right - left) // 2

            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1

        return nums[right]