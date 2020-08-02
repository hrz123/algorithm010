# 45. 跳跃游戏 II.py
from typing import List


# 贪心算法
# 每次在可跳范围内选择可以使得跳得更远的位置
class Solution:
    def jump(self, nums: List[int]) -> int:
        end = 0
        max_position = 0
        steps = 0

        n = len(nums)
        # 这里注意是len(nums) - 1，因为是索引为0时，steps已经是1了
        for i in range(n - 1):
            # 更新这一步能走到的最远距离
            max_position = max(max_position, nums[i] + i)
            if max_position >= n - 1:
                return steps + 1
            # 第几步可达的边界，遇到边界就更新边界，且步数加一
            if i == end:
                end = max_position
                steps += 1
        return steps


# 以下为自我练习
# 最佳解法
class Solution:
    def jump(self, nums: List[int]) -> int:
        # 当前能到的最大值
        cur = 0
        # 一旦超过当前能到的最大值，下一步可以走到的最远位置是哪里
        cur_max = 0
        # 记录一共需要多少步
        steps = 0

        for i in range(len(nums)):
            # 如果这个位置比能到达的最大值要大了，就步数加一，并且把当前最大值更新为当前已经加一的这一步的上一步能到达的最大值
            if i > cur:
                steps += 1
                cur = cur_max
            # 更新在这一步范围内，下一步能到达的最大值
            cur_max = max(cur_max, nums[i] + i)

        return steps


class Solution:
    def jump(self, nums: List[int]) -> int:
        # 当前能走到的最远
        cur_max = 0
        # 下一步能走到的最远
        next_max = 0
        steps = 0
        for i in range(len(nums)):
            if i > cur_max:
                steps += 1
                cur_max = next_max
            next_max = max(next_max, i + nums[i])
        return steps


class Solution:
    def jump(self, nums: List[int]) -> int:
        cur_max = 0
        next_max = 0
        steps = 0
        for i in range(len(nums)):
            if i > cur_max:
                steps += 1
                cur_max = next_max
            next_max = max(next_max, i + nums[i])
        return steps


def main():
    sol = Solution()

    nums = [2, 3, 1, 1, 4]
    res = sol.jump(nums)
    print(res)

    nums = [0]
    res = sol.jump(nums)
    print(res)


if __name__ == '__main__':
    main()
