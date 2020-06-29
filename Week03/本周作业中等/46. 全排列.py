# 46. 全排列.py
from typing import List


# 迭代的写法
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for n in nums:
            new_perms = []
            for perm in perms:
                for i in range(len(perm) + 1):
                    new_perms.append(perm[:i] + [n] + perm[i:])  # insert n
            perms = new_perms
        return perms


def main():
    s = Solution()
    res = s.permute([1, 2, 3])
    print(res)


if __name__ == '__main__':
    main()
