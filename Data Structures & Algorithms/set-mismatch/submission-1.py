class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        freq = {}
        result = [0, 0]

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        for n in range(1, len(nums) + 1):
            count = freq.get(n, 0)

            if count == 2:
                result[0] = n
            if count == 0:
                result[1] = n

        return result