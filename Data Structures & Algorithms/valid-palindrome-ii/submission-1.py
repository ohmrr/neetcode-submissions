class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] == s[r]:
                l, r = l + 1, r - 1
                continue

            l_removed, r_removed = s[l + 1:r + 1], s[l:r]
            return l_removed == l_removed[::-1] or r_removed == r_removed[::-1]
            
        return True
