# 45. 跳跃游戏 II.py
from typing import List


# 贪心算法
# 每次在可跳范围内选择可以使得跳得更远的位置
class Solution:
    def jump(self, nums: List[int]) -> int:
        end = 0
        maxPosition = 0
        steps = 0
        # 这里注意是len(nums) - 1，因为是索引为0时，steps已经是1了
        for i in range(len(nums) - 1):
            # 找能跳得最远的
            maxPosition = max(maxPosition, nums[i] + i)
            # 遇到边界就更新边界，且步数加一
            if i == end:
                end = maxPosition
                steps += 1
        return steps


def main():
    pass


if __name__ == '__main__':
    main()
