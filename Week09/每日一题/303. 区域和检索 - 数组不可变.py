# 303. 区域和检索 - 数组不可变.py
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.pre = [0] * (n + 1)
        for i in range(n):
            self.pre[i + 1] = self.pre[i] + nums[i]

    def sumRange(self, i: int, j: int) -> int:
        return self.pre[j + 1] - self.pre[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
def main():
    pass


if __name__ == '__main__':
    main()
