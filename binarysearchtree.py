class TreeNode():
    def __init__(self, value = None):
        self.__value = value
        self.__l_node = None
        self.__r_node = None
        
    def get_value(self):   
        return self.__value
    
    def get_node(self, node):
        node = node.lower()
        if node == "right" or node == "r":
            return self.__r_node
        elif node == "left" or node == "l":
            return self.__l_node
        else:
            raise NameError("'{}' unknown node, must be either '(l)eft' or '(r)ight'".format(node))
        
    def set_value(self, value):
        self.__value = value

    def set_nodes(self, l_node = None, r_node = None):
        self.__l_node = l_node
        self.__r_node = r_node
 
# Implementation based on: https://blog.boot.dev/computer-science/binary-search-tree-in-python/       
class BinarySearchTree():
    def __init__(self, root, limit = None):
        self.__root = root
        self.__limit = limit
        
    def get_root(self):
        return self.__root

    def get_limit(self):
        try:
            if self.__limit == None:
                return self.__limit
            elif isinstance(self.__limit, int):
                return self.__limit
        except ValueError as e:
            print(e)
            
    def set_root(self, root):
        self.__root = root
    
    def set_limit(self, limit):
        try:
            if isinstance(self.__limit, int):
                self.__limit = limit
        except TypeError as e:
            print(e)
        
    def is_empty(self):
        if self.__root is None:
            return True
        
    def is_full(self, root):
        if root.get_node('r') is None and root.get_node('l') is None:
            return True
        if root.get_node('r') is not None and root.get_node('l') is not None:
            return (self.is_full(root.get_node('r')) and self.is_full(root.get_node('l')))
        return False
    
    def search(self, root, value):
        if value == root.get_value():
            return True
        if value < root.get_value():
            if root.get_node('l') == None:
                return False
            return self.root.get_node('l').search(root.get_node('l'), value)
        if root.get_node('r') == None:
            return False
        return self.get_node('r').search(root.get_node('r'), value)
    
    def insert(self, root, value):
        if not root.get_value():
            root.set_value(value)
            return

        if root.get_value() == value:
            return

        if value < root.get_value():
            if root.get_node('l'):
                root.get_node('l').insert(root, value)
                return
            left_node = TreeNode(value)
            root.get_node('l').set_nodes(l_node=left_node)
            return

        if root.get_node('r'):
            root.get_node('r').insert(root, value)
            return
        right_node = TreeNode(value)
        root.get_node('r').set_nodes(r_node=right_node)
        return
    
    def delete(self, root, value):
        if root == None:
            return root
        if value < root.get_value():
            root.get_node('l') = self.left.delete(value)
            return self
        if value > self.value:
            self.right = self.right.delete(value)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.value = min_larger_node.value
        self.right = self.right.delete(min_larger_node.value)
        return self
    
    def traverse():
        pass
    
    def print_tree():
        pass       
        