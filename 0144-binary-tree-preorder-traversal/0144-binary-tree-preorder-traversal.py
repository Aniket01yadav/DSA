# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def __init__(self):
    #     self.ans = []
    # def preorder(self, root):
    #     if root is None:
    #         return
    #     self.ans.append(root.val)
    #     self.preorder(root.left)
    #     self.preorder(root.right)
    # def preorderTraversal(self, root: TreeNode | None) -> list[int]:
    #     self.ans = []
    #     self.preorder(root)
    #     return self.ans

    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        ans = []

        def preorder(root):
            if not root:
                return 
            ans.append(root.val)
            preorder(root.left)
            preorder(root.right)
            
        preorder(root)
        return ans