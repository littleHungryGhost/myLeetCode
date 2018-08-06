# -*- coding:utf-8 -*-
class Solution:
    counter = {}
    def Fibonacci1(self, n):
        # write code here
        if n == 1:
            return 1
        elif n == 0 :
            return 0
        if self.counter.has_key(n):
            return self.counter[n]
        else:
            result = self.Fibonacci(n-1)+self.Fibonacci(n-2)
            self.counter[n] = result
            return result
    def Fibonacci2(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        a = 0
        b = 1
        i = 2
        while i <= n:
            c = a + b
            a = b
            b = c
            i += 1
        return c
    def matrix_power(self, a, n):
        """ failed!!! """
        if n == 1:
            return a
        if n == 2:
            return [[a[0][0]**2+a[0][1]*a[1][0], a[0][0]*a[0][1]+a[0][1]*a[1][1]],
                    [a[1][0]*a[0][0]+a[1][1]*a[1][0], a[1][0]*a[0][1]+a[1][1]**2]]
        if n/2 == 1:
            return self.matrix_power(a, (n-1)/2)*self.matrix_power(a, 1)
        else:
            return self.matrix_power(a, n/2)
    


if __name__ == '__main__':
    s = Solution()
    print s.Fibonacci2(10)

