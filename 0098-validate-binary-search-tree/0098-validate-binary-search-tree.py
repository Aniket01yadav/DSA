# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def checkBinary(self, root, mn, mx):
        if root is None:
            return True

        if root.val < mn or root.val > mx:
            return False

        checkLeft = self.checkBinary(root.left, mn, root.val-1)
        checkRight = self.checkBinary(root.right, root.val+1, mx)

        return checkLeft and checkRight
        
    def isValidBST(self, root: TreeNode | None) -> bool:
        return self.checkBinary(root, float('-inf'), float('inf'))
