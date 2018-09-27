# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        """
        :param numbers: 输入数组 
        :param duplication: 0位置放结果
        :return: 
        """
        l = len(numbers)
        if l == 0:
            return False
        counters = {}
        for i in numbers:
            if counters.has_key(i):
                duplication[0] = i
                return True
            else:
                counters[i] = 1

        return False

    def duplicate2(self, numbers, duplication):
        l = len(numbers)
        if l == 0:
            return False
        for i,j in enumerate(numbers):
            while i != j:
                if j == numbers[j]:
                    duplication[0] = j
                    return True,j
                numbers[i] = numbers[j]
                numbers[j] = j
                j = numbers[i]
        return False



# write code here
if __name__ == '__main__':
    s = Solution()
    a = [0,1]
    print s.duplicate([2,1,3,1,4],a), a[0]