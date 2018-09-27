# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root:
            return
        if not root.left and not root.right:
            return
        temp = root.left
        root.left = root.right
        root.right = temp
        if root.left:
            self.Mirror(root.left)
        if root.right:
            self.Mirror(root.right)
    def Mirror2(self, root):
        if not root:
            return
        stack = []
        stack.append(root)
        while stack:
            cur_node = stack.pop()
            if not cur_node.left and not cur_node.right:
                continue
            temp = cur_node.left
            cur_node.left = cur_node.right
            cur_node.right = temp
            if cur_node.left:
                stack.append(cur_node.left)
            if cur_node.right:
                stack.append(cur_node.right)

