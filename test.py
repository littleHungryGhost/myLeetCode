import  numpy as np
def split_data(data):
    original = data
    step = 20
    temp = [original[0:1,i:i+step].reshape(20).tolist() for i in range(original.shape[1]-step)]
    split_d = np.array(temp)
    return split_d

if __name__ == '__main__':
    data = np.array(range(30)).reshape(1,30)
    print split_data(data)