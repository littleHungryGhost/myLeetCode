# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expect_number):
        # write code here
        if not root:
            return []
        path = []
        cur_sum = 0
        result = []
        self.FindPathRecurse(root, expect_number, path, cur_sum, result)
        return result

    def FindPathRecurse(self, root, expect_number, path, cur_sum, result):
        path.append(root.val)
        if not root.left and not root.right:
            if cur_sum + root.val == expect_number:
                path_copy = [i for i in path]
                result.append(path_copy)
        elif cur_sum + root.val <= expect_number:
            if root.left:
                self.FindPathRecurse(root.left, expect_number, path, cur_sum + root.val, result)
            if root.right:
                self.FindPathRecurse(root.right, expect_number, path, cur_sum + root.val, result)
        path.pop()
        return


if __name__ == '__main__':
    s = Solution()
    tree = TreeNode(10)
    tree.left = TreeNode(5)
    tree.right = TreeNode(12)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(7)
    print s.FindPath(tree, 15)
