# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # Passing a null to the function? Return True if tree is not initialized
        if not root:
            return True
        # Initialize the queue by adding root.
        queue = [root]
        while len(queue) != 0:
            nextQueue = []  # queue to visit in next iteration, substitute to queue at the end of each round
            cmpList = []    # comparison list in which perserve None children for each level. Reduce the running minutes.
            for node in queue:  # Retrieve the node and adding their existed children to the nextQueue, adding all their children to the cmpList.
                if node.left:
                    nextQueue.append(node.left)
                cmpList.append(node.left)
                if node.right:
                    nextQueue.append(node.right)
                cmpList.append(node.right)
            # Pop from the beginning and the end. List is used as deque.
            while len(cmpList) > 1:
                left = cmpList.pop(0)
                right = cmpList.pop()
                if (left and right) and (left.val != right.val):
                    print(left, right)
                    return False
                elif (left and not right) or (not left and right):
                    print(left, right)
                    return False
            queue = nextQueue   # Replace the queue by nextQueue.
        return True