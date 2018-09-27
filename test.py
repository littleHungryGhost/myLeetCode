import  numpy as np
class A(object):
    def __init__(self, x):
        self.val = x
        self.next = None
def split_data(data):
    original = data
    step = 20
    temp = [original[0:1,i:i+step].reshape(20).tolist() for i in range(original.shape[1]-step)]
    split_d = np.array(temp)
    return split_d
def test(head):
    if head.next:
        head = head.next
if __name__ == '__main__':
    # data = np.array(range(30)).reshape(1,30)
    # print split_data(data)
    head = A(5)
    p = head.next
    for i in [4, 2, 1, 3]:
        p = A(i)
        p = p.next
    test(head)
    print head.val