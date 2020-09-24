# 636. 函数的独占时间.py
from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        res = [0] * n
        prev = 0
        for log in logs:
            fid, s, t = log.split(':')
            # print(stack)
            # print(res)
            if s == "start":
                if stack:
                    res[stack[-1]] += int(t) - prev
                stack.append(int(fid))
                prev = int(t)
            else:
                res[stack.pop()] += int(t) - prev + 1
                prev = int(t) + 1
        return res


def main():
    pass


if __name__ == '__main__':
    main()
