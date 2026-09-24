class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = defaultdict(int)
        length = 0

        for c in s:
            counts[c] += 1
            if counts[c] % 2 == 0:
                length += 2
        
        for c in counts.values():
            if c % 2 == 1:
                length += 1
                break

        return length
