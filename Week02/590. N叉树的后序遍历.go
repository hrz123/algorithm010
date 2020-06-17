// 590. N叉树的后序遍历.go
package main

/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Children []*Node
 * }
 */

type Node struct {
	Val      int
	Children []*Node
}

var res []int

func postorder(root *Node) []int {
	res = []int{}
	dfs(root)
	return res
}

func dfs(root *Node) {
	if root != nil {
		for _, n := range root.Children {
			dfs(n)
		}
		res = append(res, root.Val) //后序输出
	}
}

func postorder(root *Node) []int {
	var res []int
	if root == nil {
		return res
	}
	var stack = []*Node{root}
	for 0 < len(stack) {
		root = stack[len(stack)-1]
		res = append(res, root.Val)
		stack = stack[:len(stack)-1]
		l := len(root.Children)
		for i := 0; i < l; i++ {
			stack = append(stack, root.Children[i]) //入栈
		}
	}

	l := len(res) - 1
	for i := 0; i < l/2+1; i++ {
		res[i], res[l-i] = res[l-i], res[i]
	}
	return res
}
