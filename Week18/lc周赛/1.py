# 1.py
from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        cur = []
        for log in logs:
            if log == '../':
                if cur:
                    cur.pop()
            elif log == './':
                continue
            else:
                cur.append(log)
        print(cur)
        print(len(cur))
        return len(cur)


def main():
    pass


if __name__ == '__main__':
    main()
