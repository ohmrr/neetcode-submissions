class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_map = {}
        longest = 1

        for n in nums:
            num_map[n] = num_map.get(n, 0) + 1

        for n in nums:
            if n - 1 in num_map:
                continue
            
            curr = n + 1
            length = 1
            while curr in num_map:
                length += 1
                curr += 1
            
            longest = max(length, longest)

        return longest