# 寻找列表中特殊数 如 [1,1,1,1,1,2,1,1,1]  返回2
'''
def find_uniq(arr):
    odd = [(arr[0]-1)]
    li1 = [x for x in arr if x-1 in odd]
    li2 = [y for y in arr if y-1 not in odd]
    return li1[0] if len(li1)< len(li2) else li2[0]


def find_uniq(arr):
    a,b = set(arr)
    return a if arr.count(a)==1 else b
'''

def find_uniq(arr):
    arr.sort()
    return arr[0] if arr.count(arr[0])==1 else arr[1]
    
if __name__ == '__main__':
    a = [-2,-2,-2,-2,-2,-2,-1]
    r = find_uniq(a)
    print(r)
