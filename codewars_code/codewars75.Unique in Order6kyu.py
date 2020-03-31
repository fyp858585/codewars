# 'AABBBCCCCDDAABB' 返回 ['A', 'B', 'C', 'D', 'A', 'B']
# 'ABBCcAD' 返回 ['A', 'B', 'C', 'c', 'A', 'D']
# [1,2,2,3,3] 返回 [1,2,3]

'''
def unique_in_order(iterable):
    li = []
    for i in range(len(iterable)):
        if i +1 >= len(iterable):
            if iterable[i-1] == iterable[i]:
                if i == len(iterable)-1:
                    if li[-1]!= iterable[i]:
                        li.append(iterable[i])
            else:
                li.append(iterable[i])
        else:
            if iterable[i]==iterable[i+1]:
                pass
            else:
                li.append(iterable[i])
    return li


def unique_in_order(iterable):
    li = []
    long = len(iterable)
    for i in range(long):
        if i+1<long:
            if iterable[i] == iterable[i+1]:
                pass
            else:
                li.append(iterable[i])
        else:
            li.append(iterable[i])
    return li

'''
def unique_in_order(iterable):
    result = []
    prev = None
    for i in iterable:
        if i != prev:
            result.append(i)
            prev = i
    return result




if __name__ == '__main__':
    r = unique_in_order('ABBCcAD')
    print(r)
