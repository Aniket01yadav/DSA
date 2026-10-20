class Queue:
    def __init__(self):
        self.items = []
    def add(self, item):
        self.items.append(item)
    def delete(self):
        if len(self.items) > 0:
            a = self.items.pop(0)
        return a
    def size(self):
        return len(self.items)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        ans = []

        if root is None:
            return ans
        
        queue = Queue()
        queue.add(root)
        ans.append([root.val])

        while queue.size() > 0:
            level = []

            for i in range(queue.size()):
                front = queue.delete()

                if front.left != None:
                    queue.add(front.left)
                    level.append(front.left.val)
                if front.right != None:
                    queue.add(front.right)
                    level.append(front.right.val)
            if len(level) > 0:
                if len(ans) % 2 == 1:
                    level.reverse()
                ans.append(level)
        return ans