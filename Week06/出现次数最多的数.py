# 出现次数最多的数.py

# 给定一个数组，数组长度为n,数组所有元素x满足：0<x<=m<=1000。
# 求数组中出现次数最多的元素，
# 若多个元素出现次数相同，输出元素值较大的，
# 要求时间复杂度O(m),空间O(1)。


class Solution:
    def maxCount(self, nums):
        counter = [0] * 1000
        max_count = 0
        res = 0
        for num in nums:
            counter[num - 1] += 1
            if counter[num - 1] > max_count:
                max_count = counter[num - 1]
                res = num
        return res


# 改变原有数组，不使用额外数组
class Solution:
    def maxCount(self, nums):
        for num in nums:
            nums[(num - 1) & ((1 << 16) - 1)] += (1 << 16)

        res = 0
        max_count = 0
        for i in range(len(nums) - 1, -1, -1):
            count = nums[i] >> 16
            if count > max_count:
                max_count = count
                res = i

        return res + 1


class Solution:
    def maxCount(self, nums):
        for num in nums:
            nums[(num - 1) & ((1 << 16) - 1)] += 1 << 16
        _max = 0
        res = 0
        for i in range(len(nums) - 1, -1, -1):
            count = nums[i] >> 16
            if count > _max:
                _max = count
                res = i
        return res + 1


class Solution:
    def maxCount(self, nums):
        mask = (1 << 16) - 1
        for n in nums:
            nums[n - 1 & mask] += 1 << 16
        _max_count = 0
        res = 0
        for i in range(len(nums) - 1, -1, -1):
            count = nums[i] >> 16
            if count > _max_count:
                _max_count = count
                res = i + 1
        return res


def main():
    sol = Solution()

    nums = [2, 5, 5, 2, 6, 6]
    res = sol.maxCount(nums)
    print(res)

    nums = [1, 1, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9]
    res = sol.maxCount(nums)
    print(res)


if __name__ == '__main__':
    main()
