# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, p_head):
        # write code here
        if not p_head:
            return None
        p_copy = p_copy_head = RandomListNode(p_head.label)
        p_node = p_head
        copy_dict = {}
        copy_dict[p_node] = p_copy
        p_node = p_node.next
        while p_node:
            p_copy.next = RandomListNode(p_node.label)
            p_copy = p_copy.next
            copy_dict[p_node] = p_copy
            p_node = p_node.next
        p_node = p_head
        p_copy = p_copy_head
        while p_node:
            if p_node.random:
                p_copy.random = copy_dict[p_node.random]
            p_node = p_node.next
            p_copy = p_copy.next
        return p_copy_head

    def Clone2(self, p_head):
        if not p_head:
            return None
        p_node = p_head
        # 原节点与复制节点逐次相连成一个链表
        while p_node:
            p_copy = RandomListNode(p_node.label)
            p_copy.next = p_node.next
            p_node.next = p_copy
            p_node = p_copy.next
        # 复制链表的random指针
        p_node = p_head
        while p_node:
            if p_node.random:
                p_copy = p_node.next
                p_copy.random = p_node.random.next
            p_node = p_node.next.next
        # 拆分链表
        p_node = p_head
        p_copy = p_copy_head = p_head.next
        while p_copy.next:
            next_node = p_copy.next
            p_node.next = next_node
            p_copy.next = next_node.next
            p_node = next_node
            p_copy = p_copy.next
        p_node.next = None
        return p_copy_head,p_head




if __name__ == '__main__':
    s = Solution()
    linked_list = RandomListNode(0)
    p_node = linked_list
    import random
    for i in [1,2,3,4,5]:
        p_node.next = RandomListNode(i)
        p_node = p_node.next
    p_node = linked_list.next
    p_node.random = p_node.next
    p_node = p_node.next
    p_node.random = p_node.next.next
    p_node = p_node.next
    p_node.random = p_node
    # p_node = linked_list.next
    # while p_node:
    #     random_num = random.randint(0, 4)
    #     random_node = linked_list.next
    #     i = 0
    #     while i < random_num:
    #         random_node = random_node.next
    #         i += 1
    #     p_node.random = random_node
    #     print p_node.label, p_node.random.label,
    #     p_node = p_node.next
    p_node = linked_list.next
    while p_node:
        print p_node.label,
        # if p_node.random:
        #     print p_node.random.label,
        # else:
        #     print "#",
        p_node = p_node.next
    print ""
    result, input_data = s.Clone2(linked_list.next)
    p_node = result
    while p_node:
        print p_node.label,
        p_node = p_node.next
    p_node = input_data
    print ""
    while p_node:
        print p_node.label,
        p_node = p_node.next

