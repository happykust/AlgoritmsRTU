# Create binary tree with check for red-black property


class TreeNode:
    """A node of the binary tree"""
    def __init__(self, val: int):
        self.left: [TreeNode, None] = None
        self.right: [TreeNode, None] = None
        self.parent: [TreeNode, None] = None
        self.value: int = val
        self.color: str = "red"

    def __str__(self):
        return f'[{self.value}]'

    def __repr__(self):
        return f'[{self.value}]'

    def __check_red_black(self, node):
        if node.left is None and node.right is None:
            return node.color == "black"

        if node.left is None:
            return node.color == "black" and node.right.color == "black"

        if node.right is None:
            return node.color == "black" and node.left.color == "black"

        return node.color == "black" and node.left.color == "black" and node.right.color == "black"


class BinaryTreeWithRBCheck:
    def __init__(self):
        self.root: [TreeNode, None] = None

    def add(self, value: int):
        if self.root is None:
            self.root = TreeNode(value)
            return

        node = self.root
        while True:
            if value < node.value:
                if node.left is None:
                    node.left = TreeNode(value)
                    node.left.parent = node
                    break
                else:
                    node = node.left
            else:
                if node.right is None:
                    node.right = TreeNode(value)
                    node.right.parent = node
                    break
                else:
                    node = node.right

    def __str__(self):
        return str(self.root)

    def __repr__(self):
        return str(self.root)

    def check_red_black(self):
        if self.root is None:
            return True

        return self.root.__check_red_black(self.root)
