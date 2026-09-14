class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        nm = {}

        for n in nums:
            nm[n] = 1 + nm.get(n, 0)

        largest = - 1
        for n, cnt in nm.items():
            if n > largest and cnt == 1:
                largest = n

        return largest