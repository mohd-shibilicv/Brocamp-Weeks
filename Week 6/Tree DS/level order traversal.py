class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def levelOrderTraversal(root):
    if root is None:
        return []
    
    result = []
    queue = [root]

    while queue:
        current = queue.pop(0)
        result.append(current.value)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return result


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

print(levelOrderTraversal(root))
