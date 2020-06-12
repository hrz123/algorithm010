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


def main():
    s = Solution()
    res = s.plusOne([9, 9])
    print(res)


if __name__ == '__main__':
    main()
