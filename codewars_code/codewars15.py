'''
def duplicates(a):
    ans = 0
    for i in set(a):
        if a.count(i) == 1:
            pass
        else:
            ans += (a.count(i)//2)
    return ans
'''
def duplicates(a):
    return sum(a.count(i)//2 for i in set(a))


if __name__ == '__main__':
#    r = duplicates([1,2,2,20,6,20,2,6,2])
    r = duplicates([0,0,0,0,0,0,0])
    print(r)

    
    
