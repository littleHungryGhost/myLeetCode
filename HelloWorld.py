class task_queue:
    queue = []
    num = 0

    def append(self, obj):
        self.queue.append(obj)

    def print_queue(self):
        print self.queue
def test():
    print "iner of the function"
print "outer of function"