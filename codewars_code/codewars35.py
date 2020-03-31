'''
from itertools import combinations

def mininum_steps(numbers,value):
    none = True
    for i in range(1,len(numbers)):
        for j in combinations(numbers,i):
            if sum(j) == value:
                return i-1
            else:
                none = True
    if none == True:
        return 0
'''

def mininum_steps(numbers,value):
    li = sorted(numbers)
    answer = 0
    for i in range(len(numbers)):
        answer += li[i]
        if answer == value:
            return i
            break
        else:
            none = True
    if none == True:
        return 0
        
            
#[1,10,12,9,2,3]    


if __name__ == '__main__':
#    r = mininum_steps([19,98,69,28,75,45,17,98,67],464)
    r = mininum_steps([1,10,12,9,2,3],6)
    print(r)

    
