# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not pushV or not popV:
            return False
        m = len(popV)
        n = len(pushV)
        if m != n:
            return False
        stack = []
        i = j = 0
        while i < m:
            num = popV[i]
            if stack and stack[-1] == num:
                i += 1
                stack.pop()
            else:
                while j < n and pushV[j] != num:
                    stack.append(pushV[j])
                    j += 1
                if j >= n:
                    return False
                else:
                    # 当前元素与要pop的元素一致，push后再pop，过程可以省略，但push、pop计数+1
                    i += 1
                    j += 1
        return True
if __name__ == '__main__':
    s = Solution()
    print s.IsPopOrder([1,2,3,4,5], [4,5,3,2,1])