class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_binary_search_tree(root):
    def helper(node, min_value, max_value):
        if node is None:
            return True
        
        if not (min_value < node.value < max_value):
            return False
        
        return (
            helper(node.left, min_value, node.value) and helper(node.right, node.value, max_value)
        )
    
    return helper(root, float('-inf'), float('inf'))

def isBST(root):
    def helper(node, min_val, max_val):
        if not node:
            return True
        
        if not (min_val < node.value < max_val):
            return False
        
        return (helper(node.left, min_val, node.value) and helper(node.right, node.value, max_val))

    return helper(root, float('-inf'), float('inf'))

# Test the is_binary_search_tree function
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

print(is_binary_search_tree(root))
print(isBST(root))