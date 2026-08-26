class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = '+-*/'
        stack = []

        for tok in tokens:
            if tok in operations:
                n1, n2 = stack.pop(), stack.pop()

                if tok == '+':
                    stack.append(n1 + n2)
                elif tok == '-':
                    stack.append(n2 - n1)
                elif tok == '*':
                    stack.append(n1 * n2)
                elif tok == '/':
                    stack.append(int(float(n2) / n1))
            else:
                stack.append(int(tok))

        return stack[0]