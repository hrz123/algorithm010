# 303. 区域和检索 - 数组不可变.py
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        pre = self.pre = [0]
        p = 0
        for n in nums:
            p += n
            pre.append(p)

    def sumRange(self, i: int, j: int) -> int:
        return self.pre[j + 1] - self.pre[i]


# 以下为自我练习
class NumArray:

    def __init__(self, nums: List[int]):
        self.pre = [0]
        p = 0
        for n in nums:
            p += n
            self.pre.append(p)

    def sumRange(self, i: int, j: int) -> int:
        return self.pre[j + 1] - self.pre[i]


class NumArray:

    def __init__(self, nums: List[int]):
        self.pre = [0]
        p = 0
        for n in nums:
            p += n
            self.pre.append(p)

    def sumRange(self, i: int, j: int) -> int:
        return self.pre[j + 1] - self.pre[i]


class NumArray:

    def __init__(self, nums: List[int]):
        self.pre = [0]
        p = 0
        for num in nums:
            p += num
            self.pre.append(p)

    def sumRange(self, i: int, j: int) -> int:
        return self.pre[j + 1] - self.pre[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
def main():
    pass


if __name__ == '__main__':
    main()
