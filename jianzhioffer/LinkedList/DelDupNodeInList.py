# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead:
            print "input is null!"
            return
        pre_node = None
        p_node = pHead
        while p_node:
            next_node = p_node.next
            is_duplicate = False
            if next_node and next_node.val == p_node.val:
                is_duplicate = True
            if not is_duplicate:
                pre_node = p_node
                p_node = p_node.next
            else:
                value = p_node.val
                while p_node and p_node.val == value:
                    p_node = p_node.next
                if pre_node:
                    pre_node.next = p_node
                else:
                    pHead = p_node
        return pHead

if __name__ == '__main__':
    s = Solution()
    a = [1,2,3,4,5]
    pHead = ListNode(0)
    p_node = pHead
    for i in a:
        p_node.next = ListNode(i)
        p_node = p_node.next

    pHead = s.deleteDuplication(pHead)
    p_node = pHead
    while p_node:
        print p_node.val
        p_node = p_node.next





