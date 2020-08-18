# 1437. 是否所有 1 都至少相隔 k 个元素.py
from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if not k:
            return True
        c = k
        for num in nums:
            if num == 1:
                if c < k:
                    return False
                c = 0
            else:
                c += 1
        return True


def main():
    sol = Solution()
    nums = [1, 0, 0, 0, 1, 0, 0, 1]
    k = 2
    res = sol.kLengthApart(nums, k)
    print(res)


if __name__ == '__main__':
    main()
