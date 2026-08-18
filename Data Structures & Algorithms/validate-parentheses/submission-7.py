class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closedToOpen = { ')': '(', ']': '[', '}': '{' }

        for c in s:
            if c in closedToOpen:
                if not stack:
                    return False

                if closedToOpen[c] != stack[-1]:
                    return False

                stack.pop()
            else:
                stack.append(c)

        return not stack
        