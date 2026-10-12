class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        count = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            freq[n] = 1 + freq.get(n, 0)

        for num, cnt in freq.items():
            count[cnt].append(num)

        result = []
        for i in range(len(count) - 1, 0, -1):
            for num in count[i]:
                result.append(num)
                if len(result) == k:
                    return result