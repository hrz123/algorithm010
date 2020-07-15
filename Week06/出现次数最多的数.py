# 出现次数最多的数.py
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


def main():
    nums = [2, 5, 5, 2, 4, 4]
    sol = Solution()
    res = sol.maxCount(nums)
    print(res)


if __name__ == '__main__':
    main()
