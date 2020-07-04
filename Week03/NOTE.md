# 学习笔记


## 必须背下来的递归代码模板

```python
# Python
def recursion(level, param1, param2, ...):
    # recursion terminator
    if level > MAX_LEVEL:
        process_result
        return
    
    # process logic in current level
    process(level, data...)

    # drill down
    self.recursion(level + 1, p1, ...)

    # reverse the current level status if needed
```

```java
// Java
public void recur(int level, int param) { 
  // terminator 
  if (level > MAX_LEVEL) { 
    // process result 
    return; 
  }
  // process current logic 
  process(level, param); 
  // drill down 
  recur( level: level + 1, newParam); 
  // restore current status 
 
}
```

## 分治代码模板

```python3
# python
def divide_conquer(problem, param1, param2, ...):
    # recursion terminator
        if problem is None:
        print_result
        return
    # prepare data
    data = prepare_data(problem)
    subproblems = split_problem(problem, data)
    # conquer subproblems
    subresult1 = self.divide_conquer(subproblems[0], p1, ...)
    subresult2 = self.divide_conquer(subproblems[1], p1, ...) 
    subresult3 = self.divide_conquer(subproblems[2], p1, ...)
    …
    # process and generate the final result 
    result = process_result(subresult1, subresult2, subresult3, …)
	
    # revert the current level states
```

## 关于回溯的剪枝问题

最后，由于回溯算法的时间复杂度很高，因此，如果在遍历的时候，如果能够提前知道这一条分支不能搜索到满意的结果，就可以提前结束，这一步操作称之为剪枝。



回溯算法会大量应用“剪枝”技巧达到以加快搜索速度。有些时候，需要做一些预处理工作（例如排序）才能达到剪枝的目的。预处理工作虽然也消耗时间，但一般能够剪枝节约的时间更多。还有正是因为回溯问题本身时间复杂度就很高，所以能用空间换时间就尽量使用空间。否则时间消耗又上去了。
