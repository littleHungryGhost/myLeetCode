# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return None
        result = numbers[0]
        times = 1
        i = 1
        n = len(numbers)
        while i < n:
            if times == 0:
                result = numbers[i]
                times = 1
            elif result == numbers[i]:
                times += 1
            else:
                times -= 1
            i += 1
        if not self.CheckMoreThanHalf(numbers, result):
            result = None
        return result

    def MoreThanHalfNum_Solution2(self, numbers):
        if not numbers:
            return None
        n = len(numbers)
        middle = n >> 1
        start = 0
        end = n-1
        index = self.Partition(numbers, start, end)
        while middle != index:
            if middle < index:
                end = index - 1
                index = self.Partition(numbers, start, end)
            if middle > index:
                start = index + 1
                index = self.Partition(numbers, start, end)
        result = numbers[index]
        if not self.CheckMoreThanHalf(numbers, result):
            result = None
        return result

    def Partition(self, numbers, start, end):
        n = len(numbers)
        # 应该有个随机函数，随机选取某个值，但需要调用外部包，这里不调用，直接选择数组最后一个数。
        small = start - 1
        index = start
        while index < end:
            if numbers[index] < numbers[end]:
                small += 1
                if small != index:
                    temp = numbers[index]
                    numbers[index] = numbers[small]
                    numbers[small] = temp
            index += 1
        small += 1
        temp = numbers[end]
        numbers[end] = numbers[small]
        numbers[small] = temp
        return small

    def CheckMoreThanHalf(self, numbers, number):
        n = len(numbers)
        times = 0
        for i in numbers:
            if i == number:
                times += 1
        if times*2 <= n:
            return False
        else:
            return True

if __name__ == '__main__':
    s = Solution()
    print s.MoreThanHalfNum_Solution2([1,2,3,2,2,2,5,4,2])