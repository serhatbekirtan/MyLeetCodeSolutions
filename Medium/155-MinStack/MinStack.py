class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            self.stack.append((val, min(val, self.stack[-1][1])))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None

    def getMin(self) -> int:
        return min(self.stack[-1][0], self.stack[-1][1])
    

# 2 Stack implementation
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        minVal = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(minVal)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]