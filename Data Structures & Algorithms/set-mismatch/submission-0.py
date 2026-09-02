class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        result = []

        for n in nums:
            if n in seen:
                result.append(n)
            else:
                seen.add(n)

        for n in range(1, len(nums) + 1):
            if not n in seen:
                result.append(n)

        return result
