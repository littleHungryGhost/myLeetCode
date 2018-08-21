# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        numbers_copy = [str(i) for i in numbers]
        sorted_numbers = sorted(numbers_copy, cmp=self.compare)
        print sorted_numbers
        return "".join(sorted_numbers)
    def compare(self, num1, num2):
        comb1 = num1+num2
        comb2 = num2+num1
        if comb1 < comb2:
            return -1
        if comb1 == comb2:
            return 0
        if comb1 > comb2:
            return 1
        return cmp(comb1, comb2)
if __name__ == '__main__':
    s = Solution()
    print s.PrintMinNumber([32,3,321])
