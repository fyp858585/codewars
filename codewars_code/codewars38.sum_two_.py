from itertools import combinations
def sum_two(numbers,target):
    li = []
    for i in range(len(numbers)):
        for j in range(1,len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i,j]
            
def two_sum(nums,t):
    for i,x in enumerate(nums):
        for j,y in enumerate(nums):
            if i != j and x + y == t:
                return [i,j]

                
def two_sum(nums,target):
    
    d = {}
    for i ,num in enumerate(nums):
        diff = target - num
        if diff in d:
            return [d[diff],i]
        d[num] = i


if __name__ == '__main__':
    r = sum_two([1,2,3,5],5)
    print(r)


