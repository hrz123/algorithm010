# 1122. 数组的相对排序.py
from typing import List


# 计数排序
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = [0] * 1001
        for n in arr1:
            counter[n] += 1
        res = [0] * len(arr1)
        start = 0
        for n in arr2:
            num_n = counter[n]
            res[start: start + num_n] = [n] * num_n
            start += num_n
            counter[n] = 0
        for n in range(1001):
            num_n = counter[n]
            if num_n:
                res[start: start + num_n] = [n] * num_n
                start += num_n
        return res


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr = [0 for _ in range(1001)]
        ans = []
        for n in arr1:
            arr[n] += 1
        for n in arr2:
            while arr[n]:
                ans.append(n)
                arr[n] -= 1
        for i in range(1001):
            while arr[i] > 0:
                ans.append(i)
                arr[i] -= 1
        return ans


# 国际站解法
# 虽然短，然而这不是O(n)的解法
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        k = {b: i for i, b in enumerate(arr2)}
        return sorted(arr1, key=lambda a: k.get(a, 1000 + a))


# 以下为自我练习
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = [0] * 1001
        for n in arr1:
            counter[n] += 1

        res = [0] * len(arr1)
        i = 0
        for n in arr2:
            while counter[n] > 0:
                res[i] = n
                i += 1
                counter[n] -= 1
        for n in range(1001):
            while counter[n] > 0:
                res[i] = n
                i += 1
                counter[n] -= 1
        return res


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = [0] * 1001
        for n in arr1:
            counter[n] += 1

        res = [0] * len(arr1)
        i = 0
        for n in arr2:
            res[i:i + counter[n]] = [n] * counter[n]
            i += counter[n]
            counter[n] = 0
        for n in range(1001):
            if counter[n]:
                res[i:i + counter[n]] = [n] * counter[n]
                i += counter[n]
        return res


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = [0] * 1001
        for n in arr1:
            counter[n] += 1

        res = [0] * len(arr1)
        i = 0
        for n in arr2:
            for _ in range(counter[n]):
                res[i] = n
                i += 1
            counter[n] = 0
        for k in range(len(counter)):
            for _ in range(counter[k]):
                res[i] = k
                i += 1
        return res


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = [0] * 1001
        for n in arr1:
            counter[n] += 1
        res = [0] * len(arr1)
        i = 0
        for n in arr2:
            for _ in range(counter[n]):
                res[i] = n
                i += 1
            counter[n] = 0
        for n in range(len(counter)):
            for _ in range(counter[n]):
                res[i] = n
                i += 1
        return res


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = [0] * len(arr1)
        counter = [0] * 1001
        for n in arr1:
            counter[n] += 1
        i = 0
        for n in arr2:
            while counter[n] > 0:
                counter[n] -= 1
                res[i] = n
                i += 1
        for k in range(1001):
            while counter[k] > 0:
                res[i] = k
                i += 1
                counter[k] -= 1
        return res


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = [0] * 1001
        for n in arr1:
            counter[n] += 1
        res = []
        for n in arr2:
            res.extend([n] * counter[n])
            counter[n] = 0
        for i in range(1001):
            if counter[i]:
                res.extend([i] * counter[i])
        return res


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = [0] * 1001
        for num in arr1:
            counter[num] += 1
        res = []
        for num in arr2:
            res.extend([num] * counter[num])
            counter[num] = 0
        for num in range(1001):
            if counter[num]:
                res.extend([num] * counter[num])
        return res


def main():
    sol = Solution()

    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]
    res = sol.relativeSortArray(arr1, arr2)
    assert res == [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]
    print(res)


if __name__ == '__main__':
    main()
