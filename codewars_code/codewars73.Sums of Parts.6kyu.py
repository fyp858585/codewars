'''
ls = [0,1,3,6,10]
过程
ls = [0,1,3,6,10] sum = 20
ls = [1,3,6,10] sum = 20
ls = [3,6,10] sum = 19
ls = [6,10] sum = 16
ls = [10] sum = 10
ls = [] sum = 0
相应的总和[20,20,19,16,10,0]
其他例子：
ls = [1,2,3,4,5,6]
返回 [21, 20, 18, 15, 11, 6, 0]
'''
'''
def parts_sums(ls):
    long = len(ls)
    sum1 = sum(ls)
    answer = [sum1]
    for i in range(long):
        sum1 -= ls[i]
        answer.append(sum1)

    return answer
'''

def parts_sums(ls):
    answer = [sum(ls)]
    for item in ls:
        answer.append(answer[-1]-item)
    return answer

if __name__ == '__main__':
    r = parts_sums([0,1,3,6,10])
    print(r)
