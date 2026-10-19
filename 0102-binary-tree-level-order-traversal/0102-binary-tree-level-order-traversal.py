class Queue:
    def __init__(self):
        self.items = []
        
    def Add(self, item):
        self.items.append(item)
    
    def Remove(self):
        if len(self.items) > 0:
            a = self.items.pop(0)
            return a
        else:
            return None
    def size(self):
        return len(self.items)
    


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        ans = []

        if root is None:
            return ans
        
        queue = Queue()
        queue.Add(root)
        ans.append([root.val])

        while queue.size() > 0:
            l = queue.size()
            level = []

            for i in range(l):
                front = queue.Remove()
                if front.left != None:
                    queue.Add(front.left)
                    level.append(front.left.val)
                if front.right != None:
                    queue.Add(front.right)
                    level.append(front.right.val)
            if len(level) > 0:
                ans.append(level)
        return ans