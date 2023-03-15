class TreeNode:
    def __init__(self, value: int):
        self.value: int = value
        self.left: [TreeNode, None] = None
        self.right: [TreeNode, None] = None
        self.parent: TreeNode
        self.balance: int = 0

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""

        # No child.
        if self.right is None and self.left is None:
            line = '%s' % f'{self.value} - {self.balance}'
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % f'{self.value} - {self.balance}'
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % f'{self.value} - {self.balance}'
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % f'{self.value} - {self.balance}'
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


class BinaryTreeWithBalanceCheck:
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


tree = BinaryTreeWithBalanceCheck()
tree.add(5)
tree.add(3)
tree.add(7)
tree.add(2)
tree.add(4)
tree.add(6)

tree.check_balance()
tree.root.display()
