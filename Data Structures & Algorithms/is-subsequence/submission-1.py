class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i_s, i_t = 0, 0

        while i_t <= len(t) - 1:
            if t[i_t] == s[i_s]:
                i_s += 1

                if i_s == len(s) - 1:
                    return True
            
            i_t += 1

        return False
