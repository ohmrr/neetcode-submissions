class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = '+-*/'
        stack = []

        for tok in tokens:
            if tok in operations:
                if tok == '+':
                    stack.append(stack.pop() + stack.pop())
                elif tok == '-':
                    n1, n2 = stack.pop(), stack.pop()

                    stack.append(n2 - n1)
                elif tok == '*':
                    stack.append(stack.pop() * stack.pop())
                elif tok == '/':
                    n1, n2 = stack.pop(), stack.pop()
                    stack.append(int(float(n2) / n1))
            else:
                stack.append(int(tok))

        return stack[-1]