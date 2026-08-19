class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for s in strs:
            res.append(f'{len(s)}#{s}')

        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        strs = []

        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] != '#':
                j += 1

            length = int(s[i:j])

            word = s[j+1:j+length+1]
            strs.append(word)
            
            i = j + length + 1

        return strs