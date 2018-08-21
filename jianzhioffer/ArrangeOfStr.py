# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        ss = list(ss)
        result = []
        self.PermutationRecurse(ss, 0, result)
        return sorted(result)

    def PermutationRecurse(self, ss, index, result):
        n = len(ss)
        if index >= n:
            sss = "".join(ss)
            if not sss in result:
                result.append(sss)
            return
        else:
            i = index
            while i < n:
                temp = ss[i]
                ss[i] = ss[index]
                ss[index] = temp
                self.PermutationRecurse(ss, index + 1, result)
                temp = ss[i]
                ss[i] = ss[index]
                ss[index] = temp
                i += 1

if __name__ == '__main__':

    s = Solution()
    print s.Permutation('abc')



