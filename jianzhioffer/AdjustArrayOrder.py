# -*- coding:utf-8 -*-
class Solution:

    def reOrderArray(self, array):
        # write code here
        if not array:
            return array
        n = len(array)
        i = 0
        while i < n:
            if not self.judgeFun(array[i]):
                array.append(array.pop(i))
                n -= 1
            else:
                i += 1
        return array
    def judgeFun(self, element):
        """ whether is odd """
        return element & 0x01


if __name__ == '__main__':
    s = Solution()
    array = [1,2,3,4,5,6,8,7,9,11,13,15,17]
    print s.reOrderArray(array)
    print array



