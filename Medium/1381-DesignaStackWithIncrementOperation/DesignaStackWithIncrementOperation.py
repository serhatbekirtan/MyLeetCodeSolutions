class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.currSize = 0
        self.maxSize = maxSize
        

    def push(self, x: int) -> None:
        if not self.isFull():
            self.stack.append(x)
            self.currSize += 1


    def pop(self) -> int:
        if not self.isEmpty():
            self.currSize -= 1
            return self.stack.pop()
        return -1


    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, self.currSize)):
            self.stack[i] += val

    
    def isFull(self):
        return self.currSize == self.maxSize

    
    def isEmpty(self):
        return self.currSize == 0