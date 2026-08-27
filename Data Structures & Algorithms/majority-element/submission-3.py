class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        fq = {}

        for n in nums:
            fq[n] = fq.get(n, 0) + 1

            if fq[n] > len(nums) // 2:
                return n
