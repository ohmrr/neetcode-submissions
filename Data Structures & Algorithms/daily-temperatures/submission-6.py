class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # (temp, i)
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                stack_temp, stack_i = stack.pop()
                result[stack_i] = i - stack_i

            stack.append((temp, i))

        return result