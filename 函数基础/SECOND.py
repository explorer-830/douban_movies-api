def area(*args):
    max_num=max(args)
    min_num=min(args)
    average=sum(args)/len(args)
    return max_num,min_num,average#
print(area(2,34,5,6,1,7,22))
def first(x,y):
    return x+y
def second(x,y):
    return x-y
def add(x,y,z):
    return z(x,y)
result=add(10,220,first)
second(2,1)
