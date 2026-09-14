class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # largest = 0
        
        # for i, height in enumerate(heights):
        #     left, right = i, i
            
        #     while left >= 0 and heights[left - 1] >= height:
        #         left -= 1

        #     while right <= len(heights) - 2 and heights[right + 1] >= height:
        #         right += 1

        #     largest = max(largest, height * (right - left + 1))

        # return largest

        max_area = 0
        stack = [] # (index, height)

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index # move start back since we know this height is greater than the current height we're at
            
            stack.append((start, h))

        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area