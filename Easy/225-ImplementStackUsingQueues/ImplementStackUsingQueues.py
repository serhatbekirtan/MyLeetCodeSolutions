from collections import deque


class MyStack:

    def __init__(self):
        self.dequeue = deque()

    def push(self, x: int) -> None:
        self.dequeue.append(x)

    def pop(self) -> int:
        if self.dequeue:
            for i in range(len(self.dequeue) - 1):
                self.push(self.dequeue.popleft())
            return self.dequeue.popleft()
        else:
            return None

    def top(self) -> int:
        if self.dequeue:
            return self.dequeue[-1]
        else:
            return None

    def empty(self) -> bool:
        return len(self.dequeue) == 0