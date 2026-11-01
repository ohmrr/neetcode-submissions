class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = { ')': '(', ']': '[', '}': '{' }
        stack = []

        for i in range(len(s)):
            if s[i] in closeToOpen:
                if not stack:
                    return False

                if closeToOpen[s[i]] != stack[-1]:
                    return False

                stack.pop()
            else:
                stack.append(s[i])

        return not stack