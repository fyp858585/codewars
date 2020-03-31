# find_all(10,3) [8,118,334]
# 返回相加起来等于10的3位数，返回一共有几个，最小的，最大的
# find_all(27,3) [1,999,999]
# find_all(84,4) []
# find_all(35,6) [123,116999,566666]
import time
t1 = time.time()

def find_all(sum_dig,digs):
    low = 1*10**(digs-1)
    high = 1*10**digs
    li = []
    for i in range(low,high):
        and1 = 0
        one_li = [int(j) for j in str(i)]
        if sorted(one_li) == one_li:
            if sum(one_li) == sum_dig:
                li.append(i)
    print(li)
    if len(li) == 0:
        return []
    return [len(li),li[0],li[-1]]
'''
from itertools import combinations_with_replacement

def find_all(sum_dig,digs):
    combs = combinations_with_replacement(list(range(1,10)),digs)
    target = [''.join(str(x) for x in list(comb)) for comb in combs if sum(comb) == sum_dig]
    if not target:
        return []
    return[len(target),int(target[0]),int(target[-1])]
'''
if __name__ == '__main__':
    r = find_all(10,3)
    print(r)
    t2 = time.time()
    print(t2-t1)
