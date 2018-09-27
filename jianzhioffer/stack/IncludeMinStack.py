# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.__stack = []
        self.__min_stack = []
    def push(self, node):
        # write code here
        self.__stack.append(node)
        if len(self.__min_stack) == 0 or node < self.__min_stack[-1]:
            self.__min_stack.append(node)
        else:
            self.__min_stack.append(self.__min_stack[-1])

    def pop(self):
        # write code here
        if self.__min_stack and self.__stack:
            self.__min_stack.pop()
            return self.__stack.pop()
        else:
            return None

    def top(self):
        # write code here
        if self.__min_stack and self.__stack:
            return self.__stack[-1]
        else:
            return None

    def min(self):
        # write code here
        if self.__min_stack and self.__stack:
            return self.__min_stack[-1]
        else:
            return None

if __name__ == '__main__':
    s = Solution()
    """["PSH3","MIN","PSH4","MIN","PSH2","MIN","PSH3","MIN","POP","MIN","POP","MIN","POP","MIN","PSH0","MIN"]
"""
    s.push(3)
    print s.min()
    s.push(4)
    s.push(2)
    print s.min()
