# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head or not k:
            return None
        i = 0
        p_node = head
        while i < k-1 and p_node:
            p_node = p_node.next
            i += 1
        if not p_node:
            return None
        k_node = head
        while p_node.next:
            p_node = p_node.next
            k_node = k_node.next
        return k_node


if __name__ == '__main__':
    s = Solution()
    a = [1, 2, 3, 4, 5]
    pHead = ListNode(0)
    p_node = pHead
    for i in a:
        p_node.next = ListNode(i)
        p_node = p_node.next

    p_node = pHead
    while p_node:
        print p_node.val,
        p_node = p_node.next
    result = s.FindKthToTail(pHead, 0)
    print ""
    p_node = result
    while p_node:
        print p_node.val,
        p_node = p_node.next
