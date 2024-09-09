from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1] * n for _ in range(m)]
        left, right, top, bottom = 0, n, 0, m

        while head and left < right:
            for i in range(left, right):
                if head:
                    matrix[top][i] = head.val
                    head = head.next
            top += 1

            for i in range(top, bottom):
                if head:
                    matrix[i][right - 1] = head.val
                    head = head.next
            right -= 1

            if not head or left >= right or top >= bottom:
                break

            for i in range(right - 1, left - 1, -1):
                if head:
                    matrix[bottom - 1][i] = head.val
                    head = head.next
            bottom -= 1

            for i in range(bottom - 1, top - 1, -1):
                if head:
                    matrix[i][left] = head.val
                    head = head.next
            left += 1

        return matrix
    

    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        left, right, top, bottom = 0, n, 0, m
        matrix = [[-1] * n for _ in range(m)]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]] # right, down, left, up
        row, col, direction = 0, 0, 0

        while head:
            dr, dc = directions[direction]

            while head and (left <= col < right) and (top <= row < bottom) and matrix[row][col] == -1:
                matrix[row][col] = head.val
                head = head.next
                row, col = row + dr, col + dc
            
            row, col = row - dr, col - dc
            direction = (direction + 1) % 4
            dr, dc = directions[direction]
            row, col = row + dr, col + dc
        
        return matrix