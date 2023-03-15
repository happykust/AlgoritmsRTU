class TreeNode:
    """A node of the binary tree"""
    def __init__(self, val: int):
        self.left: [TreeNode, None] = None
        self.right: [TreeNode, None] = None
        self.parent: [TreeNode, None] = None
        self.value: int = val
        self.balance: int = 0

    def __str__(self):
        return f'[{self.value}]'

    def __repr__(self):
        return f'[{self.value}]'


class AVLTree:
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

    def __check_balance(self, node: TreeNode):
        if node.left is None and node.right is None:
            node.balance = 0
            return node.balance

        if node.left is None:
            node.balance = 1
            return node.balance

        if node.right is None:
            node.balance = -1
            return node.balance

        node.balance = self.__check_balance(node.left) - self.__check_balance(node.right)
        return node.balance

    def check_balance(self):
        if self.root is None:
            return "Tree is empty"

        return self.__check_balance(self.root)

    def __rotate_left(self, node: TreeNode):
        right = node.right
        node.right = right.left
        if right.left is not None:
            right.left.parent = node
        right.parent = node.parent
        if node.parent is None:
            self.root = right
        elif node == node.parent.left:
            node.parent.left = right
        else:
            node.parent.right = right
        right.left = node
        node.parent = right

    def __rotate_right(self, node: TreeNode):
        left = node.left
        node.left = left.right
        if left.right is not None:
            left.right.parent = node
        left.parent = node.parent
        if node.parent is None:
            self.root = left
        elif node == node.parent.right:
            node.parent.right = left
        else:
            node.parent.left = left
        left.right = node
        node.parent = left

    def __check_balance_and_rebalance(self, node: TreeNode):
        if node is None:
            return

        self.__check_balance_and_rebalance(node.left)
        self.__check_balance_and_rebalance(node.right)

        if node.balance > 1:
            if node.left.balance < 0:
                self.__rotate_left(node.left)
            self.__rotate_right(node)
        elif node.balance < -1:
            if node.right.balance > 0:
                self.__rotate_right(node.right)
            self.__rotate_left(node)

