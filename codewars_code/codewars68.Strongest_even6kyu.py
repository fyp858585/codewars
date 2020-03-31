'''
偶数的强度是可以连续初一2直到达以偶数n开头的奇数的次数
例如 如果n=12则
12/2=6
6/2=3
我们相继分化了2次达到3，所以12强度为2
如果n=16
16/2=8
8/2=4
4/2=2
2/2=1
我们相继分化了4次达到1，所以16强度为4

任务
给定一个封闭的间隔[n,m],返回间隔中最强的偶数。如果存在多个解
则返回最小的最强偶数

输入（1,2）返回2
输入（5,10）返回8
输入（12,14）返回12
输入（48,56）返回48
输入（129,193）返回192
'''

def strongest_even(n,m):
    dic = {}
    for i in range(n,m+1):
        num = i
        time = 0
        while i % 2 == 0:
            i = i/2
            time+=1
        if time in dic:
            if dic[time]>num:
                dic[time] = num
        else:
            dic[time] = num
    return dic[max(dic)]

'''

def strongest_even(n,m):
    while True:
        if m & m -1 <n:
            return m
        m &= m-1
        
'''


if __name__ == '__main__':
    r = strongest_even(14,20)
    print(r)
    
