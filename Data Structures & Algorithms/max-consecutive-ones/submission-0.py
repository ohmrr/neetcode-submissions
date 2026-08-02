class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left, right = 0, 0
        n, maxx = len(nums) - 1, 0

        while left <= n and right <= n:
            if nums[left] == 1:
                right = left
                while right <= n and nums[right] == 1:
                    right += 1

                if maxx < right - left:
                    maxx = right - left

                left = right
            
            left += 1
        
        return maxx
