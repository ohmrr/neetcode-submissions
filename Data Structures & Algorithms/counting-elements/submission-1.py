class Solution:
    def countElements(self, arr: List[int]) -> int:
        s = set(arr)
        res = 0

        for n in arr:
            if n + 1 in s:
                res += 1
        
        return res