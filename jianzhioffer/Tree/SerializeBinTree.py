# -*- coding:utf-8 -*-
from __future__ import print_function
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    index = 0

    def Serialize(self, root):
        # write code here

        if not root:
            return []
        s = []
        self.SerializeRecurse(root, s)
        return s
    def SerializeRecurse(self, root, s):
        if not root:
            s.append('$')
            return
        else:
            s.append(root.val)
            self.SerializeRecurse(root.left, s)
            self.SerializeRecurse(root.right, s)


    def Deserialize(self, s):
        # write code here
        if not s:
            return None
        root = self.DeserializeRecurse(s)
        return root
    def DeserializeRecurse(self, s):
        if self.index < len(s) and s[self.index].isdigit():
            cur_node = TreeNode(s[self.index])
            self.index += 1
            cur_node.left = self.DeserializeRecurse(s)
            cur_node.right = self.DeserializeRecurse(s)
            return cur_node
        else:
            self.index += 1
            return None
if __name__ == '__main__':
    s = Solution()
    tree = s.Deserialize('124$$$35$$6$$')
    result = s.Serialize(tree)
    print(result)


