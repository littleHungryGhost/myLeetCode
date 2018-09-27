# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        """ 若pRoot2为空指针，返回False"""
        # write code here
        result = False
        if not pRoot2 or not pRoot1:
            return False
        if pRoot1.val == pRoot2.val:
            result = self.CompareSubtree(pRoot1, pRoot2)
        if not result:
            result = self.HasSubtree(pRoot1.left, pRoot2)
        if not result:
            result = self.HasSubtree(pRoot1.right, pRoot2)
        return result

    def CompareSubtree(self, root1, root2):
        if not root2:
            return True
        if not root1:
            return False
        if root1.val != root2.val:
            return False
        else:
            return self.CompareSubtree(root1.left, root2.left) and self.CompareSubtree(root1.right, root2.right)

if __name__ == '__main__':
    from RebuildBinaryTree import Solution as BuildTree
    pre = [1, 2, 4, 7, 3, 5, 6, 8]
    tin = [4, 7, 2, 1, 5, 3, 8, 6]
    b = BuildTree()
    tree = b.reConstructBinaryTree(pre, tin)
    root1 = TreeNode(8)
    root1.left = TreeNode(8)
    root1.right = TreeNode(7)
    root1.left.left = TreeNode(9)
    root1.left.right = TreeNode(2)
    root1.left.right.left = TreeNode(4)
    root1.left.right.right = TreeNode(7)
    root2 = TreeNode(8)
    root2.left = TreeNode(9)
    root2.right = TreeNode(3)
    s = Solution()
    print s.HasSubtree(root1, root2)


