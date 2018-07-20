# -*- coding:utf-8 -*-
class Solution:
    # 题目：替换空格
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        if not s:
            return False
        l = len(s)
        if l == 0:
            return s
        counter = 0
        for i in s:
            if i == ' ':
                counter += 1
        l1 = l + 2*counter
        result = [' ']*l1
        i = l1 - 1
        j = l - 1
        while j >= 0 and i >= 0:
            if s[j] != ' ':
                result[i] = s[j]
                i -= 1
                j -= 1
            else:
                result[i] = '0'
                result[i-1] = '2'
                result[i-2] = '%'
                i -= 3
                j -= 1
        return "".join(result)

    def replaceSpace2(self, s):
        return s.replace(" ", "%20")
if __name__ == '__main__':
    s = Solution()
    a = " ab  c d "
    b = "abcd"
    print s.replaceSpace2(a)
