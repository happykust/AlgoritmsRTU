class Node:
    def __init__(self, key, color):
        self.key = key
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return str(self.key)

    def __repr__(self):
        return str(self.key)

    def __iter__(self):
        if self.left:
            yield from self.left
        yield self.key
        if self.right:
            yield from self.right

    def __contains__(self, key):
        if self.key == key:
            return True
        elif key < self.key and self.left:
            return key in self.left
        elif key > self.key and self.right:
            return key in self.right
        return False

    def __len__(self):
        return 1 + len(self.left) + len(self.right) if self.left or self.right else 1

    def __min(self):
        if self.left:
            return self.left.__min()
        return self

    def __max(self):
        if self.right:
            return self.right.__max()
        return self

    def __successor(self):
        if self.right:
            return self.right.__min()
        node = self
        while node.parent and node == node.parent.right:
            node = node.parent
        return node.parent

    def __predecessor(self):
        if self.left:
            return self.left.__max()
        node = self
        while node.parent and node == node.parent.left:
            node = node.parent
        return node.parent

    def __replace(self, node):
        if self.parent:
            if self == self.parent.left:
                self.parent.left = node
            else:
                self.parent.right = node
        if node:
            node.parent = self.parent

    def __rotate_left(self):
        node = self.right
        self.right = node.left
        if node.left:
            node.left.parent = self
        node.parent = self.parent
        if self.parent:
            if self == self.parent.left:
                self.parent.left = node
            else:
                self.parent.right = node
        node.left = self
        self.parent = node

    def __rotate_right(self):
        node = self.left
        self.left = node.right
        if node.right:
            node.right.parent = self
        node.parent = self.parent
        if self.parent:
            if self == self.parent.right:
                self.parent.right = node
            else:
                self.parent.left = node
        node.right = self
        self.parent = node

    def __insert(self, key):
        if key < self.key:
            if self.left:
                return self.left.__insert(key)
            else:
                self.left = Node(key, 'red')
                self.left.parent = self
                return self.left
        else:
            if self.right:
                return self.right.__insert(key)
            else:
                self.right = Node(key, 'red')
                self.right.parent = self
                return self.right

    def __insert_fixup(self, node):
        while node.parent and node.parent.color == 'red':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle and uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        node.__rotate_left()
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    node.parent.parent.__rotate_right()
            else:
                uncle = node.parent.parent.left
                if uncle and uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        node.__rotate_right()
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    node.parent.parent.__rotate_left()
        self.root.color = 'black'

    def __delete(self, key):
        if key < self.key:
            if self.left:
                return self.left.__delete(key)
        elif key > self.key:
            if self.right:
                return self.right.__delete(key)
        else:
            if self.left and self.right:
                node = self.right.__min()
                self.key = node.key
                return self.right.__delete(node.key)
            elif self.left:
                self.__replace(self.left)
            elif self.right:
                self.__replace(self.right)
            else:
                self.__replace(None)
            return self

    def __delete_fixup(self, node):
        while node != self.root and (not node or node.color == 'black'):
            if node == node.parent.left:
                sibling = node.parent.right
                if sibling.color == 'red':
                    sibling.color = 'black'
                    node.parent.color = 'red'
                    node.parent.__rotate_left()
                    sibling = node.parent.right
                if (not sibling.left or sibling.left.color == 'black') and (not sibling.right or sibling.right.color == 'black'):
                    sibling.color = 'red'
                    node = node.parent
                else:
                    if not sibling.right or sibling.right.color == 'black':
                        sibling.left.color = 'black'
                        sibling.color = 'red'
                        sibling.__rotate_right()
                        sibling = node.parent.right
                    sibling.color = node.parent.color
                    node.parent.color = 'black'
                    sibling.right.color = 'black'
                    node.parent.__rotate_left()
                    node = self.root
            else:
                sibling = node.parent.left
                if sibling.color == 'red':
                    sibling.color = 'black'
                    node.parent.color = 'red'
                    node.parent.__rotate_right()
                    sibling = node.parent.left
                if (not sibling.left or sibling.left.color == 'black') and (not sibling.right or sibling.right.color == 'black'):
                    sibling.color = 'red'
                    node = node.parent
                else:
                    if not sibling.left or sibling.left.color == 'black':
                        sibling.right.color = 'black'
                        sibling.color = 'red'
                        sibling.__rotate_left()
                        sibling = node.parent.left
                    sibling.color = node.parent.color
                    node.parent.color = 'black'
                    sibling.left.color = 'black'
                    node.parent.__rotate_right()
                    node = self.root
        if node:
            node.color = 'black'


class RBTree(object):
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root:
            self.root.__insert(key)
        else:
            self.root = Node(key, 'black')
        self.root.__insert_fixup(key)

    def delete(self, key):
        if self.root:
            node = self.root.__delete(key)
            if node:
                node.__delete_fixup(key)

    def search(self, key):
        if self.root:
            return self.root.__search(key)
        return None

    def min(self):
        if self.root:
            return self.root.__min()
        return None

    def max(self):
        if self.root:
            return self.root.__max()
        return None

    def successor(self, key):
        node = self.search(key)
        if node:
            return node.__successor()
        return None

    def predecessor(self, key):
        node = self.search(key)
        if node:
            return node.__predecessor()
        return None
