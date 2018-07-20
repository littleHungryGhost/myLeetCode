# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if not listNode:
            return []
        stack = []
        p_node = listNode
        while p_node:
            stack.append(p_node.val)
            p_node = p_node.next
        return stack[::-1]
