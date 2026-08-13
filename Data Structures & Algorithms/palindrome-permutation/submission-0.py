class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        freq = {}

        for c in s:
            freq[c] = freq.get(c, 0) + 1

        odd = 0
        for c, n in freq.items():
            if n % 2 == 1:
                odd += 1

        return odd <= 1