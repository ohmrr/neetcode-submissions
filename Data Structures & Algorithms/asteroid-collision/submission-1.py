class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in range(len(asteroids)):
            stack.append(asteroids[i])

            while len(stack) >= 2 and stack[-2] > 0 and stack[-1] < 0:
                size1, size2 = abs(stack[-2]), abs(stack[-1])

                if size1 > size2:
                    stack.pop()
                elif size1 < size2:
                    stack[-2], stack[-1] = stack[-1], stack[-2]
                    stack.pop()
                elif size1 == size2:
                    stack.pop()
                    stack.pop()

        return stack