# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        # return base**exponent
        if base == 0 and exponent < 0:
            raise ZeroDivisionError
        if base == 0 and exponent >= 0:
            return 0
        if exponent == 0:
            return 1
        abs_exponent = exponent
        if exponent < 0:
            abs_exponent = -exponent
        result = 1.0
        while abs_exponent > 0:
            result *= base
            abs_exponent -= 1
        if exponent < 0:
            result = 1.0/result
        return result




if __name__ == '__main__':
    s = Solution()
    print s.Power(0, 0)