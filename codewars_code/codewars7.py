# 寻找一个数组中，不同的数（奇数组中的偶数，偶数组中的奇数）
# 如 [1,3,5,7,9,11,15,6] 返回6

'''
def find_outlier(integers):
    li1 = []
    li2 = []
    for i in integers:
        if i%2 !=0:
            li1.append(i)
        if i%2 ==0:
            li2.append(i)

    if len(li1) > len(li2):
        return li2[0]
    if len(li2) > len(li1):
        return li1[0]
'''
def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens = [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]


if __name__ == '__main__':
    a = [2,4,0,100,4,11,2602,36]
    r = find_outlier(a)
    print(r)

    
