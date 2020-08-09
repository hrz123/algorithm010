package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// 递归的写法
func inorderTraversal(root *TreeNode) []int {
	var xs []int
	if root != nil {
		xs = append(xs, inorderTraversal(root.Left)...)
		xs = append(xs, root.Val)
		xs = append(xs, inorderTraversal(root.Right)...)
	}
	return xs
}

// 迭代的写法
func inorderTraversal(root *TreeNode) []int {
	var todo []*TreeNode
	var ans []int

	node := root
	for node != nil || len(todo) > 0 {
		for node != nil {
			todo = append(todo, node)
			node = node.Left
		}
		node = todo[len(todo)-1]
		todo = todo[:len(todo)-1]
		ans = append(ans, node.Val)
		node = node.Right
	}
	return ans
}

// 莫里斯遍历
func inorderTraversal(root *TreeNode) []int {
	var ans []int
	cur := root
	var pre *TreeNode
	for cur != nil {
		if cur.Left == nil { // 如果没有左子树
			ans = append(ans, cur.Val)
			cur = cur.Right // 移到下一个右节点
		} else { // 如果有左子树
			pre = cur.Left
			for pre.Right != nil { // 找到最右节点
				pre = pre.Right
			}
			pre.Right = cur // 将cur节点放到pre的右子节点上
			temp := cur     // 存储cur节点
			cur = cur.Left  // 将cur指向当前新数的根节点
			temp.Left = nil // 置原来根节点的左子节点为null，防止无限循环
		}
	}
	return ans
}
