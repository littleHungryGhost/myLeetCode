# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        l3 = ListNode((l1.val+l2.val)%10)
        p = l3
        surplus = (l1.val+l2.val)/10
        p1 = l1.next
        p2 = l2.next
        while p1 and p2:
            p.next = ListNode((p1.val+p2.val)%10 + surplus)
            surplus = (p1.val+p2.val)/10
            p1 = p1.next
            p2 = p2.next
        if not p2:
            if not p1:
                if surplus != 0:
                    l3 = ListNode(surplus)
                return l3
            while p1:
                l3 = ListNode(p1.val + surplus)
                p1 = p1.next
        else:
            while p2:
                l3 = ListNode(p2.val + surplus)
                p2 = p2.next
        return l3

if __name__ == '__main__':
    s = Solution()
    # print s.addTwoNumbers([2,4,3],[5,6,4])
