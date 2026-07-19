class Solution:
    def romanToInt(self, s: str) -> int:
        conv_map = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000
        }

        i = 0
        res = 0
        while i <= len(s) - 1:
            if s[i:i+2] in conv_map:
                res += conv_map.get(s[i:i+2])
                i += 2
            elif s[i] in conv_map:
                res += conv_map.get(s[i])
                i += 1

        return res
