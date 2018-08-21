# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if type(n) != int or n <= 0:
            return 0
        string = str(n)
        return self.NumberOf1(string)
    def NumberOf1(self, string):
        if not string:
            return 0
        length = len(string)
        first = ord(string[0]) - ord('0')
        if length == 1 and first == 0:
            return 0
        if length == 1 and first > 0:
            return 1
        num_of_max_bit = 0
        if first > 1:
            num_of_max_bit = 10 ** (length-1)
        if first == 1:
            num_of_max_bit = int(string[1:]) + 1
        num_of_last_bit = first*(length-1)*(10**(length-2))
        num_of_min_bit = self.NumberOf1(string[1:])
        return num_of_max_bit + num_of_last_bit + num_of_min_bit

if __name__ == '__main__':
    s = Solution()
    print s.NumberOf1Between1AndN_Solution(10000)