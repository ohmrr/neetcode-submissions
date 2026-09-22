class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        n1, n2 = 0, 0

        while n1 < len(nums1) and n2 < len(nums2):
            if nums1[n1] < nums2[n2]:
                nums.append(nums1[n1])
                n1 += 1
            else:
                nums.append(nums2[n2])
                n2 += 1

        if n1 < len(nums1):
            for i in range(n1, len(nums1)):
                nums.append(nums1[i])

        if n2 < len(nums2):
            for i in range(n2, len(nums2)):
                nums.append(nums2[i])

        if len(nums) % 2 == 0:
            m1, m2 = len(nums) // 2 - 1, len(nums) // 2
            return (nums[m1] + nums[m2]) / 2
        else:
            m = math.floor(len(nums) // 2)
            return nums[m]