# 面试题 16.11. 跳水板.py
from typing import List


class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        # 特殊情况 k = 0时，返回空数组
        if k == 0:
            return []
        # 特殊情况，短等于长时，生成跳水板可能长度都相等
        if shorter == longer:
            return [shorter * k]
        # 其余情况，因为短不等于长，不可能有重复的长度
        return [shorter * (k - i) + longer * i for i in range(k + 1)]


class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k == 0:
            return []
        if shorter == longer:
            return [k * shorter]
        return [shorter * (k - i) + longer * i for i in range(k + 1)]


class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if not k:
            return []
        if shorter == longer:
            return [shorter * k]
        return [longer * i + shorter * (k - i) for i in range(k + 1)]


class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k == 0:
            return []
        if longer == shorter:
            return [shorter * k]
        return [shorter * (k - i) + longer * i for i in range(k + 1)]


class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k == 0:
            return []
        if shorter == longer:
            return [shorter * k]
        return [shorter * (k - i) + longer * i for i in range(k + 1)]


def main():
    sol = Solution()

    shorter = 1
    longer = 2
    k = 3
    res = sol.divingBoard(shorter, longer, k)
    print(res)
    res = sol.divingBoard(2, 2, 3)
    print(res)
    res = sol.divingBoard(3, 4, 0)
    print(res)


if __name__ == '__main__':
    main()
