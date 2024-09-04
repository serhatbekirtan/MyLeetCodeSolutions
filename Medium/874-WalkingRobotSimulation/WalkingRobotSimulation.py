from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        self.x, self.y, self.direction, self.furthest = 0, 0, 0, 0
        obs = {tuple(o) for o in obstacles}

        def calculateDist():
            self.furthest = max(self.furthest, (self.x ** 2) + (self.y ** 2))

        def checkObstacle(x, y):
            return (self.x + x, self.y + y) in obs

        def move(distance):
            match self.direction:
                case 0:
                    for _ in range(distance):
                        if checkObstacle(0, 1):
                            return
                        self.y += 1
                case 1:
                    for _ in range(distance):
                        if checkObstacle(1, 0):
                            return
                        self.x += 1
                case 2:
                    for _ in range(distance):
                        if checkObstacle(0, -1):
                            return
                        self.y += -1
                case 3:
                    for _ in range(distance):
                        if checkObstacle(-1, 0):
                            return
                        self.x += -1
                        
        def setDirection(turn):
            if turn == -2:
                self.direction = (self.direction - 1) % 4
            else:
                self.direction = (self.direction + 1) % 4

        for command in commands:
            if command >= 0:
                move(command)
                calculateDist()
            else:
                setDirection(command)

        return self.furthest
    

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]] # North, East, South, West
        x, y, direction, res = 0, 0, 0, 0
        obstacles = {tuple(o) for o in obstacles}

        for command in commands:
            if command == -1:
                direction = (direction + 1) % 4
            elif command == -2:
                direction = (direction - 1) % 4
            else:
                dx, dy = directions[direction]
                for _ in range(command):
                    if (x + dx, y + dy) in obstacles:
                        break
                    x, y = x + dx, y + dy
                
            res = max(res, x ** 2 + y ** 2)
        
        return res