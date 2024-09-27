class MyCalendarTwo:

    def __init__(self):
        self.nonOverlapping = []
        self.overlapping = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.overlapping:
            if end > s and e > start:
                return False
            
        for s, e in self.nonOverlapping:
            if end > s and e > start:
                self.overlapping.append([max(s, start), min(e, end)])
        
        self.nonOverlapping.append([start, end])
        return True