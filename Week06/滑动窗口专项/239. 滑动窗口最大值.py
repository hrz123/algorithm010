# 239. 滑动窗口最大值.py
from collections import deque
from typing import List


# 方法一
# 暴力解法
# 时间复杂度：O(m*k)

# 方法二
# 维护一个缓存
# 遍历数组
# 如果新的元素比较大
# 就添加
# 如果新的元素比缓存尾部元素小
# 就不添加
# 缓存的大小始终不大于k
# 当遍历到第i个元素， 缓存首部为j，start - k = j的时候
# 先将缓存首部去掉
# 缓存最好的数据结构是单调队列，底层是双端队列

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = deque()
        size = len(nums)
        res = [0] * (size - k + 1)

        for i in range(size):
            # 只要双端队列存在，并且新来的元素，大于等于旧的元素
            while deq and nums[i] >= nums[deq[-1]]:
                # 旧的元素就没有用了可以删除了
                deq.pop()
            # 都删除之后将新的元素添加队列尾部
            deq.append(i)
            # 看是否需要更新窗口最大值了
            idx = i - k + 1
            # 此时需要更新窗口最大值
            if idx >= 0:
                res[idx] = nums[deq[0]]
                # 查看队列的头部元素是否需要删除
                if deq[0] == idx:
                    deq.popleft()

        return res


# 以下为自我练习
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        deq = deque()

        for i in range(len(nums)):
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()
            deq.append(i)

            index = i - k + 1
            if index >= 0:
                res.append(nums[deq[0]])
                if deq[0] == index:
                    deq.popleft()

        return res


# 单调双端队列
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        deq = deque()
        for i in range(len(nums)):
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()
            deq.append(i)
            index = i - k + 1
            if index >= 0:
                res.append(nums[deq[0]])
                if deq[0] == index:
                    deq.popleft()
        return res


# 单调双端队列，队列存索引，因为需要索引排除窗口最左端
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = deque()
        n = len(nums)
        res = [0] * (n - k + 1)
        for i in range(n):
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()
            deq.append(i)
            idx = i - k + 1
            if idx >= 0:
                res[idx] = nums[deq[0]]
                if deq[0] == idx:
                    deq.popleft()
        return res


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = deque()
        n = len(nums)
        res = [0] * (n - k + 1)
        for i in range(n):
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()
            deq.append(i)
            idx = i - k + 1
            if idx >= 0:
                res[idx] = nums[deq[0]]
                if idx == deq[0]:
                    deq.popleft()
        return res


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = deque()
        n = len(nums)
        res = [0] * (n - k + 1)
        for i in range(len(nums)):
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()
            deq.append(i)
            idx = i - k + 1
            if idx >= 0:
                res[idx] = nums[deq[0]]
                if deq[0] == idx:
                    deq.popleft()
        return res


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = deque()
        n = len(nums)
        res = [0] * (n - k + 1)
        for i, n in enumerate(nums):
            while deq and nums[deq[-1]] <= n:
                deq.pop()
            deq.append(i)
            idx = i - k + 1
            if idx >= 0:
                res[idx] = nums[deq[0]]
                if deq[0] == idx:
                    deq.popleft()
        return res


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = deque()
        res = [0] * (len(nums) - k + 1)
        for i, n in enumerate(nums):
            while deq and nums[deq[-1]] < n:
                deq.pop()
            deq.append(i)
            ind = i - k + 1
            if ind >= 0:
                res[ind] = nums[deq[0]]
                if deq[0] == ind:
                    deq.popleft()
        return res


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = deque()
        res = [0] * (len(nums) - k + 1)
        for i, n in enumerate(nums):
            while deq and nums[deq[-1]] < n:
                deq.pop()
            deq.append(i)
            ind = i - k + 1
            if ind >= 0:
                res[ind] = nums[deq[0]]
                if deq[0] == ind:
                    deq.popleft()
        return res


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = deque()
        res = [0] * (len(nums) - k + 1)
        for i, n in enumerate(nums):
            while deq and nums[deq[-1]] <= n:
                deq.pop()
            deq.append(i)
            idx = i - k + 1
            if idx >= 0:
                res[idx] = nums[deq[0]]
                if deq[0] == idx:
                    deq.popleft()
        return res


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = deque()
        res = [0] * (len(nums) - k + 1)
        for i, num in enumerate(nums):
            while deq and nums[deq[-1]] <= num:
                deq.pop()
            deq.append(i)
            idx = i - k + 1
            if idx >= 0:
                res[idx] = nums[deq[0]]
                if deq[0] == idx:
                    deq.popleft()
        return res


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = deque()
        res = [0] * (len(nums) - k + 1)
        for i, num in enumerate(nums):
            while deq and nums[deq[-1]] < num:
                deq.pop()
            deq.append(i)
            idx = i - k + 1
            if idx >= 0:
                res[idx] = nums[deq[0]]
                if deq[0] == idx:
                    deq.popleft()
        return res


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = deque()
        res = [0] * (len(nums) - k + 1)
        for i, num in enumerate(nums):
            while deq and nums[deq[-1]] < num:
                deq.pop()
            deq.append(i)
            idx = i - k + 1
            if idx >= 0:
                res[idx] = nums[deq[0]]
                if deq[0] == idx:
                    deq.popleft()
        return res


def main():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    sol = Solution()
    res = sol.maxSlidingWindow(nums, k)
    print(res)


if __name__ == '__main__':
    main()
