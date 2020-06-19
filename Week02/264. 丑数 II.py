# 264. 丑数 II.py
# 算法
#  - 预计算1690个丑数：
#    - 初始化数组 nums 和三个指针i2, i3, i5
#    - 循环计算所有丑数。每一步：
#      - 在nums[i2] * 2, nums[i3] * 3 和 nums[i5] * 5 选出最小的数字添加到数组 nums 中
#      - 将该数字对应的因子指针向前移动一步
#  - 在数组中返回所需的丑数。


class Ugly:
    def __init__(self):
        self.nums = nums = [1, ]
        i2 = i3 = i5 = 0

        for _ in range(1, 1690):
            ugly = min(nums[i2] * 2, nums[i3] * 3, nums[i5] * 5)
            nums.append(ugly)

            if ugly == nums[i2] * 2:
                i2 += 1
            if ugly == nums[i3] * 3:
                i3 += 1
            if ugly == nums[i5] * 5:
                i5 += 1


class Solution:
    u = Ugly()

    def nthUglyNumber(self, n: int) -> int:
        return self.u.nums[n - 1]


def main():
    s = Solution()
    res = s.nthUglyNumber(1690)
    print(res)


if __name__ == '__main__':
    main()
