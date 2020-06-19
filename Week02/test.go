// test.go
package main

var aaa []int

func _preorder(root *Node) []int {
	aaa = []int{}
	helper(root)
	return aaa
}

func _helper(node *Node) {
	if node == nil {
		return
	}
	aaa = append(aaa, node.Val)
	for _, child := range node.Children {
		helper(child)
	}
}
