class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        fmap = {}
        max_val = 0

        for n in nums:
            n_freq = fmap.get(n, 0)

            if n_freq + 1 > fmap.get(max_val, 0):
                max_val = n

            fmap[n] = n_freq + 1

        return max_val