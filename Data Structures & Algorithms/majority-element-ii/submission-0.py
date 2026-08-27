class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        result = set()

        for n in nums:
            freq[n] = freq.get(n, 0) + 1
            
            if freq[n] > len(nums) // 3:
                result.add(n)

        return list(result)