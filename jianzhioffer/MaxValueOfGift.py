# coding=utf-8
def getMaxValueOfGift(values, row, col):
    if not values or row <= 0 or col <= 0 or len(values) < row*col:
        return 0
    max_value = [0 for i in range(col)]
    i = 0
    while i < row:
        j = 0
        while j < col:
            up = left = 0
            if i > 0:
                up = max_value[j]
            if j > 0:
                left = max_value[j-1]
            max_value[j] = max(up, left) + values[i*col+j]
            j += 1
        i += 1
    return max_value[col-1]

if __name__ == '__main__':
    print getMaxValueOfGift([1,2,3,4,5,6], 6, 1)