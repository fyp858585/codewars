# 给定一个数组，返回其所有元素相加的值 例子 输入[1,2,3,4,5] 返回 15
'''
def sum_array(a):
    answer = 0
    for i in a:
        answer += i
    return answer
'''

def sum_array(a):
    return sum(a)

if __name__ == '__main__':
    r = sum_array([1,2,3,4,5])
    print(r)


