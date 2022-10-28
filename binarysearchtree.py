# Implementationo for BST from https://github.com/pagekeytech/education/blob/master/BST/bst.py
class TreeNode():
    def __init__(self, data):
        self.__data = data
        self.__left = None
        self.__right = None

    def get_data(self):
        return self.__data
    
    def get_left(self):
        return self.__left
    
    def get_right(self):
        return self.__right
    
    def set_data(self, data):
        self.__data = data
        
    def set_left(self, left_node):
        self.__left = left_node
        
    def set_right(self, right_node):
        self.__right = right_node
    
    def insert(self, data):
        if self.__data == data:
            return False
        elif data < self.__data:
            if self.__left:
                return self.__left.insert(data)
            else:
                self.__left = TreeNode(data)
                return True
        else:
            if self.__right:
                return self.__right.insert(data)
            else:
                self.__right = TreeNode(data)
                return True

    def search(self, data):
        if self.__data == data:
            return True
        elif data < self.__data and self.__left:
            return self.__left.search(data)
        elif data > self.__data and self.__right:
            return self.__right.search(data)
        return False

    def traverse(self, inorder_list):
        if self.__left:
            self.__left.traverse(inorder_list)
        inorder_list.append(self.__data)
        if self.__right:
            self.__right.traverse(inorder_list)
        return inorder_list
    
    ## represent implementation from https://stackoverflow.com/questions/62406562/how-to-print-a-binary-search-tree-in-python
    def __repr__(self):
        lines = []
        if self.__right:
            found = False
            for line in repr(self.__right).split("\n"):
                if line[0] != " ":
                    found = True
                    line = " ┌─" + line
                elif found:
                    line = " | " + line
                else:
                    line = "   " + line
                lines.append(line)
        lines.append(str(self.__data))
        if self.__left:
            found = False
            for line in repr(self.__left).split("\n"):
                if line[0] != " ":
                    found = True
                    line = " └─" + line
                elif found:
                    line = "   " + line
                else:
                    line = " | " + line
                lines.append(line)
        return "\n".join(lines) 

class BinarySearchTree():
    def __init__(self):
        self.__root = None
        self.__limit = None
        
    def get_root(self):
        return self.__root
    
    def get_limit(self):
        return self.__limit
    
    def set_root(self, node):
        self.__root = node
    
    def get_limit(self, value):
        self.__limit == value
    
    def is_empty(self):
        if self.__root is None:
            return True
        return False
    
    def is_full(self):
        if self.__limit == len(self.traverse()):
            return True
        return False
    
    # return True if successfully inserted, false if full or exists
    def insert(self, data):
        if self.is_full():
            return False
        elif self.__root:
            return self.__root.insert(data)
        else:
            self.__root = TreeNode(data)
            return True
    # return True if data is found in tree, false otherwise
    def search(self, data):
        if self.__root:
            return self.__root.search(data)
        else:
            return False
    # return True if node successfully removed, False if not removed
    def delete(self, data):
        # Case 1: Empty Tree?
        if self.is_empty():
            return False
        
        # Case 2: Deleting root node
        if self.__root.get_data() == data:
            # Case 2.1: Root node has no children
            if self.__root.get_left() is None and self.__root.get_right() is None:
                self.__root = None
                return True
            # Case 2.2: Root node has left child
            elif self.__root.get_left() and self.__root.get_right() is None:
                self.__root = self.__root.get_left()
                return True
            # Case 2.3: Root node has right child
            elif self.__root.get_left() is None and self.__root.get_right():
                self.__root = self.__root.get_right()
                return True
            # Case 2.4: Root node has two children
            else:
                moveNode = self.__root.get_right()
                moveNodeParent = None
                while moveNode.get_left():
                    moveNodeParent = moveNode
                    moveNode = moveNode.get_left()
                self.__root.set_data(moveNode.get_data())
                if moveNode.get_data() < moveNodeParent.get_data():
                    moveNodeParent.set_left(None)
                else:
                    moveNodeParent.set_right(None)
                return True		
        # Find node to remove
        parent = None
        node = self.__root
        while node and node.get_data() != data:
            parent = node
            if data < node.get_data():
                node = node.get_left()
            elif data > node.get_data():
                node = node.get_right()
        # Case 3: Node not found
        if node is None or node.get_data() != data:
            return False
        # Case 4: Node has no children
        elif node.get_left() is None and node.get_right() is None:
            if data < parent.get_data():
                parent.set_left(None)
            else:
                parent.set_right(None)
            return True
        # Case 5: Node has left child only
        elif node.get_left() and node.get_right() is None:
            if data < parent.get_data():
                parent.set_left(node.get_left())
            else:
                parent.set_right(node.get_left())
            return True
        # Case 6: Node has right child only
        elif node.get_left() is None and node.get_right():
            if data < parent.get_data():
                parent.set_left(node.get_right())
            else:
                parent.set_right(node.get_right())
            return True
        # Case 7: Node has left and right child
        else:
            moveNodeParent = node
            moveNode = node.get_right()
            while moveNode.get_left():
                moveNodeParent = moveNode
                moveNode = moveNode.get_left()
            node.set_data(moveNode.get_data())
            if moveNode.get_right():
                if moveNode.get_data() < moveNodeParent.get_data():
                    moveNodeParent.set_left(moveNode.get_right())
                else:
                    moveNodeParent.set_right(moveNode.get_right())
            else:
                if moveNode.get_data() < moveNodeParent.get_data():
                    moveNodeParent.set_left(None)
                else:
                    moveNodeParent.set_right(None)
            return True

    # return list of inorder elements
    def traverse(self):
        if self.__root:
            return self.__root.traverse([])
        else:
            return []
    
    ## represent implementation from https://stackoverflow.com/questions/62406562/how-to-print-a-binary-search-tree-in-python together with above __repr__ function
    def print_tree(self):
        print(self.__root)
 