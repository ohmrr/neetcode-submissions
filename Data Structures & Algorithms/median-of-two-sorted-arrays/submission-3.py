class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        # Run binary search on the smaller array
        # Ensure A is the smaller array
        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = l + (r - l) // 2    # A
            # Why subtract the extra 2?
            # B/c A contributes i + 1 elements to left partition
            # So we need to find how many elements from B can be added to the partition of length half
            # j = half - (i + 1) - 1
            # subtract the extra 1 to convert B's count back to an index (last index of left partition)
            j = half - i - 2        # B
            

            # grab the last value of the left partition for both arrays
            Aleft = A[i] if i >= 0 else float("-infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")

            # grab the first value of the right partition for both arrays
            Aright = A[i + 1] if i + 1 < len(A) else float("infinity")
            Bright = B[j + 1] if j + 1 < len(B) else float("infinity")

            # Ensure the left partition is correct:
            # The last value of left partition for both arrays is <= first value of right partition for both arrays
            if Aleft <= Bright and Bleft <= Aright:
                # if even length, take middle 2 numbers
                if total % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
                else:
                    return min(Aright, Bright)
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
