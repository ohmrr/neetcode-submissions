class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for s in strs:
            res.append(f'{len(s)}#{s}')

        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            llen = int(s[i])

            res.append(s[i+2:i+llen+2])
            
            i += llen + 2

        return res