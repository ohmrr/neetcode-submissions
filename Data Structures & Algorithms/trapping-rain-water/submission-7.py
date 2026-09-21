class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax, rightMax = [0] * n, [0] * n
        total_water = 0

        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])

        rightMax[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        for i in range(n):
            total_water += min(leftMax[i], rightMax[i]) - height[i]

        return total_water