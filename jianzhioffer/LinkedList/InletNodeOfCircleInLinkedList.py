# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead:
            return None
        meet_node = self.ContainCircle(pHead)
        if not meet_node:
            return None
        p_node = meet_node.next
        circle_length = 1
        while p_node != meet_node:
            p_node = p_node.next
            circle_length += 1
        p2_node = p1_node = pHead
        i = 0
        while i < circle_length:
            p1_node = p1_node.next
            i += 1
        while p1_node != p2_node:
            p1_node = p1_node.next
            p2_node = p2_node.next
        return p1_node


    def ContainCircle(self, pHead):
        slow_node = pHead.next
        if slow_node:
            fast_node = slow_node.next
        else:
            return False
        while slow_node and fast_node and slow_node != fast_node:
            slow_node = slow_node.next
            fast_node = fast_node.next
            if fast_node:
                fast_node = fast_node.next
        if slow_node and fast_node and slow_node == fast_node:
            return fast_node
        else:
            return False

if __name__ == '__main__':
    array = [1,2,3,4,5,6,7]
    pHead = ListNode(0)
    p_node = pHead
    i_node = None
    for i in array:
        p_node.next = ListNode(i)
        p_node = p_node.next
        if i == 3:
            i_node = p_node
    if i_node:
        p_node.next = i_node
    p_node = pHead
    i = 0
    while i < 9 and p_node:
        print p_node.val,
        p_node = p_node.next
        i += 1
    print ""
    s = Solution()
    # print s.ContainCircle(pHead)
    one = ListNode(1)
    one.next = one
    result = s.EntryNodeOfLoop(one)
    if result:
        print result.val
    else:
        print None

