class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0 or s[0] == '0':
            return 0
        if '00' in s:
            return 0
        # i = 0
        # while i<n:
        #     if s[i]=='0':
        #         i += 1
        #     else:
        #         break
        # if i<n:
        #     s = s[i:]
        # else:
        #     return 0
        if n == 1:
            return 1
        if n == 2:
            if int(s) > 26 or s == '10':
                return 1
            else:
                return 2
        if int(s[-2:]) <= 26:

            if s[-1] == '0':
                return self.numDecodings(s[:-2])
            if int(s[-2:]) > 10:
                return self.numDecodings(s[:-2]) + self.numDecodings(s[:-1])
            else:
                return self.numDecodings(s[:-1])
        else:
            if s[-1] == '0':
                return 0
            else:
                return self.numDecodings(s[:-1])


if __name__ == '__main__':
    s = Solution()
    print s.numDecodings('50926')