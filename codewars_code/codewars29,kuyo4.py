'''
from itertools import permutations as p
def permutations(string):
    li = []
    answer = []
    for i in p(string):
        li.append(''.join(i))
    for j in li:
        if j not in answer:
            answer.append(j)
    return answer



def per(s,start,end):
    li =[]
    if start >= end:
        print(s)
    else:
        for i in range(start,end):
            s[start],s[i] = s[i],s[start]
            per(s,start+1,end)
            s[start],s[i] = s[i],s[start]


def per(iterable,r=None):
    pool = list(iterable)
    n = len(pool)
    r = n if r is None else r
    if r >n:
        return
    indices = list(range(n))
    cycles = list(range(n,n-r,-1))
    yield list(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] ==0:
                indices[i:] = indices[i+1:]+indices[i:i+1]
                cycles[i] = n-i
            else:
                j = cycles[i]
                indices[i],indices[-j] = indices[-j],indices[i]
                yield list(pool[i] for i in indices[:r])
                break
        else:
            return

def permutations(string):
    li = []
    answer =[]
    p = per(string,len(string))
    for i in p:
        li.append(i)
    for i in li:
        if ''.join(i) not in answer:
            answer.append(''.join(i))
    return answer
'''

def permutations(string):
    if len(string) ==1:
        return set(string)
    first = string[0]
    rest = permutations(string[1:])
    result = set()
    for i in range(0,len(string)):
        for p in rest:
            result.add(p[0:i] +first + p[i:])
    return result












if __name__ == '__main__':
    p = permutations('aabb')
    print(p)
    


