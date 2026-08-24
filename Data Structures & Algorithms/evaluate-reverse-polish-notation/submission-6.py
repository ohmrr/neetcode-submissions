class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = '+-*/'

        for tok in tokens:
            if not tok in operations:
                stack.append(int(tok))
                continue

            n1, n2 = stack.pop(), stack.pop()

            if tok == '+':
                stack.append(n1 + n2)
            elif tok == '-':
                stack.append(n2 - n1)
            elif tok == '*':
                stack.append(n1 * n2)
            else:
                stack.append(int(float(n2) /n1))

        print(stack)
        return stack[0]