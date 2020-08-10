# 剑指 Offer 41. 数据流中的中位数.py
import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heap1 = []
        self.heap2 = []
        self.size = 0

    def addNum(self, num: int) -> None:
        if not self.heap1 or num > -self.heap1[0]:
            heapq.heappush(self.heap2, num)
        else:
            heapq.heappush(self.heap1, -num)
        self.size += 1
        if len(self.heap1) - len(self.heap2) == 2:
            heapq.heappush(self.heap2, -heapq.heappop(self.heap1))
        elif len(self.heap1) < len(self.heap2):
            heapq.heappush(self.heap1, -heapq.heappop(self.heap2))

    def findMedian(self) -> float:
        if self.size & 1:
            return -self.heap1[0]
        return (-self.heap1[0] + self.heap2[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

def main():
    sol = MedianFinder()
    sol.addNum(-1)
    sol.addNum(-2)
    print(sol.findMedian())
    sol.addNum(-3)
    sol.addNum(-4)
    sol.addNum(-5)
    print(sol.findMedian())


if __name__ == '__main__':
    main()
