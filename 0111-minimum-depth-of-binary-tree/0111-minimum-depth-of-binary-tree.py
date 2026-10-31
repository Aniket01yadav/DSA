# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        
        if root is None:
            return 0
        
        leftHeight = self.minDepth(root.left)
        rightHeight = self.minDepth(root.right)

        if root.left is None:
            return rightHeight + 1
        
        if root.right is None:
            return leftHeight + 1

        return min(leftHeight, rightHeight) + 1