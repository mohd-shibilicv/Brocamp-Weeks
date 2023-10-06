class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, item):
        if not self.root:
            self.root = TreeNode(item)
        else:
            self._insert_recursive_helper(item, self.root)
    
    def _insert_recursive_helper(self, item, current_node):
        if item < current_node.data:
            if current_node.left:
                return self._insert_recursive_helper(item, current_node.left)
            else:
                current_node.left = TreeNode(item)
        else:
            if current_node.right:
                return self._insert_recursive_helper(item, current_node.right)
            else:
                current_node.right = TreeNode(item)

    def contains(self, target):
        return self._contains_recursive_helper(target, self.root)
    
    def _contains_recursive_helper(self, target, current_node):
        if not current_node:
            return False
        
        if current_node.data == target:
            return True
        elif target < current_node.data:
            return self._contains_recursive_helper(target, current_node.left)
        else:
            return self._contains_recursive_helper(target, current_node.right)

    def InOrderTraversal(self):
        return self._inorder_traversal_helper(self.root)
    
    def _inorder_traversal_helper(self, current_node):
        while current_node:
            return (
                self._inorder_traversal_helper(current_node.left)
                + [current_node.data]
                + self._inorder_traversal_helper(current_node.right)
            )
        return []
    
    def PreOrderTraversal(self):
        return self._preorder_traversal_helper(self.root)
    
    def _preorder_traversal_helper(self, current_node):
        while current_node:
            return (
                [current_node.data]
                + self._preorder_traversal_helper(current_node.left)
                + self._preorder_traversal_helper(current_node.right)
            )
        return []
    
    def PostOrderTraversal(self):
        return self._postorder_traversal_helper(self.root)
    
    def _postorder_traversal_helper(self, current_node):
        while current_node:
            return (
                self._postorder_traversal_helper(current_node.left)
                + self._postorder_traversal_helper(current_node.right)
                + [current_node.data]
            )
        return []
    
    def treeHeight(self):
        return self._tree_height_helper(self.root)
    
    def _tree_height_helper(self, current_node):
        if not current_node:
            return -1
        
        left_tree = self._tree_height_helper(current_node.left)
        right_tree = self._tree_height_helper(current_node.right)

        return max(left_tree, right_tree) + 1
    
    def remove(self, item):
        return self._remove_recursive_helper(item, self.root)
    
    def _remove_recursive_helper(self, item, current_node):
        if not current_node:
            return None
        
        if item < current_node.data:
            current_node.left = self._remove_recursive_helper(item, current_node.left)
        elif item > current_node.data:
            current_node.right = self._remove_recursive_helper(item, current_node.right)
        else:
            # Case 1 : Node has no child
            if not current_node.left and not current_node.right:
                return None
            # Case 2 : Node has one child (right)
            elif not current_node.left:
                return current_node.right
            # Case 3 : Node has one child (left)
            elif not current_node.right:
                return current_node.left
            # Case 4 : Node has two children
            else:
                successor = self._find_min_node(current_node.right)
                current_node.data = successor.data
                current_node.right = self._remove_recursive_helper(successor.data, current_node.right)

        return current_node

    def _find_min_node(self, current_node):
        while current_node.left:
            current_node = current_node.left
        return current_node

    def _find_max_node(self, current_node):
        while current_node.right:
            current_node = current_node.right
        return current_node
    
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


tree = BinaryTree()

tree.insert(250)
tree.insert(200)
tree.insert(300)
tree.insert(50)

# tree.remove(50)

print(tree.InOrderTraversal())
print(tree.PreOrderTraversal())
print(tree.PostOrderTraversal())

print(tree.contains(250))

print(tree.findClosest(100))

print(tree.treeHeight())
