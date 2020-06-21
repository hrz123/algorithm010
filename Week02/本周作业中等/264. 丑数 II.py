# 264. 丑数 II.py

# 1.维护一个小顶堆。
# 开始时堆只有1.
# 移除堆顶元素1。
# 加入1*2， 1*3， 1*5.
# 继续移除堆顶。
# 2.临时计算。三个指针开始都指向第1个元素1.
# 如果nums[i2]*2, nums[i3]*3, nums[i5]*5那个更小就加入。
# 然后如果是nums[i2]*2，i2+= 1
# 如果是nums[i3]*3，i3+= 1
# 如果是nums[i5]*5，i5+= 1
# 重复的话指针都移到下一位
# 时间复杂度O(N)
# 空间复杂度O(N)
# 3.因为n不超过一个数。可以提前计算。hashmap返回相应索引的元素。
# 时间复杂度O(1)
# 空间复杂度O(1)

# 算法
#  - 预计算1690个丑数： 1是丑数
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
