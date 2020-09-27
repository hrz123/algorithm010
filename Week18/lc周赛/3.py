# 3.py
from typing import List


class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.is_death = False


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.root = TreeNode(kingName)
        self.mem = {kingName: self.root}

    def birth(self, parentName: str, childName: str) -> None:
        p_node = self.mem[parentName]
        c_node = TreeNode(childName)
        p_node.children.append(c_node)
        self.mem[childName] = c_node

    def death(self, name: str) -> None:
        node = self.mem[name]
        node.is_death = True

    def getInheritanceOrder(self) -> List[str]:
        res = []
        stack = [self.root]
        while stack:
            node = stack.pop()
            if not node.is_death:
                res.append(node.name)
            for child in reversed(node.children):
                stack.append(child)
        return res


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

def main():
    pass


if __name__ == '__main__':
    main()
