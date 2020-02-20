# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        self.insertHelper(None, root, val)
        return root
        
    def insertHelper(self, parent: TreeNode, node: TreeNode, val: int):
        if node.val < val:
            if node.right:
                self.insertHelper(node, node.right, val)
            else:
                node.right = TreeNode(val)
        elif node.val > val:
            if node.left:
                self.insertHelper(node, node.left, val)
            else:
                node.left = TreeNode(val)