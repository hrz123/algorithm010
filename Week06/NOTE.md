学习笔记



## 动态规划

分治+回溯+递归+动态规划

将一个复杂的问题分解为子问题，同时寻找重复性。



递归的模板

```java
public void recur(int level, int param) {
  // terminator
  if (level > MAX_LEVEL) {
    // process result
    return;
  }
  
  // process current logic
  process(level, param);
  
  // drill down
  recur(leve: level+1, newParam);
  
  // restore current status
}
```



分治 divide & conquer

```python
def divide_conquer(problem, param1, param2, ...):
  // recursion terminator
  if problem is None:
    print_result
    return
  
  # process data
  data = prepare_data(problem)
  subproblem = split_problem(problem, data)
  
  # conquer subproblems
  subresult1 = self.divide_conquer(subproblems[1], p1, ...) 
  subresult2 = self.divide_conquer(subproblems[2], p2, ...) 
  subresult3 = self.divide_conquer(subproblems[3], p3, ...) 
  ...
  
  # process and generate the final result
  result = process_result(subresult1, subresult2, subresult3, ...)
  
  # revert the current level status
```



wiki上对动态递推的关键解释：

Simplifying a complicated problem by breaking it down into simpler subproblems.(in a recursive manner)



与递推和分治的关键对比

- **动态递推**和**递归**或者**分治**没有根本上的区别（关键看有无最有子结构）
- **共性：找到重复子问题**
- 差异性：最有子结构、中途可以**淘汰**次优解

傻递归或者傻分支的话，经常是指数级的复杂度。可以降到多项式级别。

DP三部曲

a.定义子问题
b.定义状态数组
c.定义递推方程



并查集

1.小弟老大

2.帮派识别

3.两种优化方式



## 滑动窗口

详解「滑动窗口」这种高级双指针技巧的算法框架，带你秒杀几道难度较大的子字符串匹配问题：

[最小覆盖子串](https://leetcode-cn.com/problems/minimum-window-substring/)

[找到字符串中所有字母异位词](https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/)

[无重复字符的最长子串](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/)

[字符串的排列](https://leetcode-cn.com/problems/permutation-in-string/)

### 滑动窗口防滑记

链表子串数组题，用双指针别犹豫。

双指针家三兄弟，各个都是万人迷。



快慢指针最神奇，链表操作无压力。

归并排序找中点，链表成环搞判定。



左右指针最常见，左右两端相向行。

反转数组要靠它，二分搜索是弟弟。



滑动窗口老猛男，子串问题全靠它。

左右指针滑窗口，一前一后齐头进。

自称十年老司机，怎料农村道路滑。

一不小心滑倒了，鼻青脸肿少颗牙。

算法思想很简单，出了bug想升天。

