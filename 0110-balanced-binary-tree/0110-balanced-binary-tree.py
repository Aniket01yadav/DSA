# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.ans = True
    def heightCal(self, root: TreeNode | None) -> bool:
        
        if root is None:
            return 0

        leftHeight = self.heightCal(root.left)
        rightHeight = self.heightCal(root.right)

        if abs(leftHeight - rightHeight) > 1:
            self.ans = False
        
        return max(leftHeight, rightHeight) + 1

    def isBalanced(self, root: TreeNode | None) -> bool:
        self.heightCal(root)
        return self.ans
    