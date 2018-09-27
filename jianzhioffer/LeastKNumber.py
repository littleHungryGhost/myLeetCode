# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if not tinput or k <= 0 or k > len(tinput):
            return []
        n = len(tinput)
        start = 0
        end = n - 1
        index = self.Partition(tinput, start, end)
        while index != k-1:
            if index < k-1:
                start = index + 1
                index = self.Partition(tinput, start, end)
            if index > k-1:
                end = index - 1
                index = self.Partition(tinput, start, end)
        result = tinput[:k]
        self.QuickSort(result, 0, k-1)
        return result

    def GetLeastNumbers_Solution2(self, tinput, k):
        if not tinput or k <= 0 or k > len(tinput):
            return []
        result = []
        n = len(tinput)
        i = 0
        while i < n:
            if len(result) < k:
                result.append(tinput[i])
            else:
                if tinput[i] < result[k-1]:
                    result.append(tinput[i])
                    self.QuickSort(result, 0, k)
                    result.pop()
            i += 1
        self.QuickSort(result, 0, k-1)
        return result

    def Partition(self, numbers, start, end):
        index = start
        small = start - 1
        while index < end:
            if numbers[index] < numbers[end]:
                small += 1
                if small != index:
                    temp = numbers[index]
                    numbers[index] = numbers[small]
                    numbers[small] = temp
            index += 1
        small += 1
        temp = numbers[small]
        numbers[small] = numbers[end]
        numbers[end] = temp
        return small

    def QuickSort(self, numbers, start, end):
        if not numbers:
            print "invalid input"
            return
        if start == end:
            return
        index = self.Partition(numbers, start, end)
        if index > start:
            self.QuickSort(numbers, start, index-1)
        if index < end:
            self.QuickSort(numbers, index+1, end)

if __name__ == '__main__':
    s = Solution()
    a = [3,2,1,4,5,9,7,8,6]
    s.QuickSort(a, 0, 8)
    print a
    print s.GetLeastNumbers_Solution2([3,2,1,4,6,5,7,8,9],4)