class Queue:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)

    def delete(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        ans = []

        if root is None:
            return ans
        
        queue = Queue()
        queue.push(root)
        ans.append(root.val)
        
        while queue.size() > 0:
            level = []
            for i in range(queue.size()):
                front = queue.delete()
                if front.left != None:
                    queue.push(front.left)
                    level.append(front.left.val)
                if front.right != None:
                    queue.push(front.right)
                    level.append(front.right.val)
            if len(level) > 0:
                ans.append(sum(level)/len(level))
        return ans