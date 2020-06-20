// 144. 二叉树的前序遍历.go
package main

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

// 递归的写法

func preorderTraversal(root *TreeNode) []int {
	var res []int
	dfs(root, &res)
	return res
}

func dfs(root *TreeNode, res *[]int) {
	if root != nil {
		*res = append(*res, root.Val)
		dfs(root.Left, res)
		dfs(root.Right, res)
	}
}

// 迭代的写法
func preorderTraversal(root *TreeNode) []int {
	r := make([]int, 0)
	if root == nil {
		return r
	}
	stack := StackNode{}
	stack.Push(root)
	for !stack.IsEmpty() {
		cur := stack.Pop()
		r = append(r, cur.Val)
		if cur.Right != nil {
			stack.Push(cur.Right)
		}
		if cur.Left != nil {
			stack.Push(cur.Left)
		}
	}
	return r
}

type StackNode struct {
	data [1000]*TreeNode
	pos  int
}

func NewStackNode() *StackNode {
	return &StackNode{}
}
func (s *StackNode) IsEmpty() bool {
	return s.pos == 0
}
func (s *StackNode) Push(n *TreeNode) {
	s.data[s.pos] = n
	s.pos++
}
func (s *StackNode) Pop() (n *TreeNode) {
	s.pos--
	return s.data[s.pos]
}
