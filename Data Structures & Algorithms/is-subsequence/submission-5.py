class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        target_char, curr_char = 0, 0

        while target_char < len(s) and curr_char < len(t):
            if s[target_char] == t[curr_char]:
                target_char += 1

            curr_char += 1

        return target_char == len(s)
