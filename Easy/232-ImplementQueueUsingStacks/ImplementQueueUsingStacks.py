class MyQueue:

    def __init__(self):
        self.stack = []
        self.stack_backup = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if not self.stack_backup:
            while self.stack:
                self.stack_backup.append(self.stack.pop())
        return self.stack_backup.pop()

    def peek(self) -> int:
        if not self.stack_backup:
            while self.stack:
                self.stack_backup.append(self.stack.pop())
        return self.stack_backup[-1]

    def empty(self) -> bool:
        return max(len(self.stack), len(self.stack_backup)) == 0