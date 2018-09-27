"""
class A():
    
    def add(self,n):
        return 0
class B():
    def add(self,n):
        return arr[bool(n)].add(n-1) + n
a = A()
b = B()
arr = [a,b]    
print arr[1].add(100)
"""
def A(n):
    return 0
def B(n):
    return arr[bool(n)](n-1)+n
arr = [A,B]
print arr[1](100)

