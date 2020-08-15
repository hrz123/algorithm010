# 433. 最小基因变化.py
from collections import deque
from typing import List, Set


# 从目标库中，选一个bank[start]，和start diff为1的，尝试一下，
# 如果发现这种尝试失败了（start 一步变不到bank[start]），
# 就回溯到上一层（记得清理现场），尝试bank中下一个bank[start]，再去和start比。
# 否则成功的话，就把这个bank[start]（start一步变成的），
# dfs到下一层作为下一层的start
# 一旦发现start和end一样了，在终止条件中记录目前为止count的最小值
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # 剪枝: 所有的目标基因序列必须是合法的。
        if end not in bank:
            return -1

        min_count = -1

        def __diff(s1: str, s2: str) -> int:
            res = 0
            for i, ch in enumerate(s1):
                if ch != s2[i]:
                    res += 1
            return res

        def __dfs(start: str, end: str, bank: List[str], visited: set,
                  count: int) -> None:
            nonlocal min_count
            # recursion terminator
            if end == start:
                if min_count == -1 or count < min_count:
                    min_count = count
            # process current row logic
            for elem in bank:
                if elem not in visited:
                    if __diff(elem, start) == 1:
                        visited.add(elem)
                        # drill down
                        __dfs(elem, end, bank, visited, count + 1)
                        # reverse current row status
                        visited.remove(elem)

        __dfs(start, end, bank, set(), 0)

        return min_count


# 第二种解法，
# bfs
# bfs(row, start, end， visited)
# 终止条件
# 若start等于end，返回level
# 每次
# 将所有change摆出，
# 若在visited中，不递归
# 若在bank中，递归
# 若全部change都不在bank中，返回-1
class Solution:

    def __init__(self):
        self.change = {
            'A': "CGT",
            'C': "AGT",
            'G': "ACT",
            "T": "ACG"
        }

    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        return self.__bfs(start, end, set(bank))

    def __bfs(self, start: str, end: str, bank: Set[str]) -> int:
        # 定义结果变量
        ans = 0
        # 定义广度优先所需队列
        deq = deque()
        # 队列加入初始元素
        deq.append(start)
        # 防止环的出现，加入visited记录已访问的元素
        visited = set(start)

        while deq:
            # 遍历这一层
            size = len(deq)
            for _ in range(size):
                cur = deq.popleft()
                # 如果到了终点，返回结果
                if cur == end:
                    return ans
                # 产生这一元素能产生的孩子
                children = [e for e in self.__showChanges(cur) if e in
                            bank and e not in visited]
                # 加入到queue中
                deq.extend(children)
                # 加入到visited中
                visited.update(children)
            # 层数加一
            ans += 1
        # 如果队列为空也没找到，返回负1
        return -1

    def __showChanges(self, cur):
        for i in range(8):
            for ch in self.change[cur[i]]:
                yield cur[:i] + ch + cur[i + 1:]


# 以下为自我练习
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if end not in bank:
            return -1
        bq, eq, nq, n = {start}, {end}, set(), 8
        res = 0

        while bq:
            bank -= bq
            res += 1
            for x in bq:
                for y in [x[:i] + c + x[i + 1:] for i in range(n) for c in
                          "AGCT"]:
                    if y in bank:
                        if y in eq:
                            return res
                        nq.add(y)
            bq, nq = nq, set()
            if len(bq) > len(eq):
                bq, eq = eq, bq
        return -1


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if end not in bank:
            return -1
        bq, eq, nq, n = {start}, {end}, set(), 8
        res = 0
        while bq:
            bank -= bq
            res += 1
            for x in bq:
                for y in [x[:i] + c + x[i + 1:] for i in range(n) for c in
                          "AGCT"]:
                    if y in bank:
                        if y in eq:
                            return res
                        nq.add(y)
            bq, nq = nq, set()
            if len(bq) > len(eq):
                bq, eq = eq, bq
        return -1


# 以下为自我练习
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if end not in bank:
            return -1

        bq, eq, nq, res = {start}, {end}, set(), 0

        while bq:
            bank -= bq
            res += 1
            for x in bq:
                for y in [x[:i] + c + x[i + 1:] for i in range(8) for c in
                          "AGCT"]:
                    if y in bank:
                        if y in eq:
                            return res
                        nq.add(y)
            bq, nq = nq, set()
            if len(bq) > len(eq):
                bq, eq = eq, bq
        return -1


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if end not in bank:
            return -1
        bq, eq, nq, n, res = {start}, {end}, set(), 8, 0
        while bq:
            bank -= bq
            res += 1
            for x in bq:
                for y in [x[:i] + c + x[i + 1:] for i in range(n) for c in
                          "AGCT"]:
                    if y in bank:
                        if y in eq:
                            return res
                        nq.add(y)
            bq, nq = nq, set()
            if len(bq) > len(eq):
                bq, eq = eq, bq
        return -1


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if end not in bank:
            return -1
        bq, eq, nq, res = {start}, {end}, set(), 0
        while bq:
            bank -= bq
            res += 1
            for x in bq:
                for y in [x[:i] + c + x[i + 1:] for i in range(8)
                          for c in 'AGCT']:
                    if y in bank:
                        if y in eq:
                            return res
                        nq.add(y)
            bq, nq = nq, set()
            if len(bq) > len(eq):
                bq, eq = eq, bq
        return -1


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if end not in bank:
            return -1
        bq, eq, nq, res = {start}, {end}, set(), 0
        while bq:
            bank -= bq
            res += 1
            for x in bq:
                for y in [x[:i] + c + x[i + 1:] for i in range(8) for c in
                          "AGCT"]:
                    if y in bank:
                        if y in eq:
                            return res
                        nq.add(y)
            bq, nq = nq, set()
            if len(bq) > len(eq):
                bq, eq = eq, bq
        return -1


def main():
    sol = Solution()
    start = "AAAAACCC"
    end = "AACCCCCC"
    bank = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]

    res = sol.minMutation(start, end, bank)
    print(res)


if __name__ == '__main__':
    main()
