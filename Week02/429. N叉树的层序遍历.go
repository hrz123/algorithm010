// 429. N叉树的层序遍历.go
package main

/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Children []*Node
 * }
 */

func levelOrder(root *Node) [][]int {
	var res [][]int
	if root == nil {
		return res
	}
	queue := []*Node{root}
	var output []int
	size := 0
	for len(queue) > 0 {
		size = len(queue)
		output = []int{}
		for _, node := range queue {
			output = append(output, node.Val)
			for _, child := range node.Children {
				queue = append(queue, child)
			}
		}
		queue = queue[size:]
		res = append(res, output)

	}
	return res
}
