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