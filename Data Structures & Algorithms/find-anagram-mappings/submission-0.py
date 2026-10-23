class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # initialize an array to hold the output
        mapping = [0] * len(nums1)

        # create a hash map to store the indices of values in nums2
        index_map = {}

        for i, n in enumerate(nums2):
            index_map[n] = i

        # then, go through each num in num1 and index_map[num] should be the correct mapping

        for i, n in enumerate(nums1):
            mapping[i] = index_map[n]

        return mapping