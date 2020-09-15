# 1521. 找到最接近目标值的函数值.py
from typing import List


class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        ans = abs(arr[0] - target)
        valid = {arr[0]}
        for num in arr:
            # l, r中的值最多有20种
            valid = {x & num for x in valid} | {num}
            ans = min(ans, min(abs(x - target) for x in valid))
        return ans


def main():
    pass


if __name__ == '__main__':
    main()
