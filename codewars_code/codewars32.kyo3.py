import time
from math import sqrt
t1 = time.time()
'''
def pri(n):
    l = [True]*(n+1)
    for i in range(2,round(sqrt(n))+1):
        if l[i]:
            e = i*i
            while e<=n:
                l[e] =False
                e += i
    yield [i for i in range(2,n+1) if l[i]]

for i in pri(100000):
    print(i)
t2 = time.time()
print(t2-t1)
'''

def pri(n):
    flag = [1]*(n+2)
    p = 2
    while (p<=n):
        yield p
        for i in range(2*p,n+1,p):
            flag[i] = 0
        while 1:
            p+=1
            if(flag[p]==1):
                break
li = []
for i in pri(16000000):
    li.append(i)
t2 = time.time()
print(t2-t1)
