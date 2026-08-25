class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        map = {}

        for n in nums:
            map[n] = map.get(n, 0) + 1

        print(map)

        for count in map.values():
            if count % 2 == 1:
                return False

        return True
