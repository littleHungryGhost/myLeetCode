class Solution:
    def maxProductAfterCutting_solution1(self, length):
        if length < 2:
            return 0
        if length == 2:
            return 1
        if length == 3:
            return 2
        products = [0 for i in range(length+1)]
        products[0] = 0
        products[1] = 1
        products[2] = 2
        products[3] = 3
        i = 4
        while i <=length:
            max = 0
            j = 1
            while j <= i/2:
                product = products[j] * products[i-j]
                if max < product:
                    max = product
                j += 1
            products[i] = max
            i += 1
        return products[length]
    def maxProductAfterCutting_solution2(self, length):
        if length < 2:
            return 0
        if length == 2:
            return 1
        if length == 3:
            return 2
        timesOf3 = length/3
        if length - timesOf3*3 == 1:
            timesOf3 -= 1
        timesOf2 = (length - timesOf3*3)/2
        return 3**timesOf3 * 2**timesOf2


if __name__ == '__main__':
    s = Solution()
    for i in range(100):
        a = s.maxProductAfterCutting_solution2(i)
        b = s.maxProductAfterCutting_solution1(i)
        if a != b:
            print i
        else:
            print a, " | ", b
