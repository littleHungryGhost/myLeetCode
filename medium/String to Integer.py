class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        MAX = 2 ** 31 - 1
        MIN = -2 ** 31
        number = ""
        sign = 1
        str = str.strip()
        i = 0
        if str == "":
            return 0
        if str[0] == '-' or str[0] == '+':
            sign = int(str[0] + "1")
            str = str[1:]
        for char in str:
            if char.isdigit():
                number += char
                i += 1
            else:
                break
        if len(number) > 0:
            result = sign * int(number)
            if result > MAX:
                return MAX
            elif result < MIN:
                return MIN
            else:
                return result
        else:
            return 0

if __name__ == '__main__':
    s = Solution()
    print s.myAtoi("-91283472332")