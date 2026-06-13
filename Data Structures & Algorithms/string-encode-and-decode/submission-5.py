class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for s in strs:
            res.append(f'{len(s)}#{s}')

        print(''.join(res))
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        j = 0

        while i < len(s):
            while s[j] != '#':
                j += 1

            llen = int(s[i:j])
            res.append(s[j + 1:llen + j + 1])

            i = llen + j + 1
            j = i

        return res