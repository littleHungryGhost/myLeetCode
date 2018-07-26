# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
    # write code here
        if not pre or not tin:
            return None
        if len(pre) != len(tin):
            print "invalid input!"
            return False
        root = TreeNode(pre[0])
        if len(pre) == 1 and len(tin) == 1:
            return root
        root_index = tin.index(root.val)
        root.left = self.reConstructBinaryTree(pre[1:root_index+1], tin[:root_index])
        root.right = self.reConstructBinaryTree(pre[root_index+1:], tin[root_index+1:])
        return root

    def

if __name__ == '__main__':
    s = Solution()
    pre = [1,2,4,7,3,5,6,8]
    tin = [4,7,2,1,5,3,8,6]
    tree = s.reConstructBinaryTree([1], [1])
    print "hello"

