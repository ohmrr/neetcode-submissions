class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = [0] * len(arr)

        maxx = -1
        for i in range(len(arr) - 1, -1, -1):
            greatest[i] = maxx
            maxx = max(maxx, arr[i])

        return greatest