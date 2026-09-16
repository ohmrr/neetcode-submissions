class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []

        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue

                if words[i] in words[j]:
                    result.append(words[i])
                    break 
                    # break because the same word can be a substring of
                    # multiple other words but we dont consider duplicates

        return result