# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return None
        p_head, p_tail = self.ConvertNode(pRootOfTree)
        return p_head
    def ConvertNode(self, root):
        if root.left:
            left_min_node, left_max_node = self.ConvertNode(root.left)
            root.left = left_max_node
            left_max_node.right = root
            min_node = left_min_node
        else:
            min_node = root
        if root.right:
            right_min_node, right_max_node = self.ConvertNode(root.right)
            root.right = right_min_node
            right_min_node.left = root
            max_node = right_max_node
        else:
            max_node = root
        return min_node, max_node

    def Convert2(self, pRootOfTree):
        if not pRootOfTree:
            return None
        last_node_inlist = [None, ]
        self.ConvertNode2(pRootOfTree, last_node_inlist)
        pnode = last_node_inlist[0]
        while pnode.left:
            pnode = pnode.left
        return pnode


    def ConvertNode2(self, root, last_node_inlist):
        if root.left:
            self.ConvertNode2(root.left, last_node_inlist)
        root.left = last_node_inlist[0]
        if last_node_inlist[0]:
            last_node_inlist[0].right = root
        last_node_inlist[0] = root
        if root.right:
            self.ConvertNode2(root.right, last_node_inlist)




if __name__ == '__main__':
    s = Solution()
    pre = [10,6,4,8,14,12,16]
    tin = [4,6,8,10,12,14,16]
    from jianzhioffer.Tree.RebuildBinaryTree import Solution as BuildTree
    build = BuildTree()
    tree = build.reConstructBinaryTree(pre,tin)
    phead = s.Convert2(tree)
    pnode = phead
    while pnode:
        print pnode.val,
        pnode = pnode.right


