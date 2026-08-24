class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []

        c1, c2 = 0, 0
        while c1 < len(word1) and c2 < len(word2):
            merged.append(word1[c1])
            merged.append(word2[c2])

            c1 += 1
            c2 += 1

        if c1 < len(word1):
            merged.append(word1[c1:])
        elif c2 < len(word2):
            merged.append(word2[c2:])

        return ''.join(merged)