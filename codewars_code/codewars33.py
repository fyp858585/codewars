import math
def pri():
    li = []
    for i in range(2,10000):
        y = int(math.sqrt(i)+1)
        for j in range(2,y):
            if i % j==0:
                break
        else:
            rev_num = int(str(i)[::-1])
            for k in range(2,rev_num):
                if rev_num%k==0:
                    break
            else:
                li.append(i)
    return li

r = pri()
print(len(r))
print(r)


def prime(n):
    return r[n]

for i in range(259):
    print(prime(i))



