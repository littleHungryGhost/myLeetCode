# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.hash_table = [-1 for i in range(256)]
        self.index = 0
    # 返回对应char
    def FirstAppearingOnce(self):
        # write code here
        i = 0
        min = 256
        res = "#"
        while i < 256:
            if self.hash_table[i] >=0 and self.hash_table[i] < min:
                res = chr(i)
                min = self.hash_table[i]
            i += 1
        return res


    def Insert(self, char):
        # write code here
        if self.hash_table[ord(char)] == -1:
            self.hash_table[ord(char)] = self.index
        elif self.hash_table[ord(char)] >= 0:
            self.hash_table[ord(char)] = -2
        self.index += 1


if __name__ == '__main__':
    s = Solution()
    a = "BabyBaby"
    for i in a:
        s.Insert(i)
        print s.FirstAppearingOnce(),
