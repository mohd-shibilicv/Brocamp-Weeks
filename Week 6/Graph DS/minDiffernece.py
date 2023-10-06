class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDiffInBST(root):
    def inorder(node):
        nonlocal prev, min_diff
        if node:
            inorder(node.left)
            
            if prev is not None:
                min_diff = min(min_diff, abs(node.val - prev))
            prev = node.val
            
            inorder(node.right)
    
    prev = None
    min_diff = float('inf')
    
    inorder(root)
    return min_diff


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

result = minDiffInBST(root)
print("Minimum distance:", result)  # Output: 1
