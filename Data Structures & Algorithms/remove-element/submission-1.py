class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # init a left pointer to 0 and right to len(nums) - 1
        # start by positioning right until it does not equal the target val
            # right most numbers that equal val can be skipped since those are already in the correct place
        # then compare left with val, if it equals, swap left and right. then increment right
        # if not, then increment left

        # set l, r to 0 and end of nums
        # if nums[l] equals to val
            # move r until it does not equal val
            # swap l and r
            # move r to left by 1
        # otherwise we can keep moving l to the right
        
        l, r = 0, len(nums) - 1

        while l < r:
            if nums[l] == val:
                while l < r and nums[r] == val:
                    r -= 1
                
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            else:
                l += 1

        k = 0
        for n in nums:
            if n == val:
                break

            k += 1

        return k