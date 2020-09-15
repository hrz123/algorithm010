# 1282. 用户分组.py
from collections import defaultdict
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        hashmap = defaultdict(list)
        for i, g in enumerate(groupSizes):
            hashmap[g].append(i)
        res = []
        for k, v in hashmap.items():
            for i in range(0, len(v), k):
                res.append(v[i:i + k])
        return res


def main():
    sol = Solution()
    nums = [3, 3, 3, 3, 3, 1, 3]
    res = sol.groupThePeople(nums)
    print(res)


if __name__ == '__main__':
    main()
