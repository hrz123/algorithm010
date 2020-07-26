

# 学习笔记

## Trie，字典树完成 单词搜索II 问题的时间复杂度

遍历矩阵 O(M*M)

dfs有四个方向 4

每个方向最长走K，K为单词平均长度

所以dfs 4^K的复杂度

所以使用字典树的时间复杂度O(M\*M\*4^K)这样的时间复杂度，最坏情况。

因为有剪枝，所以实际上运行要更快一点。

## 双向bfs模板

双向bfs的模板有两种，一种用visited记录已经访问的节点，在新一层处更新，一种用available记录可以使用的节点，在新一层处删除

输出路径长度的值，a->b路径长度为1

```python
class Solution:
    def biDirectionBFS(cls, start: str, end: str, elems: List[str]) -> int:
        elems = set(elems)
        if end not in elems:
            return -1
        bq, eq, nq, visited, n = {start}, {end}, set(), set(), len(end)
        res = 0
        while bq:
            elems -= bq
            res += 1
            for x in bq:
                for y in [x[:i] + c + x[i + 1:] for i in range(n) for c in "available chars"]:
                    if y in elems:
                        if y in eq:
                            return res
                        nq.add(y)
            bq, nq = nq, set()
            if len(bq) > len(eq):
                bq, eq = eq, bq
        return -1
```

输出整个路径，start -> t -> t -> end

```python
class Solution:
    def findLadders(cls, beginWord: str, endWord: str,
                    wordList: List[str]) -> List[List[str]]:
        words = set(wordList)
        if endWord not in words:
            return []
        bq, eq, nq, n, found, rev, tree = {beginWord}, {endWord}, set(), \
                                          len(endWord), False, False, \
                                          defaultdict(set)

        while bq and not found:
            words -= bq
            for x in bq:
                for y in [x[:i] + c + x[i + 1:] for i in range(n) for c in
                          "qwertyuiopasdfghjklzxcvbnm"]:
                    if y in words:
                        if y in eq:
                            found = True
                        else:
                            nq.add(y)
                        tree[y].add(x) if rev else tree[x].add(y)
            bq, nq = nq, set()
            if len(bq) > len(eq):
                bq, eq, rev = eq, bq, not rev

        def bt(x):
            return [[x]] if x == endWord else [[x] + rest for y in tree[x]
                                               for rest in bt(y)]

        return bt(beginWord)
```

## 从普通bfs到启发式搜索(heuristic search)

```python
def bfs(graph, start, end):
    queue = []
    queue.append([start])
    visited.add(start)

    while queue:
        node = queue.pop()  # can we add more intelligence here?
        visited.add(node)

        process(node)
        nodes = generate_related_nodes(node)
        queue.push(nodes)
```

A* search

```python
def AstarSearch(graph, start, end):
    pq = collections.priority_queue()  # 优先级 -> 估价函数
    pq.append([start])
    visited.add(start)

    while pq:
        node = pq.pop()  # can we add more intelligence here?
        visited.add(node)

        process(node)
        nodes = generate_related_nodes(node)
        unvisited = [node for node in nodes if node not in visited]
        pq.push(nodes)
```

## AVL树

- 平衡因子 Balance Factor，是它的左子树的高度减去它的右子树的高度（有时相反）。balance factor = {-1, 0, 1}
- 通过旋转操作来进行平衡（四种）

保证任何一个结点的平衡因子都只在{-1, 0, 1}

### 旋转操作

1. 左旋
2. 右旋
3. 左右旋
4. 右左旋

#### 子树形态：右右子树 -> 左旋 (单一的右子树且单一的右子树)

#### 子树形态：左左子树 -> 右旋 (单一的左子树且单一的左子树)

#### 子树形态：左右子树 -> 左右旋 (单一的左子树且单一的右子树)

#### 子树形态：右左子树 -> 右左旋 (单一的右子树且单一的左子树)

### AVL总结

1. 平衡二叉搜索树，而且是自平衡的

2. 每个结点存balance factor = {-1, 0, 1}

3. 四种旋转操作

   不足：结点需要存储额外信息（int类型）、且调整次数频繁（加减）

   --> 于是近似平衡二叉树

## 红黑树

- 近似平衡的二叉搜索树
- 能够确保任何一个结点的左右子树的 **高度差小于两倍**

具体来说

1. 每个结点要么是红色，要么是黑色。
2. 根结点是黑色。
3. 每个叶结点（NIL结点，空结点）是黑色的。
4. 不能有相邻接的两个红色结点。
5. 从任一结点到其每个叶子的所有路径都包含相同数目的黑色结点。

查询时间复杂度O(log2_and_minus_1(n))，同时调整时间较小

**关键性质：从根到叶子的最长的可能路径不多于最短的可能路径的两倍长。**

## 对比

- AVL trees provide **faster lookups** than Red Black Trees because they are **more strictly balanced**.
  - AVL有更快的查询，因为更严格的平衡

- Red Black Trees provide **faster insertion and removal** operations than AVL trees as fewer rotations are done due to relatively relaxed balancing.
  - 红黑树插入和删除的操作更快，也是因为不严格平衡
- AVL trees store balance **factors or heights** with each node, thus requires storage for an integer per node whereas Red Black Tree requires only 1 bit of information per node.
  - AVL每个结点需要存储平衡因子，占一个int，而红黑树只需要一个bit
- Red Black Trees are used in most of the **language libraries like map, multimap, multiset in C++** whereas AVL trees are used in **databases** where faster retrievals are required.
  - 红黑树在很多语言的库中使用，比如C++中的map，multimap，multiset，而AVL树更广泛用于数据库中，因为查询操作的速度要求更块
  - 读操作很多，写操作很少的时候用AVL
  - 插入操作比较多，或者插入操作和读操作一半一半，一般用红黑树（比较简洁好实现）