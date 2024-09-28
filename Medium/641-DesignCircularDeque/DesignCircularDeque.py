class MyCircularDeque:

    def __init__(self, k: int):
        self.arr = []
        self.k = k
        self.size = 0


    def insertFront(self, value: int) -> bool:
        if self.size < self.k:
            self.arr.insert(0, value)
            self.size += 1
            return True
        return False
        

    def insertLast(self, value: int) -> bool:
        if self.size < self.k:
            self.arr.append(value)
            self.size += 1
            return True
        return False
        

    def deleteFront(self) -> bool:
        if self.size:
            self.arr.pop(0)
            self.size -= 1
            return True
        return False


    def deleteLast(self) -> bool:
        if self.size:
            self.arr.pop()
            self.size -= 1
            return True
        return False

    def getFront(self) -> int:
        if self.size:
            return self.arr[0]
        return -1

    def getRear(self) -> int:
        if self.size:
            return self.arr[-1]
        return -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k