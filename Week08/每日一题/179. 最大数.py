# 179. 最大数.py
from typing import List


class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num


# 以下为自我练习
# 满足传递性即可，传递性可以证明
class LargerNumKey(str):
    def __lt__(self, other):
        return self + other > other + self


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num


class LargerNumKey(str):
    def __lt__(self, other):
        return self + other > other + self


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        largest = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest and largest[0] == '0' else largest


class LargerNumKey(str):
    def __lt__(self, other):
        return self + other > other + self


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        largest = "".join(sorted(map(str, nums), key=LargerNumKey))
        return "0" if largest and largest[0] == '0' else largest


class LargerNumKey(str):
    def __lt__(self, other):
        return self + other > other + self


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if res and res[0] == '0' else res


def main():
    sol = Solution()

    nums = [10, 2]
    res = sol.largestNumber(nums)
    print(res)


if __name__ == '__main__':
    main()
