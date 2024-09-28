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
    

class Node:
    def __init__(self, prev, next, val):
        self.prev, self.next, self.val = prev, next, val


class MyCircularDeque:

    def __init__(self, k: int):
        self.space = k
        self.left = Node(None, None, 0)
        self.right = Node(self.left, None, 0)
        self.left.next = self.right


    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            node = Node(self.left, self.left.next, value)
            self.left.next.prev = node
            self.left.next = node
            self.space -= 1
            return True
        return False
        

    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            node = Node(self.right.prev, self.right, value)
            self.right.prev.next = node
            self.right.prev = node
            self.space -= 1
            return True
        return False
        

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            self.left.next = self.left.next.next
            self.left.next.prev = self.left
            self.space += 1
            return True
        return False


    def deleteLast(self) -> bool:
        if not self.isEmpty():
            self.right.prev = self.right.prev.prev
            self.right.prev.next = self.right
            self.space += 1
            return True
        return False


    def getFront(self) -> int:
        return self.left.next.val if not self.isEmpty() else -1


    def getRear(self) -> int:
        return self.right.prev.val if not self.isEmpty() else -1


    def isEmpty(self) -> bool:
        return self.left.next == self.right


    def isFull(self) -> bool:
        return self.space == 0