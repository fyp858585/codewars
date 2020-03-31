# 例子 531,513 ；135，-1； 2071，2017； 414,144； 907,790；21,12；

from itertools import permutations

def next_smaller(n):
    if len(str(n)) == 1:
        return -1
    li = []
    for i in permutations(str(n),len(str(n))):
        if int(''.join(i)) < n:
            li.append(int(''.join(i)))
    if len(li) == 0:
        return -1
    else:
        return max(li)

if __name__ == '__main__':
    r = next_smaller(135)
    print(r)

