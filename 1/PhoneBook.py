class TreeNode:
    def __init__(self, value: [int], name: str):
        self.value: [int] = value
        self.name: str = name
        self.left: [TreeNode, None] = None
        self.right: [TreeNode, None] = None

    def __str__(self):
        return f'{self.value} {self.name}'

    def __repr__(self):
        return f'{self.value} {self.name}'

    def __eq__(self, other):
        return self.value == other.value

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        # Дичь для красивого вывода дерева.
        # Сам хз, как оно работает =)
        if self.right is None and self.left is None:
            line = '%s' % f'{self.name} {self.value}'
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % f'{self.name} {self.value}'
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % f'{self.name} {self.value}'
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % f'{self.name} {self.value}'
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


class PhoneBookTree:
    def __init__(self):
        self.root: [TreeNode, None] = None

    def get_root(self):
        return self.root

    def add_value(self, value: [int], name: str) -> None:
        if self.root is None:
            self.root = TreeNode(value, name)
        else:
            self._add_to_node(value, name, self.root)

    def _add_to_node(self, value: [int], name: str, node: TreeNode) -> None:
        if value < node.value:
            if node.left is not None:
                self._add_to_node(value, name, node.left)
            else:
                node.left = TreeNode(value, name)
        else:
            if node.right is not None:
                self._add_to_node(value, name, node.right)
            else:
                node.right = TreeNode(value, name)

    def display(self):
        if self.root is not None:
            return self.root.display()
        print("Tree is empty.")

    def find_name(self, name: str) -> [TreeNode, None]:
        if self.root is not None:
            return self._find_name(name, self.root)
        else:
            return None

    def _find_name(self, name: str, node: TreeNode) -> [TreeNode, None]:
        if name == node.name:
            return node
        elif name < node.name and node.left is not None:
            return self._find_name(name, node.left)
        elif name > node.name and node.right is not None:
            return self._find_name(name, node.right)

    def _find_min(self, node: TreeNode) -> TreeNode:
        if node.left is None:
            return node
        else:
            return self._find_min(node.left)

    def delete_by_name(self, name: str) -> None:
        if self.root is not None:
            self.root = self._delete_by_name(name, self.root)

    def _delete_by_name(self, name: str, node: TreeNode) -> [TreeNode, None]:
        if node is None:
            return node
        if name < node.name:
            node.left = self._delete_by_name(name, node.left)
        elif name > node.name:
            node.right = self._delete_by_name(name, node.right)
        else:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                temp = self._find_min(node.right)
                node.value = temp.value
                node.name = temp.name
                node.right = self._delete_by_name(temp.name, node.right)
        return node


tree = PhoneBookTree()
tree.add_value([1, 2, 3], 'Ahn')
tree.add_value([1, 2, 4], 'B')
tree.add_value([1, 2, 5], 'Jill')
tree.add_value([1, 2, 6], 'uuuu')
tree.add_value([1, 2, 7], 'Jenny')
tree.add_value([1, 2, 8], 'Jen')

tree.display()
