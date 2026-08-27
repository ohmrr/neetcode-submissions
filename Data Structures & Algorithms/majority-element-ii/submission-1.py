class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        result = []

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        for n in freq:
            if freq[n] > len(nums) // 3:
                result.append(n)

        return result