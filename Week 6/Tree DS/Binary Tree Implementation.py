class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            self._insert_recursively(data, self.root)

    def _insert_recursively(self, data, current_node):
        if data < current_node.data:
            if current_node.left:
                self._insert_recursively(data, current_node.left)
            else:
                current_node.left = TreeNode(data)
        else:
            if current_node.right:
                self._insert_recursively(data, current_node.right)
            else:
                current_node.right = TreeNode(data)

    def remove(self, key):
        return self._remove_recursive_helper(self.root, key)
    
    def _remove_recursive_helper(self, current_node, key):
        if not current_node:
            return None
        
        if key < current_node.data:
            current_node.left = self._remove_recursive_helper(current_node.left, key)
        elif key > current_node.data:
            current_node.right = self._remove_recursive_helper(current_node.right, key)
        else:
            if not current_node.left and not current_node.right:
                return None
            elif not current_node.right:
                return current_node.left
            elif not current_node.left:
                return current_node.right
            else:
                successor = self._find_min_node(current_node.right)
                current_node.data = successor.data
                current_node.right = self._remove_recursive_helper(current_node.right, successor.data)
        
        return current_node

    def _find_min_node(self, current_node):
        while current_node.left:
            current_node = current_node.left
        return current_node

    def search(self, item):
        return self._search_recursively(item, self.root)
    
    def _search_recursively(self, item, current_node):
        if not current_node:
            return False
        if current_node.data == item:
            return True
        elif item < current_node.data:
            return self._search_recursively(item, current_node.left)
        else:
            return self._search_recursively(item, current_node.right)
        
    def inorder_traversal(self):
        return self._inorder_traversal_recursive(self.root)
    
    def _inorder_traversal_recursive(self, current_node):
        if current_node:
            return (
                self._inorder_traversal_recursive(current_node.left)
                + [current_node.data]
                + self._inorder_traversal_recursive(current_node.right)
            )
        return []
    
    def tree_height(self):
        return self._tree_height(self.root)
    
    def _tree_height(self, root):
        if not root:
            return -1
        
        left_height = self._tree_height(root.left)
        right_height = self._tree_height(root.right)

        return max(left_height, right_height) + 1
    
    def findClosest(self, target):
        return self._find_closest_helper(self.root, target)
    
    def _find_closest_helper(self, root, target):
        closest = root.data

        while root:
            if abs(root.data - target) < abs(closest - target):
                closest = root.data

            if target < root.data:
                root = root.left
            else:
                root = root.right  
        
        return closest

    def isBST(self):
        return self._is_BST(self.root, prev=[None])
    
    def _is_BST(self, root, prev):
        if root is None:
            return True
        
        if not self._is_BST(root.left, prev):
            return False
        
        if prev[0] is not None and root.data <= prev[0].data:
            return False
        
        prev[0] = root

        return self._is_BST(root.right, prev)

    
tree = BinaryTree()

tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)

tree.remove(2)

print(tree.inorder_traversal())
print("5 is in the Binary tree?", tree.search(5))

print("Height of the tree:", tree.tree_height())

print("Value Closest to 10 in the tree:", tree.findClosest(10))

print("Is the tree is a BST:", tree.isBST())
