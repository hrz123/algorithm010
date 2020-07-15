# 297. 二叉树的序列化与反序列化.py
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')

        vals = []
        doit(root)
        return ' '.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def doit():
            val = next(vals)
            if val == '#':
                return
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node

        vals = iter(data.split())
        return doit()


# 以下为自我练习

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        vals = []

        def doit(node):
            # recursion terminator
            # process current level logic
            if node:
                vals.append(str(node.val))
                # drill down
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')

        doit(root)
        return ' '.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def doit():
            val = next(vals)
            if val == '#':
                return
            node = TreeNode(val)
            node.left = doit()
            node.right = doit()
            return node

        vals = iter(data.split())

        return doit()


# dfs
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        values = []

        def helper(node):
            if not node:
                values.append('#')
            else:
                values.append(str(node.val))
                helper(node.left)
                helper(node.right)

        helper(root)
        return ' '.join(values)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        values = iter(data.split())

        def helper():
            val = next(values)
            if val == '#':
                return
            node = TreeNode(val)
            node.left = helper()
            node.right = helper()
            return node

        return helper()


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []

        def doit(root):
            if not root:
                res.append('#')
                return
            res.append(str(root.val))
            doit(root.left)
            doit(root.right)

        doit(root)

        return ' '.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = iter(data.split())

        def doit():
            val = next(data)
            if val == '#':
                return None
            root = TreeNode(val)
            root.left = doit()
            root.right = doit()
            return root

        return doit()


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

def main():
    codec = Codec()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    res = codec.serialize(root)
    print(res)
    node = codec.deserialize(res)
    print(node)

    def print_tree(node):
        if not node:
            print('#', end=' ')
            return
        print(node.val, end=' ')
        print_tree(node.left)
        print_tree(node.right)

    print_tree(node)


if __name__ == '__main__':
    main()
