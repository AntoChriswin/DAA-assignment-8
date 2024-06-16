class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def heightAfterSubtreeRemoval(root, queries):
    def dfs(node):
        if not node:
            return 0
        left_height = dfs(node.left)
        right_height = dfs(node.right)
        return 1 + max(left_height, right_height)

    def removeSubtree(node, target):
        if not node:
            return None
        if node.val == target:
            return None
        node.left = removeSubtree(node.left, target)
        node.right = removeSubtree(node.right, target)
        return node

    result = []
    for query in queries:
        root = removeSubtree(root, query)
        result.append(dfs(root))

    return result

# Example
root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(4)
root1.left.left = TreeNode(2)
root1.left.right = None
root1.right.left = TreeNode(6)
root1.right.right = TreeNode(5)
root1.right.left.left = None
root1.right.left.right = None
root1.right.right.left = None
root1.right.right.right = TreeNode(7)
queries1 = [4]
print(heightAfterSubtreeRemoval(root1, queries1))  # Output: [2]

root2 = TreeNode(5)
root2.left = TreeNode(8)
root2.right = TreeNode(9)
root2.left.left = TreeNode(2)
root2.left.right = TreeNode(1)
root2.right.left = TreeNode(3)
root2.right.right = TreeNode(7)
root2.left.left.left = TreeNode(4)
root2.left.left.right = TreeNode(6)
queries2 = [3, 2, 4, 8]
print(heightAfterSubtreeRemoval(root2, queries2))  # Output: [3, 2, 3, 2]
