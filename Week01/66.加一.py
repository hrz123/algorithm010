# 66.加一.py

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        size = len(digits)

        for i in range(size - 1, -1, -1):
            digits[i] += 1
            digits[i] %= 10
            if digits[i] != 0:
                return digits

        if not any(digits):
            digits.insert(0, 1)

        return digits


# 以下为自我练习
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        size = len(digits)

        for i in range(size - 1, -1, -1):
            digits[i] += 1
            digits[i] %= 10
            if digits[i]:
                return digits

        if not digits[0]:
            digits.insert(0, 1)

        return digits


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        size = len(digits)

        for i in range(size - 1, -1, -1):
            digits[i] += 1
            digits[i] %= 10
            if digits[i]:
                return digits
        if not digits[0]:
            digits.insert(0, 1)

        return digits


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1
            if digits[i] == 10:
                digits[i] = 0
            if digits[i]:
                return digits
        if not digits[0]:
            digits.insert(0, 1)
        return digits


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1
            if digits[i] == 10:
                digits[i] = 0
            else:
                return digits
        if not digits[0]:
            digits.insert(0, 1)
        return digits


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1
            if digits[i] == 10:
                digits[i] = 0
            else:
                return digits
        if not digits[0]:
            digits.insert(0, 1)
        return digits


def main():
    s = Solution()
    res = s.plusOne([9, 9])
    print(res)

    res = s.plusOne([9, 8])
    print(res)


if __name__ == '__main__':
    main()
