# Find the odd int 返回数组中出现奇数次的数
# [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5] 返回5
# [1,1,2,-2,5,2,4,4,-1,-2,5] 返回 -1
 
def find_it(seq):
    count = 0
    for i in seq:
        if seq.count(i)%2 != 0:
            count = i
    return count

if __name__ == '__main__':
    r = find_it([1,1,2,-2,5,2,4,4,-1,-2,5])
    print(r)

