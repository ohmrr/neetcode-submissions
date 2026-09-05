class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # (temperature, index)

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                s_temp, s_index = stack.pop()
                result[s_index] = i - s_index
            
            stack.append((temp, i))
        
        return result

        