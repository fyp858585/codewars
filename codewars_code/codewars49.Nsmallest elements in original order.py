# [1,2,3,4,5] 3  return [1,2,3]
# [5,4,3,2,1] 3  return [3,2,1]
# [1,2,3,4,1] 3  return [1,2,1]
# [1,2,3,-4,0] 3 return [1,-4,0]
# [1,2,3,4,5] 0  return []


def first_n_smallest(arr,n):
    small = sorted(arr)[:n]
    answer = []
    for i in arr:
        if i in small:
            answer.append(i)
            small.remove(i)
    return answer

if __name__ == '__main__':
    r = first_n_smallest([1,2,3,4,1],3)
    print(r)
    
