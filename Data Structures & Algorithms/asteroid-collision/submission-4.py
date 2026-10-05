class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            stack.append(ast)

            while len(stack) >= 2 and stack[-2] > 0 and stack[-1] < 0:
                s1, s2 = abs(stack[-2]), abs(stack[-1])

                if s1 > s2: # asteroid moving right is bigger than asteroid moving left
                    stack.pop()
                elif s1 < s2: # asteroid moving right is smaller than asteroid moving left
                    # swap since bigger asteroid just added and is at the top.
                    # we want to pop the top w/ O(1) time complex
                    stack[-2], stack[-1] = stack[-1], stack[-2]
                    stack.pop()
                elif s1 == s2: # asteroids the same size
                    stack.pop()
                    stack.pop()

        return stack