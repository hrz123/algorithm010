// 589. N叉树的前序遍历.go
package main

/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Children []*Node
 * }
 */
// 递归

var res []int

func preorder(root *Node) []int {
	helper(root)
	return res
}

func helper(node *Node) {
	if node == nil {
		return
	}
	res = append(res, node.Val)
	for _, child := range node.Children {
		helper(child)
	}
}

var res []int

func preorder(root *Node) []int {
	helper(root, &res)
	return res
}

func helper(node *Node, res *[]int) {
	if node == nil {
		return
	}
	*res = append(*res, node.Val)
	for _, child := range node.Children {
		helper(child, res)
	}
}

// 迭代
//func preorder(root *Node) []int {
//	var aaa []int
//	var stack = []*Node{root}
//	for 0 < len(stack) {
//		for root != nil {
//			aaa = append(aaa, root.Val) //前序输出
//			if 0 == len(root.Children) {
//				break
//			}
//			for i := len(root.Children) - 1; 0 < i; i-- {
//				stack = append(stack, root.Children[i]) //入栈
//			}
//			root = root.Children[0]
//		}
//		root = stack[len(stack)-1]
//		stack = stack[:len(stack)-1]
//	}
//	return aaa
//}
