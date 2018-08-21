# coding=utf-8
def getTranslateCount(number):
    if number < 0:
        return 0
    number_string = str(number)
    n = len(number_string)
    i = n - 1
    counts = [0 for i in range(n)]
    counts[i] = 1
    i -= 1
    while i >= 0:
        first = ord(number_string[i]) - ord('0')
        second = ord(number_string[i+1]) - ord('0')
        temp = 10*first + second
        if temp >= 10 and temp <= 25:
            if i < n - 2:
                counts[i] = counts[i+1] + counts[i+2]
            else:
                counts[i] = counts[i+1] + 1
        else:
            counts[i] = counts[i+1]
        i -= 1
    return counts[0]


if __name__ == '__main__':
    print getTranslateCount(1261)