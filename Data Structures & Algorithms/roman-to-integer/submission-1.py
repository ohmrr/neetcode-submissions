class Solution:
    def romanToInt(self, s: str) -> int:
        conversion = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        result = 0

        i = 0
        while i < len(s):
            if i + 1 < len(s) and conversion[s[i]] < conversion[s[i + 1]]:
                result += conversion[s[i + 1]] - conversion[s[i]]
                i += 2
            else:
                result += conversion[s[i]]
                i += 1

        return result