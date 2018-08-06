# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        if not s:
            return False
        # 判断整数位

        integer, s = self.judgeInterger(s)
        num = integer
        if s and s[0] == '.':
            dec, s = self.judgeUnsignedInteger(s[1:])
            num = integer or dec
        if s and (s[0] == 'e' or s[0] == 'E'):
            exponent, s = self.judgeInterger(s[1:])
            num = num and exponent
        return num and not s



    def judgeInterger(self, s):
        if s and (s[0] == '+' or s[0] == '-'):
            return self.judgeUnsignedInteger(s[1:])
        return self.judgeUnsignedInteger(s)
    def judgeUnsignedInteger(self, s):
        i = 0
        n = len(s)
        while i < n and ord(s[i]) >= ord('0') and ord(s[i]) <= ord('9'):
            i += 1
        return i > 0, s[i:]


if __name__ == '__main__':
    s = Solution()
    print s.isNumeric('e12')