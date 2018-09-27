#coding=utf-8
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        head, end = self.quickSort(head,None)
        return head

    def quickSort(self,head,end):
        if head == end:
            return head,end
        start, med, end = self.partition(head, end)
        s1, e1 = self.quickSort(start, med)
        s2, e2 = self.quickSort(med.next, end)
        e1.next = s2
        return s1, e2

    def partition(self, start, end):
        p = med = start
        value = start.val
        while p != end:
            tmp = p.next
            if not tmp:
                break
            if tmp and tmp.val < value:
                p.next = tmp.next
                tmp.next = start
                start = tmp
            else:
                p = tmp
        return start, med, end


if __name__ == '__main__':
    s = Solution()
    head = ListNode(5)
    p = head
    for i in [4,2,1,3]:
        p.next = ListNode(i)
        p = p.next

    head = s.sortList(head)
    print "hello"



