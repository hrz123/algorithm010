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


def main():
    pass


if __name__ == '__main__':
    main()
