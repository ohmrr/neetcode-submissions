class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        n, m = len(word1), len(word2)
        i, j = 0, 0

        while i < n or j < m:
            if i < n:
                merged.append(word1[i])
            
            if j < m:
                merged.append(word2[j])
            
            i += 1
            j += 1

        return "".join(merged)