class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # (index, temperature)
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                s_i, s_temp = stack.pop()
                result[s_i] = i - s_i
            
            stack.append((i, temp))
        
        return result