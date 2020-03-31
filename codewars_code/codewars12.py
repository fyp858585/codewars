# [-2,1,-3,4,-1,2,1,-5,4]

def maxSequence(arr):
    if arr == []:
        return 0
    max_sum = arr[0]
    pre_sum = 0
    for i in arr:
        if pre_sum <0:
            pre_sum = i
        else:
            pre_sum += i
        if pre_sum > max_sum:
            max_sum = pre_sum
    if max_sum < 0:
        return 0
    else:
        return max_sum

if __name__ == '__main__':
    r = maxSequence([-1])
    print(r)

