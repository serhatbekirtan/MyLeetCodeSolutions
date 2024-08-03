from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        else:
            val = ""
            arr = self.hashmap[key]
            L, R = 0, len(arr) - 1

            while L <= R:
                mid = (L + R) // 2
                if arr[mid][1] > timestamp:
                    R = mid - 1
                elif arr[mid][1] < timestamp:
                    val = arr[mid][0]
                    L = mid + 1
                else:
                    return arr[mid][0]
                    
            return val


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)