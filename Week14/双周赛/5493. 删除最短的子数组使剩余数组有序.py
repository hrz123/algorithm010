# 5493. 删除最短的子数组使剩余数组有序.py
import bisect
from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        start = 0
        i = 0
        while i < n - 1 and arr[i] <= arr[i + 1]:
            i += 1
        left = i - start + 1
        if left == n:
            return 0
        start = n - 1
        i = n - 1
        while i > 0 and arr[i] >= arr[i - 1]:
            i -= 1
        right = start - i + 1

        def get_max_len(left, right):
            res = 0
            for l in range(left):
                r = bisect.bisect_left(arr[n - right:], arr[l])
                res = max(res, l + 1 + right - r)
            return res

        mix = get_max_len(left, right)

        return min(n - mix, n - left, n - right)

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        Right = 0
        las = 1e9 + 5
        n = len(arr)
        for i in arr[::-1]:
            if i <= las:
                Right += 1
                las = i
            else:
                break
        if Right == n:
            return 0
        Left = 0
        las = -1
        ans = n - Right
        for i in arr:
            if i >= las:
                Left += 1
                las = i
                while Right >= 1 and arr[n - Right] < i:
                    Right -= 1
                ans = min(ans, n - (Left + Right))
            else:
                break
        return ans
def main():
    sol = Solution()
    # arr = [13, 0, 14, 7, 18, 18, 18, 16, 8, 15, 20]
    # res = sol.findLengthOfShortestSubarray(arr)
    # print(res)
    # arr = [1, 2, 3, 10, 4, 2, 3, 5]
    # res = sol.findLengthOfShortestSubarray(arr)
    # print(res)
    #
    # arr = [0, 1, 2, 3, 9, 8, 7, 2, 2, 3, 5, 6]
    # res = sol.findLengthOfShortestSubarray(arr)
    # print(res)
    # arr = [1, 3, 2.5, 3, 4]
    # res = sol.findLengthOfShortestSubarray(arr)
    # print(res)
    # arr = [1, 2, 3, 10, 4, 2, 3, 5]
    # res = sol.findLengthOfShortestSubarray(arr)
    # print(res)
    arr = [6, 3, 10, 11, 15, 20, 13, 3, 18, 12]
    res = sol.findLengthOfShortestSubarray(arr)
    print(res)


if __name__ == '__main__':
    main()
