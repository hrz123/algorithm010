- 完成了leetcode 300题以上打卡

- [数据结构与算法导图](https://github.com/hrz123/algorithm010/blob/master/Week10/数据结构与算法.png)

## 文档没有脑图的树状结构好记忆

毕业总结如果大而全显然也不合适。尽量把一些思考写下来，以后形成树状的记忆。在看洛谷上题目的时候，才感觉到自己还有很多东西都不会，(在上面还学会了蒟蒻这个词)。

但是查理芒格说过，学习并不是追求更多的知识，而是要寻找更好的决策依据。这个更好的决策依据，就是那些经过广泛验证的原理和规律，称之为思维模型。Google的创始人拉里·佩奇也说过：“让我自由地从物理规则去思考问题，而不是迎合哪些所谓的世俗智慧。”

这其实都提醒了我，也让我不断地告诉我自己，真正重要的事情，永远都是非常简单的。我要做的，就是关注本质，坚持下去。

## 数据结构与算法

1. 一维数据结构

   1. 数组

      int a[105]; // c++定义一个105容量的int数组；

      int a[105] = {5,1,3,2,4}; // 定义并初始化

      1. O(1)的随机访问
      2. O(n)的插入和删除
      3. 可以被缓存加速访问

      - 常见算法：

        - 荷兰国旗算法

        - 擂台法（对于指针，比如选择数组中最小的数，比如堆的维护）

        - 双指针：左右指针、前后指针（滑动窗口）、快慢指针

        - 与单调栈、单调双端队列进行缓存的结合，栈中判断需要索引还是只需要值

        - 快速选择（切分）：O(n)找到数组中第K大的数

        - 排序，归并和快排（注意快排要引入随机性）。归并可以用来统计逆序对，快速切分可以O(n)时间找到数组第K大的某值。

        - 二分，二分法常常跟着排序，换句话说，排序常常是二分的前置算法。二分数组的查询O(logn)

        - 前缀和，O(1)时间求前缀和，O(1)时间求区间和，但是有元素发生更改维护时间是O(n)

          ```python
          # 前缀和示例
          arr = [1,4,6,-3,5]
          pre = [0]
          p = 0
          for n in arr:
            p += n
            pre.append(p)
          
            
          pre[4]  # 前4个数的前缀和
          pre[1]  # 前1个数的前缀和
          ```

        - 树状数组，求前缀和O(logn)，求任意区间和也是O(logn)，修改任何一个元素维护的时间也是O(logn)。

          ```python
          arr = [1,4,6,-3,5]
          n = len(arr)
          BITree = [0] * (n + 1)
          def update(i, k=1):
            while i <= n:
              BITree[i] += k
              i += i & -i
          
          def getSum(i):
            s = 0
            while i:
              s += BITree[i]
              i -= i & -i
            return s
          ```

        - 一些二分操作，旋转数组（比较mid与r），局部极值数据（比较mid与mid+1），只有一个元素是一次其他都是两次的排序数组(mid是奇数就会退一个)

        - 一些离散化操作，比如用rank离散化，同时保持了数组的顺序。

   2. 链表

      1. 不同于数组·必须要连续的内存空间，链表可以使用零散的内存空间
      2. 不支持随机访问，访问为O(n)
      3. 插入和删除O(1)，但是需要前置节点。
      4. 经常需要一个dummy节点，next指向head。经常需要保留pre，cur两个指针，这样当cur需要被删掉，或者cur之前需要插入时，就有了前置节点的指针。
      5. 比数组占用空间大。
      6. 合并K个链表（n为链表平均长度，归并O(nklogk)空间复杂度O(logk)，堆存储(Onklogk)，空间复杂度O(k)）
      7. 链表排序（直接模拟归并的向上回升，可以在O(nlogn)时间复杂度，O(1)的空间复杂度内完成）
      8. 链表翻转
      9. 链表环的检测，快慢双指针
      10. 链表从后数第K个节点，前后双指针

   3. 哈希表

      1. 物理存储是数组，根据key算出数组下标，那么就可以快速的在数组中找到需要的key和value。hashmap和hashset本质上是一样的，也有在数组中存储的是指针，再通过指针找到实际存储的值。
      2. 最简单的hash函数是余数法。目前常用的有murmurhash3。
      3. 拉链法-平衡二叉树法解决冲突。

   4. 栈

      1. 很多先入后出的结构里都需要用到栈。很多时候我们可以用数组来实现栈。
      2. 在顺序表上增加限制，事情就简单了。而简单，正是我们做软件开发应该努力追求的一个目标。
      3. dfs

   5. 队列

      1. bfs

   6. 双端队列

      1. 很多语言推荐使用双端队列作为队列的实现。

2. 二维

   1. 树
      1. 二叉树（递归、分支）
      2. 学会定义适当的dfs函数，可以在解决左右问题的同时，更新所要求的问题的答案。
      3. 二叉树的前缀和
      4. AVL，红黑树
      5. 很多递归问题最终都可以转化为树的搜索问题，画出状态树。
   2. 图
      1. 邻接矩阵邻接表表示，边的出度点在前，入度点在后
      2. 如何判断有环。
         1. 定义一个全局的flags数组，大小为全部的节点数量，初始化为0，遍历所有的节点。数组中1表示正在被本轮递归访问，-1表示已经被之前的某轮递归访问过，0表示还没有被访问过。
         2. 在遍历一个节点时，如果它已经被标记上-1了，那么就返回True，因为这个节点已经被访问过了
         3. 如果它已经被标上1，那么返回False，说明我们在这一次遍历中再次访问到了这个节点。
         4. 将本节点标记为1，然后遍历邻接矩阵或者邻接表中的下一个节点，递归的调用。如果有一个返回False，就返回False。
         5. 如果都没有False返回，说明这个节点的相连节点都没有环的出现，将flags标记为-1，代表已经访问过。
      3. Dijkstra最短路径算法
      4. 图的遍历：bfs dfs （注意加visited）
      5. A*启发式搜索：在求最短路径，最小距离等问题时，我们往往使用bfs。而其实，对于一些更为靠近终点的候选者，是更有可能最快到达终点的。
   3. 字典树
   4. 并查集
   5. LRU Cache
   6. 布隆过滤器：二进制向量+一系列哈希函数

3. 合并N个有序数组，链表，排序数组，排序链表

4. 排序

   1. 所有排序

5. 字符串算法

   1. 匹配：BF、RK、KMP、BM
   2. 回文：dp，中间向两边扩散、manacher

6. 位运算

   1. N皇后，快速判重
   2. 解决一个数字出现p次，其他所有数字出现k次问题。
   3. 格雷码的规律

7. 数学

   1. 一些概率问题
   2. 数论中的一些问题
   3. 找规律问题

   
