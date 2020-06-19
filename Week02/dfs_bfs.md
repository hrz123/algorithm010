# DFS BFS

## DFS 代码 - 递归写法

```python
visited = set() # 和树中的DFS最大区别

def dfs(node, visited):
    if node in visited: # terminator
        # already visited
        return
    
    visited.add(node)

    # process current node here.
    ...
    for next_node in node.children():
        if not next_node in visited:
            dfs(next_node, visited)
```

## BFS代码

```python
def BFS(graph, start, end):
    queue = [[start]]

    visited = set() # 和树中的BFS的最大区别          
    
    while queue:
        node = queue.pop()
        visited.add(node)

        process(node)
        nodes = generate_related_nodes(node)
        queue.push(nodes)
```
