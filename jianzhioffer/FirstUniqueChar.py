# -*- coding:utf-8 -*-
# 第一个只出现一次的字符
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s:
            return -1
        hash_table = [0 for i in range(ord('z')-ord('A')+1)]
        n = len(s)
        i = 0
        while i < n:
            index = ord(s[i])-ord('A')
            hash_table[index] += 1
            i += 1
        i = 0
        while i < n:
            index = ord(s[i]) - ord('A')
            if hash_table[index] == 1:
                return i
            i += 1
        return -1

if __name__ == '__main__':
    s = Solution()
    print s.FirstNotRepeatingChar("NXWtnzyoHoBhUJaPauJaAitLWNMlkKwDYbbigdMMaYfkVPhGZcrEwp")
