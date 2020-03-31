'''
def odd_one(arr):
    li1 = [i for i in arr if i%2 ==0]
    li2 = [i for i in arr if i%2 !=0]
    if len(li1)==0 or len(li2) ==0:
        return -1
    else:
        return arr.index(li1[0]) if len(li1) < len(li2) else arr.index(li2[0])
'''

def odd_one(arr):
    return next((i for i,v in enumerate(arr) if v&1),-1)



if __name__ == '__main__':
    r = odd_one([2,4,6,7,10])
    print(r)





'''
    for i in arr:
        if i % 2 == 0:
            li1.append(i)
        else:
            li2.append(i)
'''
