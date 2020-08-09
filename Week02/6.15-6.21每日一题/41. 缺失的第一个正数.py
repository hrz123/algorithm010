# 41. 缺失的第一个正数.py
from typing import List


# 如果本题没有额外的时空复杂度要求，那么就很容易实现：
# 1. 我们可以将数组所有的数放入哈希表，随后从1开始依次枚举正整数，并判断其是否在哈希表中；
# 2. 我们可以从1开始依次枚举正整数，并遍历数组，判断其是否在数组中
# 如果数组的长度为N，那么第一种做法的时间复杂度为O(N)，空间复杂度为O(N)；
# 第二种做法的时间复杂度为O(N^2)，空间复杂度为O(1)。
# 「真正」满足此要求的算法是不存在的。但是我们可以退而求其次：利用给定数组中的空间来存储一些状态。
# 也就是说，如果题目给定的数组是不可修改的，那么就不存在满足时空复杂度要求的算法；
# 但如果我们可以修改给定的数组，那么是存在满足要求的算法的。

# 方法一.哈希表
# 对于「前言」中提到的第一种做法
# 我们可以将数组所有的数放入哈希表，随后从1开始依次枚举正整数，并判断其是否在哈希表中；
# 仔细想一想，我们为什么要使用哈希表？这是因为哈希表是一个可以支持快速查找的数据结构：
# 给定一个元素，我们可以在O(1)的时间查找给元素是否在哈希表中。
# 因此，我们可以考虑将给定的数组设计成哈希表的「替代产品」。
# 实际上，对于一个长度为N的数组，其中更没有出现的最小正整数只能在[1, N+1]中。
# 这是因为如果[1,N]都出现了，那么答案是N+1，否则答案是[1, N]中没有出现的最小正整数。
# 这样一来，我们将所有在[1,N]范围内的数放入哈希表，也可以得到最终的答案。
# 而给定的数组恰好长度为N，这让我们有了一种将数组设计成哈希表的思路。
# 我们对数组进行遍历，对于遍历到的数x，如果它在[1,N]的范围内，那么就将数组的中的
# 第x-1个位置（注意：数组下标从0开始）打上『标记』。
# 在遍历结束后，如果所有的位置都打上了标记，那么答案是N+1，
# 否则答案是最小的没有打上标记的位置加1.
# 那么如何设计这个『标记』呢？由于数组中的数没有任何限制，因此这并不是一件很容易的事情。
# 但我们可以继续利用上面提到的性质：由于我们只在意[1,N]中的数
# 因此我们可以先对数组进行遍历，把不在[1,N]范围内的数修改成任意一个大于N的数（例如N+1）
# 这样一来，数组中的所有数就都是正数了，因此我们就可以将「标记」表示为「负号」。算法的流程如下
# 我们将数组中所有小于等于0的数修改成N+1
# 我们遍历数组中的每一个数x，它可能已经被打了标记，因此原本对应的数|x|，其中||为绝对值符号。
# 如果|x|∈[1,N]，那么我们给数组中的第|x|-1个位置添加一个负号。
# 注意如果它已经有负号，不需要重复添加；
# 在遍历完成之后，如果数组中的每一个数都是负数，那么答案是N+1，否则答案是第一个正数的位置加1.
# 时间复杂度：O(n)，遍历3次数组
# 空间复杂度：O(1)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        for i in range(n):
            x = abs(nums[i])
            if 0 < x <= n:
                nums[x - 1] = nums[x - 1] if nums[x - 1] < 0 else -nums[x - 1]
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1


# 除了打标记之外，我们哈可以使用置换的方法，将给定的数组「恢复」成下面的形式：
# 如果数组中包含x∈[1,N]，那么恢复后，数组的第x-1和元素为x。
# 在恢复后，数组应当有[1,2,...,N]的形式，但其中有若干个位置上的数是错误的
# 每一个错误的位置就代表一个缺失的正数。以题目中的示例2[3,4,-1,1]为例，
# 恢复后的数组应当为[1,-1,3,4]，我们就可以知道缺失的数为2.
# 那么我们如何将数组进行恢复呢？我们可以对数组进行一次遍历吗，对于遍历到的数x=nums[i]，
# 如果x∈[1, N]，我们就知道x应当出现在数组中的x-1的位置，因此交换nums[i]和nums[x-1]，
# 这样x就出现在了正确的位置。在完成交换之后，新的nums[i]可能还在[1,N]的范围内，
# 我们需要继续进行交换操作，直到x∉[1,N].
# 注意到上面的方法可能会陷入死循环，如果nums[i]恰好与nums[x-1]相等，那么就会无限交换下去。
# 此时我们有nums[i] = x = nums[x-1]，说明x已经出现在了正确的位置。
# 因此我们可以跳出循环，开始遍历下一个数。
# 由于每次的交换操作都会使得某一个数交换到正确的位置，因此交换的次数最多为N，
# 整个方法的时间复杂度为O(N)

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1


# 以下为自我练习
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        for i in range(n):
            x = abs(nums[i])
            if 0 < x <= n:
                nums[x - 1] = -nums[x - 1] if nums[x - 1] > 0 else nums[x - 1]
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        for i in range(n):
            x = abs(nums[i])
            if 0 < x <= n:
                nums[x - 1] = -nums[x - 1] if nums[x - 1] > 0 else nums[x - 1]
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        for i in range(n):
            x = abs(nums[i])
            if 0 < x <= n:
                nums[x - 1] = nums[x - 1] if nums[x - 1] < 0 else -nums[x - 1]
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1


def main():
    sol = Solution()

    nums = [1, 2, 0]
    res = sol.firstMissingPositive(nums)
    print(res)

    nums = [2147483647]
    res = sol.firstMissingPositive(nums)
    print(res)

    nums = [3, 4, -1, 1]
    res = sol.firstMissingPositive(nums)
    print(res)


if __name__ == '__main__':
    main()
