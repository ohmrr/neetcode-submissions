class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        length = 0

        for c in s:
            count[c] = 1 + count.get(c, 0)
            if count[c] % 2 == 0:
                length += 2

        for char, cnt in count.items():
            if cnt % 2 == 1:
                length += 1
                break
        
        return length