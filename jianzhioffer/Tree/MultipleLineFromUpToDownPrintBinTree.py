# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        queue = []
        queue.append(pRoot)
        to_be_printed = 1
        next_level = 0
        result = []
        level_node = []

        while queue:
            cur_node = queue[0]
            level_node.append(cur_node.val)
            if cur_node.left:
                queue.append(cur_node.left)
                next_level += 1
            if cur_node.right:
                queue.append(cur_node.right)
                next_level += 1
            queue.pop(0)
            to_be_printed -= 1
            if to_be_printed == 0:
                result.append(level_node)
                to_be_printed = next_level
                next_level = 0
                level_node = []
        return result


