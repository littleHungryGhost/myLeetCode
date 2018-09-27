# -*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    def search(self, root, x):
        if not root:
            return None
        if root.val == x:
            return root
        result = self.search(root.left, x)
        if result:
            return result
        result = self.search(root.right, x)
        if result:
            return result
        return None

    def reConstructBinaryTree(self, pre, tin, par):
    # write code here
        if not pre or not tin:
            return None
        if len(pre) != len(tin):
            print "invalid input!"
            return False
        root = TreeLinkNode(pre[0])
        # if len(pre) == 1 and len(tin) == 1:
        #     return root
        root_index = tin.index(root.val)
        root.left = self.reConstructBinaryTree(pre[1:root_index+1], tin[:root_index], root)
        root.right = self.reConstructBinaryTree(pre[root_index+1:], tin[root_index+1:], root)
        root.next = par
        return root

    def getNext(self, pNode):
        # write code here
        if not pNode:
            print "Null Pointer"
            return None
        if pNode.right:
            p = pNode.right
            while p.left:
                p = p.left
            return p
        elif pNode.next and pNode.next.left == pNode:
            return pNode.next
        elif pNode.next and pNode.next.right == pNode:
            p = pNode.next
            while p.next and p.next.right == p:
                p = p.next
            if not p.next:
                return None
            else:
                return p.next

if __name__ == '__main__':
    s = Solution()
    pre = [1, 2, 4, 7, 3, 5, 6, 8]
    tin = [4, 7, 2, 1, 5, 3, 8, 6]
    tree = s.reConstructBinaryTree(range(6), range(6), None)
    b = s.search(tree, 7)
    a = tree.right.right.right
    print a.val
    n = s.getNext(a)
    if n:
        print n.val
    else:
        print "None"





