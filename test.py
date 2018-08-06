class task_queue:
    queue = []
    num = 0

    def append(self, obj):
        self.queue.append(obj)

    def print_queue(self):
        print self.queue


if __name__ == "__main__":
    a = 1
    for i in range(256):
        a = a << 1
        print i+1, " ", a