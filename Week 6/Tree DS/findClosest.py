class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

def findClosest(root, target):
    closest = root.data

    while root:
        if abs(root.data - target) < abs(closest - target):
            closest = root.data

        if target < root.data:
            root = root.left
        else:
            root = root.right

    return closest

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

print(findClosest(root, 11))
