# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first = None
        second = None
        prev = None

        def inorder(node: TreeNode | None) -> None:
            nonlocal first, second, prev
            if not node:
                return
            inorder(node.left)

            if prev and prev.val > node.val:
                if not first:
                    first = prev
                second = node

            prev = node

            inorder(node.right)

        inorder(root)

        if first and second:
            first.val, second.val = second.val, first.val