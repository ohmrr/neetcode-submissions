class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_length = 0

        left = 0
        for right in range(len(s)): # O(n)
            while s[right] in seen: # O(1)
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            max_length = max(max_length, len(seen))

        return max_length