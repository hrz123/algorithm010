# 5499. 重复至少 K 次且长度为 M 的模式 .py
from typing import List


class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)
        if n < m * k:
            return False
        for start in range(0, min(m, n - m + 1)):
            pre = None
            counter = 1
            while start < n:
                tmp = tuple(arr[start:start + m])
                start += m
                if tmp == pre:
                    counter += 1
                else:
                    counter = 1
                if counter == k:
                    return True
                pre = tmp
        return False


def main():
    sol = Solution()
    arr = [1, 2, 4, 4, 4, 4]
    m = 1
    k = 3
    res = sol.containsPattern(arr, m, k)
    print(res)

    arr = [2, 2, 1, 2, 2, 1, 1, 1, 2, 1]
    m = 2
    k = 2
    res = sol.containsPattern(arr, m, k)
    print(res)


if __name__ == '__main__':
    main()
