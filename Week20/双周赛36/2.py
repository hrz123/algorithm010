# 2.py
import bisect
from collections import defaultdict
from typing import List


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        res = set()
        record = defaultdict(list)
        for name, time in zip(keyName, keyTime):
            if name in res:
                continue
            tmp = self.to_minute(time)
            loc = bisect.bisect_left(record[name], tmp)
            record[name].insert(loc, tmp)
            if loc - 2 >= 0 and tmp - record[name][loc - 2] <= 60:
                res.add(name)
                continue
            if loc - 1 >= 0 and loc + 1 < len(record[name]) and record[name][
                loc + 1] - record[name][loc - 1] <= 60:
                res.add(name)
                continue
            if loc + 2 < len(record[name]) and record[name][loc + 2] - tmp <= \
                    60:
                res.add(name)
                continue
        res = list(res)
        res.sort()
        return res

    def to_minute(self, time_str):
        h, m = map(int, time_str.split(":"))
        return h * 60 + m


def main():
    sol = Solution()
    keyName = ["john", "john", "john"]
    keyTime = ["23:58", "23:59", "00:01"]
    res = sol.alertNames(keyName, keyTime)
    print(res)


if __name__ == '__main__':
    main()
