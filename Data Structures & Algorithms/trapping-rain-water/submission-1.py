class Solution:
    def trap(self, height: List[int]) -> int:
        # leftMax = [0] * len(height)
        # curr_left_max = height[0]
        # for i in range(len(height)):
        #     curr_left_max = max(height[i], curr_left_max)
        #     leftMax[i] = curr_left_max

        # rightMax = [0] * len(height)
        # curr_right_max = height[-1]
        # for i in range(len(height) - 1, -1, -1):
        #     curr_right_max = max(height[i], curr_right_max)
        #     rightMax[i] = curr_right_max

        # total_water = 0
        # for i in range(len(height)):
        #     total_water += min(leftMax[i], rightMax[i]) - height[i]

        # return total_water

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        result = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                result += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                result += rightMax - height[r]

        return result