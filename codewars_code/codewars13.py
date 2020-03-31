'''
def nth_smallest(arr,pos):
    li = sorted(arr)
    return li[pos-1]
'''
def nth_smallest(arr,pos):
    return sorted(arr)[pos-1]

if __name__ == '__main__':
    r = nth_smallest([3,1,2],2)
    print(r)

    
