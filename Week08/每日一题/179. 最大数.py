# 179. 最大数.py


class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num


def main():
    sol = Solution()

    nums = [10, 2]
    res = sol.largestNumber(nums)
    print(res)


if __name__ == '__main__':
    main()
