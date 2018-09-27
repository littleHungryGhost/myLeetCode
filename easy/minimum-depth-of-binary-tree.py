# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        temp = []
        temp.append(root)
        root.val = 1
        while len(temp) > 0:
            p = temp.pop(0)
            left = p.left
            right = p.right
            if left or right:
                if left:
                    left.val = p.val + 1
                    temp.append(left)
                if right:
                    right.val = p.val + 1
                    temp.append(right)
            else:
                return p.val

