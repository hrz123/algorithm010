# 981. 基于时间的键值存储.py
import bisect
from collections import defaultdict


class TimeMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.dict[key])
        while l < r:
            mid = l + (r - l >> 1)
            if self.dict[key][mid][0] > timestamp:
                r = mid
            else:
                l = mid + 1
        return self.dict[key][l - 1][1] if l else ''


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        loc = bisect.bisect(self.dict[key], (timestamp, chr(123)))
        return self.dict[key][loc - 1][1] if loc else ''


class TimeMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        loc = bisect.bisect_left(self.dict[key], (timestamp, chr(123)))
        return "" if loc == 0 else self.dict[key][loc - 1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
def main():
    pass


if __name__ == '__main__':
    main()
