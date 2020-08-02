# 5476. 找出数组游戏的赢家.py
from typing import List


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if k >= n - 1:
            return max(arr)
        i = 0
        cont = 0
        while cont < k:
            if arr[i] > arr[i + 1]:
                arr.append(arr[i + 1])
                arr[i + 1] = arr[i]
                cont += 1
            else:
                arr.append(arr[i])
                cont = 1
            i += 1
        return arr[i]


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr) - 1:
            return max(arr)
        cur, tmp = arr[0], k
        for i in range(1, len(arr)):
            if cur > arr[i]:
                tmp -= 1
            else:
                cur = arr[i]
                tmp = k - 1
            if tmp == 0:
                return cur
        return cur


def main():
    sol = Solution()

    arr = [2, 1, 3, 5, 4, 6, 7]
    k = 2
    res = sol.getWinner(arr, k)
    print(res)


if __name__ == '__main__':
    main()
