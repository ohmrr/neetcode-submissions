class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0

        while i < len(t):
            if j < len(s) and t[i] == s[j]:
                j += 1

            i += 1
        
        return len(s) == j