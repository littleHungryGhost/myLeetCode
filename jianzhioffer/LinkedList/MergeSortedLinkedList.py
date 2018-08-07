# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1:
            return pHead2
        elif not pHead2:
            return pHead1
        #else:
        if pHead1.val <= pHead2.val:
            merge_list_head = pHead1
            merge_list_head.next = self.Merge(pHead1.next, pHead2)
        else:
            merge_list_head = pHead2
            merge_list_head.next = self.Merge(pHead1, pHead2.next)
        return merge_list_head

    def Merge2(self, pHead1, pHead2):
        if not pHead1:
            return pHead2
        elif not pHead2:
            return pHead1
        #else:
        p1_node = pHead1
        p2_node = pHead2
        if p1_node.val <= p2_node.val:
            pHead = p1_node
            p1_node = p1_node.next
        else:
            pHead = p2_node
            p2_node = p2_node.next
        p_node = pHead
        while p1_node and p2_node:
            if p1_node.val < p2_node.val:
                p_node.next = p1_node
                p1_node = p1_node.next
            else:
                p_node.next = p2_node
                p2_node = p2_node.next
            p_node = p_node.next
        if p1_node:
            p_node.next = p1_node
        else:   #if p2_node:
            p_node.next = p2_node
        return pHead
if __name__ == '__main__':
    s = Solution()
    a = [1, 3, 5, 7, 8, 9]
    b = [2, 4, 6, 8, 10]
    # a = []
    pHead1 = ListNode(0)
    p_node = pHead1
    for i in a:
        p_node.next = ListNode(i)
        p_node = p_node.next
    pHead2 = ListNode(0)
    p_node = pHead2
    for i in b:
        p_node.next = ListNode(i)
        p_node = p_node.next

    p_node = pHead1
    while p_node:
        print p_node.val,
        p_node = p_node.next
    print ""
    p_node = pHead2
    while p_node:
        print p_node.val,
        p_node = p_node.next
    print ""
    pHead = s.Merge2(pHead1, None)
    p_node = pHead
    while p_node:
        print p_node.val,
        p_node = p_node.next
    print ""