# 136. 只出现一次的数字.py
from typing import List


# 1.hashmap记录出现次数。元素：次数。返回次数为1的。
# 时间复杂度：遍历数组O(N)。遍历hashmap。O(N)
# 空间复杂度：O(N)。哈希表
# 不赘述。
# 2.hashmap。遇见重复的就删除。返回最终剩下的。
# 时间复杂度:O(N)。遍历数组。
# 空间复杂度:O(N)。最坏情况要存一半。
# 不赘述。
# 3.位运算。相同元素异或自己等于0.
# 所有元素异或后就剩下那个出现一次的元素。
# 0异或上任何数都等于那个数。可以简化代码。
# 时间复杂度：O(N)
# 空间复杂度：O(1)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res


def main():
    pass


if __name__ == '__main__':
    main()
