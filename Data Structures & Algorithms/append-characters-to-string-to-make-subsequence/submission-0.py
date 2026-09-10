class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s_char, t_char = 0, 0

        while s_char < len(s):
            if s[s_char] == t[t_char]:
                t_char += 1

                if t_char == len(t):
                    return 0

            s_char += 1 

        return len(t) - t_char