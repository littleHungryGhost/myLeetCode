# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead:
            return None
        pre_node = None
        p_node   = pHead
        rev_node = None
        while p_node:
            next_node = p_node.next
            if not next_node:
                rev_node = p_node
            p_node.next = pre_node
            pre_node = p_node
            p_node = next_node
        return rev_node
    def ReverseList2(self, pHead):
        if not pHead:
            return None
        return self.reverse_recurse(pHead)
    def reverse_recurse(self, p_node):
        if not p_node or not p_node.next:
            return p_node
        next_node = p_node.next
        rev_node = self.reverse_recurse(next_node)
        next_node.next = p_node
        p_node.next = None
        return rev_node

if __name__ == '__main__':
    s = Solution()
    a = [1, 2, 3, 4, 5]
    # a = []
    pHead = ListNode(0)
    p_node = pHead
    for i in a:
        p_node.next = ListNode(i)
        p_node = p_node.next

    p_node = pHead
    while p_node:
        print p_node.val,
        p_node = p_node.next
    print ""
    p_node = s.ReverseList2(pHead)
    while p_node:
        print p_node.val,
        p_node = p_node.next
    print ""