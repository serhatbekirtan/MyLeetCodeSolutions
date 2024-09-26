class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.calendar:
            #  (e > start and end > s)
            if ((s > start) and (e < end)) or (s <= start < e) or (s < end <= e):
                return False

        self.calendar.append([start, end])
        return True
    

class Tree:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None

    def insert(self, start, end):
        curr = self

        while True:
            if end <= curr.start:
                if not curr.left:
                    curr.left = Tree(start, end)
                    return True
                curr = curr.left
            
            elif start >= curr.end:
                if not curr.right:
                    curr.right = Tree(start, end)
                    return True
                curr = curr.right
            
            else:
                return False


class MyCalendar:
    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = Tree(start, end)
            return True
        
        return self.root.insert(start, end)