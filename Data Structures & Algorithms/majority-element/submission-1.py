class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        fmap = {}
        max_val = 0

        for n in nums:
            n_freq = fmap.get(n, 0)

            if n_freq > fmap.get(max_val, 0):
                maxx = n

            fmap[n] = n_freq + 1

        return maxx