# 621. 任务调度器.py
from collections import defaultdict, Counter
from typing import List


# 子问题
# 定义状态数组
# 递推方程

# 思路
# 完成所有任务的最短时间取决于出现次数最多的任务数量
# 看下题目给出的例子
# 输入：tasks = ["A", "A", "A", "B", "B", "B", n = 2
# 输出：8
# 执行顺序：A -> B -> (待命) -> A -> B -> (待命) -> A -> B
# 因为相同任务必须要有时间片为n的间隔，所以我们先把出现次数最多的任务A安排上（当然你也可以选择任务B)
# 例子中n = 2。那么任意两个任务A之间都必须有间隔2个单位的时间：
# A -> time unit -> time unit -> A -> time unit -> time unit -> A
# 中间间隔的单位时间可以用来安排别的任务，也可以处于"待命"状态。当然，为了使总任务时间最短，
# 我们尽可能地把单位时间分配给其他任务。现在把任务B安排上：
# A -> B -> time unit -> A -> B -> time unit -> A -> B
# 很容易观察到，前面两个A任务一定会固定跟着2个单位时间的间隔。最后一个A之后是否还有任务跟随取决于
# 是否存在与任务A出现次数相同的任务。
# 该例子的计算过程为：
# (任务A出现的次数 - 1) * (n + 1) + (出现次数为3的任务个数），即：
# (3 - 1) * (2 + 1) + 2 = 8
# 所以整体的解题的步骤如下：
# 1. 计算每个任务出现的次数
# 2. 找出出现次数最多的任务，假设出现次数为 x
# 3. 计算至少需要的时间 (x-1) * (n+1)，记为min_time
# 4. 计算出现次数为 x 的任务总数 count_parts，计算最终结果为min_time + count_parts
# 特殊情况
# 然而存在一种特殊情况，例如：
# 输入：tasks = ["A", "A", "A", "B", "B", "B", "C", "C", "D", "D"], n=2
# 输出：10
# 执行顺序：A -> B -> C -> A -> B -> D -> A -> B -> C -> D
# 此时如果按照上述方法计算将得到结果为 8，比数组总长度 10 要小，应返回数组长度
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        size = len(tasks)

        if size <= 1:
            return size

        # 用于记录每个任务出现的次数
        counter = defaultdict(int)
        for task in tasks:
            counter[task] += 1

        # 按任务出现的次数大小从大到小排序
        task_sort = sorted(counter.items(), key=lambda x: x[1], reverse=True)

        # 出现最多次任务的次数
        max_task_count = task_sort[0][1]
        # 至少需要的最短时间
        res = (max_task_count - 1) * (n + 1)

        for sort in task_sort:
            if sort[1] == max_task_count:
                res += 1
            else:
                break

        # 如果结果比任务数量少，咋返回任务数量
        return res if res > size else size


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks).values()
        M = max(task_counts)
        Mct = tuple(task_counts).count(M)
        return max(len(tasks), (M - 1) * (n + 1) + Mct)


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks).values()
        max_task_count = max(task_counts)
        num_max_task_counts = tuple(task_counts).count(max_task_count)
        return max(len(tasks),
                   (max_task_count - 1) * (n + 1) + num_max_task_counts)


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        size = len(tasks)
        if size <= 1:
            return size
        counter = defaultdict(int)
        for t in tasks:
            counter[t] += 1
        max_task_count = max(counter.values())
        num_max_task_counts = tuple(counter.values()).count(max_task_count)

        return max(size, (max_task_count - 1) * (n + 1) + num_max_task_counts)


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = [0] * 26
        start = ord('A')
        for t in tasks:
            counter[ord(t) - start] += 1
        _max_count = 0
        num_max_count = 0
        for c in counter:
            if c > _max_count:
                _max_count = c
                num_max_count = 1
            elif c == _max_count:
                num_max_count += 1

        return max((_max_count - 1) * (n + 1) + num_max_count, len(tasks))


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = [0] * 26
        start = ord('A')
        for t in tasks:
            counter[ord(t) - start] += 1
        _max_count = max(counter)
        num_max_count = counter.count(_max_count)
        return max((_max_count - 1) * (n + 1) + num_max_count, len(tasks))


# 充分利用python api
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks).values()
        _max_count = max(counter)
        num_max_count = tuple(counter).count(_max_count)
        return max((_max_count - 1) * (n + 1) + num_max_count, len(tasks))


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks).values()
        _max_count = max(counter)
        num_max_count = tuple(counter).count(_max_count)
        return max((_max_count - 1) * (n - 1) + num_max_count, len(tasks))


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = defaultdict(int)
        for t in tasks:
            counter[t] += 1
        _max_count = max(counter.values())
        num_max_count = 0
        for v in counter.values():
            if v == _max_count:
                num_max_count += 1
        return max((_max_count - 1) * (n + 1) + num_max_count, len(tasks))


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks).values()
        _max_count = max(counter)
        _num_max_count = tuple(counter).count(_max_count)
        return max((_max_count - 1) * (n + 1) + _num_max_count, len(tasks))


def main():
    sol = Solution()

    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    res = sol.leastInterval(tasks, n)
    print(res)

    tasks = ["A", "A", "A", "B", "B", "B", "C", "C", "D", "D"]
    n = 2
    res = sol.leastInterval(tasks, n)
    print(res)


if __name__ == '__main__':
    main()
