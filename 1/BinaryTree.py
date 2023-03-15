
class TreeNode:
    """A node of the binary tree"""
    def __init__(self, val: int):
        self.left: [TreeNode, None] = None
        self.right: [TreeNode, None] = None
        self.value: int = val


class Tree:
    """The main binary tree class"""
    def __init__(self):
        self.root: [TreeNode, None] = None

    def get_root(self):
        return self.root

    def add_value(self, value: int) -> None:
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._add_to_node(value, self.root)

    def _add_to_node(self, value: int, node: TreeNode) -> None:
        if value < node.value:
            if node.left is not None:
                self._add_to_node(value, node.left)
            else:
                node.left = TreeNode(value)
        else:
            if node.right is not None:
                self._add_to_node(value, node.right)
            else:
                node.right = TreeNode(value)

    def print_tree(self) -> None:
        if self.root is not None:
            self._print_node_tree(self.root)

    def _print_node_tree(self, node: TreeNode) -> None:
        if node is not None:
            print(f'{node.value}')
            print(f'{self._print_node_tree(node.left)} ----- {self._print_node_tree(node.right)}')
            #self.print_node_tree(node.left)
            #print(f'{node.value}')
            #self.print_node_tree(node.right)

    def get_height(self) -> int:
        if self.root is not None:
            return self._get_node_height(self.root)
        return 0

    def _get_node_height(self, node: TreeNode) -> int:
        if node is None:
            return 0
        return max(self._get_node_height(node.left), self._get_node_height(node.right)) + 1

    def find(self, value: int) -> bool:
        if self.root is not None:
            return self._find_node(value, self.root)
        return False

    def _find_node(self, value: int, node: TreeNode) -> bool:
        if node is None:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._find_node(value, node.left)
        else:
            return self._find_node(value, node.right)

    def _get_max_value(self, left):
        if left.right is not None:
            return self._get_max_value(left.right)
        return left

    def delete_node(self, value: int) -> None:
        if self.root is not None:
            self._delete_node_value(value, self.root)

    def _delete_node_value(self, value: int, node: TreeNode) -> None:
        if node is None:
            return
        if value < node.value:
            self._delete_node_value(value, node.left)
        elif value > node.value:
            self._delete_node_value(value, node.right)
        else:
            if node.left is not None and node.right is not None:
                tmp = self._get_max_value(node.left)
                node.value = tmp.value
                self._delete_node_value(tmp.value, node.left)
            elif node.left is not None:
                node.value = node.left.value
                node.left = None
            elif node.right is not None:
                node.value = node.right.value
                node.right = None
            else:
                node = None


#    3
# 0     4
#   2      8

tree = Tree()

tree.add_value(3)
tree.add_value(4)
tree.add_value(0)
tree.add_value(8)
tree.add_value(2)

tree.print_tree()
