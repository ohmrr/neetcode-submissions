class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        chars = {}
        total = 0

        for i, key in enumerate(keyboard):
            chars[key] = i

        prev, result = 0, 0

        for c in word:
            total += abs(prev - chars[c])
            prev = chars[c]

        return total