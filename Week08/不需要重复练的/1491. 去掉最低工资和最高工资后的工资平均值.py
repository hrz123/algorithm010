# 1491. 去掉最低工资和最高工资后的工资平均值.py
from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        _max, _min = float('-inf'), float('inf')
        _sum = 0
        for s in salary:
            _sum += s
            _max = max(_max, s)
            _min = min(_min, s)
        return (_sum - _max - _min) / (len(salary) - 2)


def main():
    pass


if __name__ == '__main__':
    main()
