# Implementationo for BST from https://github.com/pagekeytech/education/blob/master/BST/bst.py
class TreeNode(object):
	def __init__(self, d):
		self.data = d
		self.left = None
		self.right = None
  
	def insert(self, d):
		if self.data == d:
			return False
		elif d < self.data:
			if self.left:
				return self.left.insert(d)
			else:
				self.left = TreeNode(d)
				return True
		else:
			if self.right:
				return self.right.insert(d)
			else:
				self.right = TreeNode(d)
				return True

	def search(self, d):
		if self.data == d:
			return True
		elif d < self.data and self.left:
			return self.left.search(d)
		elif d > self.data and self.right:
			return self.right.search(d)
		return False

	def traverse(self, l):
		if self.left:
			self.left.traverse(l)
		l.append(self.data)
		if self.right:
			self.right.traverse(l)
		return l
		
class BinarySearchTree(object):
    def __init__(self):
        self.root = None
    # return True if successfully inserted, false if exists
    def insert(self, d):
        if self.root:
            return self.root.insert(d)
        else:
            self.root = TreeNode(d)
            return True
    # return True if d is found in tree, false otherwise
    def search(self, d):
        if self.root:
            return self.root.search(d)
        else:
            return False
    # return True if node successfully removed, False if not removed
    def delete(self, d):
        # Case 1: Empty Tree?
        if self.root == None:
            return False
        
        # Case 2: Deleting root node
        if self.root.data == d:
            # Case 2.1: Root node has no children
            if self.root.left is None and self.root.right is None:
                self.root = None
                return True
            # Case 2.2: Root node has left child
            elif self.root.left and self.root.right is None:
                self.root = self.root.left
                return True
            # Case 2.3: Root node has right child
            elif self.root.left is None and self.root.right:
                self.root = self.root.right
                return True
            # Case 2.4: Root node has two children
            else:
                moveNode = self.root.right
                moveNodeParent = None
                while moveNode.left:
                    moveNodeParent = moveNode
                    moveNode = moveNode.left
                self.root.data = moveNode.data
                if moveNode.data < moveNodeParent.data:
                    moveNodeParent.left = None
                else:
                    moveNodeParent.right = None
                return True		
        # Find node to remove
        parent = None
        node = self.root
        while node and node.data != d:
            parent = node
            if d < node.data:
                node = node.left
            elif d > node.data:
                node = node.right
        # Case 3: Node not found
        if node == None or node.data != d:
            return False
        # Case 4: Node has no children
        elif node.left is None and node.right is None:
            if d < parent.data:
                parent.left = None
            else:
                parent.right = None
            return True
        # Case 5: Node has left child only
        elif node.left and node.right is None:
            if d < parent.data:
                parent.left = node.left
            else:
                parent.right = node.left
            return True
        # Case 6: Node has right child only
        elif node.left is None and node.right:
            if d < parent.data:
                parent.left = node.right
            else:
                parent.right = node.right
            return True
        # Case 7: Node has left and right child
        else:
            moveNodeParent = node
            moveNode = node.right
            while moveNode.left:
                moveNodeParent = moveNode
                moveNode = moveNode.left
            node.data = moveNode.data
            if moveNode.right:
                if moveNode.data < moveNodeParent.data:
                    moveNodeParent.left = moveNode.right
                else:
                    moveNodeParent.right = moveNode.right
            else:
                if moveNode.data < moveNodeParent.data:
                    moveNodeParent.left = None
                else:
                    moveNodeParent.right = None
            return True

    # return list of inorder elements
    def traverse(self):
        if self.root:
            return self.root.traverse([])
        else:
            return []