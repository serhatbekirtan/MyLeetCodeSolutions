import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        uglySet = set()
        uglySet.add(1)

        for i in range(n):
            num = heapq.heappop(heap)

            if i == n - 1:
                return num

            for fac in [2,3,5]:
                if num * fac not in uglySet:
                    uglySet.add(num * fac)
                    heapq.heappush(heap, num * fac)

    
    def nthUglyNumber(self, n: int) -> int:
        arr = [1]
        i2, i3, i5 = 0, 0, 0

        for _ in range(n):
            uglyNum = min(arr[i2] * 2, arr[i3] * 3, arr[i5] * 5)
            arr.append(uglyNum)

            if uglyNum == arr[i2] * 2:
                i2 += 1
            if uglyNum == arr[i3] * 3:
                i3 += 1
            if uglyNum == arr[i5] * 5:
                i5 += 1

        return arr[n - 1]