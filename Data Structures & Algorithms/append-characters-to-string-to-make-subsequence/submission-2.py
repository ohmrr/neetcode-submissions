class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s_char, t_char = 0, 0

        while s_char < len(s) and t_char < len(t):
            if s[s_char] == t[t_char]:
                t_char += 1
            
            s_char += 1

        return len(t) - t_char