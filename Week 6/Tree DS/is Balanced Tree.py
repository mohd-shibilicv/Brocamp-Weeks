class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def isBalanced(root):
    def getHeight(node):
        if node is None:
            return 0
        left_height = getHeight(node.left)
        right_height = getHeight(node.right)
        return max(left_height, right_height) + 1
    
    if root is None:
        return True
    
    left_height = getHeight(root.left)
    right_height = getHeight(root.right)

    if abs(left_height - right_height) > 1:
        return False

    return isBalanced(root.left) and isBalanced(root.right)


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

print(isBalanced(root))
