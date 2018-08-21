# -*- coding:utf-8 -*-
class Solution:
    """build queue by two stack"""
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        # write code here
        self.stack1.append(node)
    def pop(self):
        # return xx
        if self.stack2:
            return self.stack2.pop()
        elif not self.stack1:
            return None
        else:
            while self.stack1:
                temp = self.stack1.pop()
                self.stack2.append(temp)
            return self.stack2.pop()
class Solution2():
    """build stack by two queue """
    que1 = []
    que2 = []
    def push(self, node):
        if self.que1:
            self.que1.append(node)
        else:
            self.que2.append(node)
    def pop(self):
        if self.que1:
            while self.que1:
                temp = self.que1.pop(0)
                if not self.que1:
                    return temp
                self.que2.append(temp)
        elif not self.que2:
            return None
        else:
            while self.que2:
                temp = self.que2.pop(0)
                if not self.que2:
                    return temp
                self.que1.append(temp)

if __name__ == '__main__':
    s = Solution2()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print s.pop()
    print s.pop()
    print s.pop()
    print s.pop()
    print s.pop()
