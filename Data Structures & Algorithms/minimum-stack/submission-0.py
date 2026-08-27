class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        if not self.mins or self.mins[-1] >= val:
            self.mins.append(val)

        self.stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.mins[-1]:
            self.mins.pop()
        
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]
