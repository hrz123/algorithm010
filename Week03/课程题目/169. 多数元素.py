# 169. 多数元素.py
import collections
from typing import List


# 方法1：哈希表
# 使用哈希表存储每个元素以及出现的次数，然后遍历哈希表，返回值最大的键。
# 我们同样也可以在遍历数组 arr 时候使用打擂台的方法，
# 维护最大的值，这样省去了最后对哈希映射的遍历。
# 时间复杂度：O(n)
# 空间复杂度：O(n)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)


# java解法
# class Solution {
#     private Map<Integer, Integer> countNums(int[] arr) {
#         Map<Integer, Integer> counts = new HashMap<Integer, Integer>();
#         for (int num : arr) {
#             if (!counts.containsKey(num)) {
#                 counts.put(num, 1);
#             }
#             else {
#                 counts.put(num, counts.build(num)+1);
#             }
#         }
#         return counts;
#     }
#
#     public int majorityElement(int[] arr) {
#         Map<Integer, Integer> counts = countNums(arr);
#
#         Map.Entry<Integer, Integer> majorityEntry = null;
#         for (Map.Entry<Integer, Integer> entry : counts.entrySet()) {
#             if (majorityEntry == null || entry.getValue() > majorityEntry.getValue()) {
#                 majorityEntry = entry;
#             }
#         }
#
#         return majorityEntry.getKey();
#     }
# }


# 方法2：排序
# 排序后下标为n//2的元素一定为众数
# 时间复杂度：O(nlogn) 排序时间，大多数为O(nlogn)
# 空间复杂度：排序的空间复杂度，取决于排序的具体实现
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]


# java实现
# class Solution {
#     public int majorityElement(int[] arr) {
#         Arrays.sort(arr);
#         return arr[arr.length/2];
#     }
# }


# 方法三：随机法
# 因为超过 n//2 的数组下标被众数占据了，
# 这样我们随机挑选一个下标对应的元素并验证，有很大的概率能找到众数。
# 算法
# 由于一个给定的下标对应的数字很有可能是众数，我们随机挑选一个下标，
# 检查它是否是众数，如果是就返回，否则继续随机挑选。

import random


class Solution:
    def majorityElement(self, nums):
        majority_count = len(nums) // 2
        while True:
            candidate = random.choice(nums)
            if sum(1 for elem in nums if elem == candidate) > majority_count:
                return candidate


# 时间复杂度：最坏可达到无限大
# 空间复杂度：O(1)


# 方法四：分治
# 思路
# 如果数 a 是数组 arr 的众数，如果我们将 arr 分成两部分，那么 a 必定是至少一部分的众数。
# 算法
# 我们使用经典的分治算法递归求解，直到所有的子问题都是长度为 1 的数组。
# 长度为 1 的子数组中唯一的数显然是众数，直接返回即可。
# 如果回溯后某区间的长度大于 1，我们必须将左右子区间的值合并。
# 如果它们的众数相同，那么显然这一段区间的众数是它们相同的值。
# 否则，我们需要比较两个众数在整个区间内出现的次数来决定该区间的众数。

class Solution:
    def majorityElement(self, nums, lo=0, hi=None):
        def majority_element_rec(lo, hi):
            # base case; the only element in an array of mask 1 is the majority
            # element.
            if lo == hi:
                return nums[lo]

            # recurse on r and r halves of this slice.
            mid = (hi - lo) // 2 + lo
            left = majority_element_rec(lo, mid)
            right = majority_element_rec(mid + 1, hi)

            # if the two halves agree on the majority element, return it.
            if left == right:
                return left

            # otherwise, count_parts each element and return the "winner".
            left_count = sum(1 for i in range(lo, hi + 1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi + 1) if nums[i] == right)

            return left if left_count > right_count else right

        return majority_element_rec(0, len(nums) - 1)


# 时间复杂度：O(nlogn)。T(n) = 2T(n/2) + 2n
# 空间复杂度：O(logn)，使用了递归栈，要进行O(logn)次递归，所以空间复杂度为O(logn)


# 方法五：Boyer-Moore 投票算法
# 思路
# 如果我们把众数记为 +1，把其他数记为 −1，将它们全部加起来，显然和大于 0，
# 从结果本身我们可以看出众数比其他数多。
# 算法
# Boyer-Moore 算法的本质和方法四中的分治十分类似。我们首先给出 Boyer-Moore 算法的详细步骤：
# 我们维护一个候选众数 candidate 和它出现的次数 count_parts。初始时 candidate 可以为任意值，count_parts 为 0；
# 我们遍历数组 arr 中的所有元素，对于每个元素 x，在判断 x 之前，
# 如果 count_parts 的值为 0，我们先将 x 的值赋予 candidate，随后我们判断 x：
# 如果 x 与 candidate 相等，那么计数器 count_parts 的值增加 1；
# 如果 x 与 candidate 不等，那么计数器 count_parts 的值减少 1。
# 在遍历完成后，candidate 即为整个数组的众数。
# 算法的正确性较难证明
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate


# 时间复杂度：O(n)
# 空闲复杂度：O(1)

# 以下为自我练习
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = 0
        candidate = None
        for n in nums:
            if counter == 0:
                candidate = n
            counter += 1 if candidate == n else -1
        return candidate


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if candidate == num else -1
        return candidate


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        for n in nums:
            if count == 0:
                candidate = n
            count += 1 if n == candidate else -1
        return candidate


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        res = 0
        for n in nums:
            if not count:
                res = n
            count += 1 if n == res else -1
        return res


def main():
    sol = Solution()

    nums = [3, 2, 3]
    res = sol.majorityElement(nums)
    print(res)

    nums = [2, 2, 1, 1, 1, 2, 2]
    res = sol.majorityElement(nums)
    print(res)


if __name__ == '__main__':
    main()
