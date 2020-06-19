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

//var aaa []int
//
//func postorder(root *Node) []int {
//	aaa = []int{}
//	dfs(root)
//	return aaa
//}
//
//func dfs(root *Node) {
//	if root != nil {
//		for _, n := range root.Children {
//			dfs(n)
//		}
//		aaa = append(aaa, root.Val) //后序输出
//	}
//}

func postorder(root *Node) []int {
	res := []int{}
	_dfs(root, &res)
	return res
}

func _dfs(root *Node, res *[]int) {
	if root != nil {
		for _, n := range root.Children {
			_dfs(n, res)
		}
		*res = append(*res, root.Val) //后序输出
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
