# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root.left and not root.right:
            return root.val
        return self.helper(None, root, 0)[0]
    
    def helper(self, parent: TreeNode, node: TreeNode, level: int) -> int:
        if not node.left and not node.right:
            return (node.val, level)
        if node.left:
            leftVal, leftLevel = self.helper(node, node.left, level+1)
        else:
            leftVal, leftLevel = (None, -1)
        if node.right:
            rightVal, rightLevel = self.helper(node, node.right, level+1)
        else:
            rightVal, rightLevel = (None, -1)
        return (rightVal, rightLevel) if leftLevel<rightLevel else (leftVal, leftLevel)