# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        return self.compare(pRoot, pRoot)
    def compare(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        if root1 == root2:
            return self.compare(root1.left, root2.right)
        else:
            return self.compare(root1.left, root2.right) and self.compare(root1.right, root2.left)