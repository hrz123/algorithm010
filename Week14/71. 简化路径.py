# 71. 简化路径.py
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")

        for item in path:
            if item == "..":
                if stack:
                    stack.pop()
            elif item and item != ".":
                stack.append(item)
        return "/" + "/".join(stack)


def main():
    pass


if __name__ == '__main__':
    main()
