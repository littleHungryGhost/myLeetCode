# coding=utf-8
class Solution:
    def print1ToMaxOfNDigits1(self, n):
        if n <= 0:
            return
        number = ['0' for i in range(n)]
        while not self.increment(number, n):
            self.printNumStr(number,n)

    def increment(self,number, n):
        is_over_flow = False
        flow = 0
        i = n-1
        while i >= 0:
            index = ord(number[i]) - ord('0') + flow
            if i == n-1:
                index += 1
            if index >= 10:
                if i == 0:
                    is_over_flow = True
                    return is_over_flow
                else:
                    index -= 10
                    flow = 1
                    number[i] = str(index)
            else:
                number[i] = str(index)
                break
            i -= 1
        return is_over_flow

    def printNumStr(self, number, n):
        i = 0
        while i < n:
            if number[i] != '0':
                break
            i += 1
        print "".join(number[i:])

    def print1ToMaxOfNDigits2(self, n):
        if n <= 0:
            return
        number = ['0' for i in range(n)]
        i = 0
        while i < 10:
            number[0] = str(i)
            self.print_recurse(number, n, 1)
            i += 1

    def print_recurse(self, number, n, index):
        if index == n:
            self.printNumStr(number, n)
            return
        for i in range(10):
            number[index] = str(i)
            self.print_recurse(number, n, index+1)

if __name__ == '__main__':
    s = Solution()
    s.print1ToMaxOfNDigits1(2)