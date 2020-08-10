# 235. 二叉搜索树的最近公共祖先.py


# 没有重复节点的二叉搜索树
# 直觉，顺着路，只要节点的值 p<=val<=q就找到了
# 证明下
# 只要p<=val<=q， 那么p一定在val的左节点，q一定在val的右节点，val是p,q的公共祖先
# 再证明val是p，q的最近公共祖先
# 反证法。val已经是p，q的公共祖先了，如果存在p,q的最近公共祖先k，
# 那么k一定在val的左子树或者右子树上，如果k在左子树上，那么q也在左子树上，q就小于val了，不可能
# k在右子树上同理，证毕。val是pq的最近公共祖先

# 算法
# p<q
# while root
# if   p<=root.val<=q  return root.val
# else if q < root.val root = root.r
# else                 root = root.r
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p
        while root:
            if p.val <= root.val <= q.val:
                return root
            elif root.val > q.val:
                root = root.left
            else:
                root = root.right
        return


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p
        if not root or p.val <= root.val <= q.val:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left:
            return left
        if right:
            return right
        return


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p
        while root:
            if p.val <= root.val <= q.val:
                return root
            if root.val > q.val:
                root = root.left
            else:
                root = root.right
        return


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p
        while root:
            if p.val <= root.val <= q.val:
                return root
            if root.val > q.val:
                root = root.left
            else:
                root = root.right
        return


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p
        while root:
            if p.val <= root.val <= q.val:
                return root
            if root.val > q.val:
                root = root.left
            else:
                root = root.right
        return


def main():
    pass


if __name__ == '__main__':
    main()
