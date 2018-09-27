# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        stack = [[], []]
        current = 0
        next = current ^ 1
        stack[current].append(pRoot)
        result = []
        level_node = []
        while stack[0] or stack[1]:
            cur_node = stack[current].pop()
            level_node.append(cur_node.val)
            if current == 0:
                if cur_node.left:
                    stack[next].append(cur_node.left)
                if cur_node.right:
                    stack[next].append(cur_node.right)
            else:
                if cur_node.right:
                    stack[next].append(cur_node.right)
                if cur_node.left:
                    stack[next].append(cur_node.left)
            if not stack[current]:
                result.append(level_node)
                level_node = []
                current ^= 1
                next ^= 1
        return result
    def Print2(self, root):
        if not root:
            return []
        queue = []
        queue.append(root)
        to_be_printed = 1
        next_level = 0
        result = []
        level_node = []
        level = 1
        while queue:
            cur_node = queue.pop(0)
            level_node.append(cur_node.val)
            if cur_node.left:
                queue.append(cur_node.left)
                next_level += 1
            if cur_node.right:
                queue.append(cur_node.right)
                next_level += 1
            to_be_printed -= 1
            if to_be_printed == 0:
                result.append(level_node[::level])
                level_node = []
                to_be_printed = next_level
                next_level = 0
                level *= -1
        return  result





if __name__ == '__main__':
    from RebuildBinaryTree import Solution as BuildTree
    build = BuildTree()
    pre = [1,2,4,8,9,5,10,11,3,6,12,13,7,14,15]
    tin = [8,4,9,2,10,5,11,1,12,6,13,3,14,7,15]
    tree = build.reConstructBinaryTree(pre,tin)
    s = Solution()
    print s.Print2(tree)


