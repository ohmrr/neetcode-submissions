class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            charset = [0] * 26

            for c in s:
                charset[ord(c) - ord('a')] += 1
            
            result[tuple(charset)].append(s)

        return list(result.values())