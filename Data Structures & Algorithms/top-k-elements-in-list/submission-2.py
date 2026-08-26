class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        count = [[] for i in range(len(nums) + 1)]

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        for n, cnt in freq.items():
            count[cnt].append(n)

        result = []

        for i in range(len(count) - 1, 0, -1):
            for n in count[i]:
                result.append(n)

                if len(result) == k:
                    return result
