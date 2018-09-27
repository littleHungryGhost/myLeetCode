# -*- coding:utf-8 -*-
# 丑数
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index < 1 or not index:
            return 0
        ugly_numbers = [1]
        next_p = 1
        m2 = m3 = m5 = 0
        while next_p < index:
            min_num = min(ugly_numbers[m2]*2, ugly_numbers[m3]*3, ugly_numbers[m5]*5)
            ugly_numbers.append(min_num)
            while ugly_numbers[m2]*2 <= min_num:
                m2 += 1
            while ugly_numbers[m3]*3 <= min_num:
                m3 += 1
            while ugly_numbers[m5]*5 <= min_num:
                m5 += 1
            next_p += 1
        return ugly_numbers[index-1]

if __name__ == '__main__':
    s = Solution()
    print s.GetUglyNumber_Solution(1500)
